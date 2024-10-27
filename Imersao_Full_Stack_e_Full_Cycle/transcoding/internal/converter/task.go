package converter

import (
	"database/sql"
	"encoding/json"
	"fmt"
	"log/slog"
	"os"
	"os/exec"
	"path/filepath"
	"regexp"
	"sort"
	"strconv"
	"time"
)

type VideoConverter struct {
	db *sql.DB
}

func NewVideoConverter(db *sql.DB) *VideoConverter {
	return &VideoConverter{
		db: db,
	}
}

// {"video_id": "1", "path": "media/uploads/1"}
type VideoTask struct {
	VideoID int    `json:"video_id"`
	Path    string `json:"path"`
}

func (vc *VideoConverter) Handle(msg []byte) {
	var task VideoTask
	err := json.Unmarshal(msg, &task)
	if err != nil {
		vc.logErrror(task, "failed to unmarshal task", err)
		return
	}

	if IsProcessed(vc.db, task.VideoID) {
		slog.Warn("Video already processed", slog.Int("video_id", task.VideoID))
		return
	}

	err = vc.processVideo(&task)
	if err != nil {
		vc.logErrror(task, "failed to process video", err)
		return
	}

	err = MarkProcessed(vc.db, task.VideoID)
	if err != nil {
		vc.logErrror(task, "failed to mark video as processed", err)
		return
	}

	slog.Info("Video marked as processd", slog.Int("video_id", task.VideoID))

}

func (vc *VideoConverter) processVideo(task *VideoTask) error {
	mergedFile := filepath.Join(task.Path, "merged.mp4")
	mpegDashPath := filepath.Join(task.Path, "mpeg-dash")

	slog.Info("Merging chunks", slog.String("path", task.Path))
	err := vc.mergeChunks(task.Path, mergedFile)
	if err != nil {
		vc.logErrror(*task, "failed to merge chunks", err)
		return fmt.Errorf("failed to merge chunks: %v", err)
	}

	slog.Info("Creating mpeg-dash dir", slog.String("path", task.Path))
	err = os.MkdirAll(mpegDashPath, os.ModePerm)
	if err != nil {
		vc.logErrror(*task, "failed to create mpeg-dash directory", err)
		return fmt.Errorf("failed to create mpeg-dash directory: %v", err)
	}

	slog.Info("Convertin video to mpeg-dash", slog.String("path", task.Path))
	ffmpegCmd := exec.Command(
		"ffmpeg", "-i", mergedFile,
		"-f", "dash",
		filepath.Join(mpegDashPath, "output.mpd"),
	)

	output, err := ffmpegCmd.CombinedOutput()
	if err != nil {
		vc.logErrror(*task, "failed to convert video to mpeg-dash, output:"+string(output), err)
		return err
	}

	slog.Info("Video converted to mpeg-dash", slog.String("path", mpegDashPath))

	slog.Info("Removing merged file", slog.String("path", mergedFile))
	err = os.Remove(mergedFile)
	if err != nil {
		vc.logErrror(*task, "failed to remove merged file", err)
		return err
	}

	return nil
}

func (vc *VideoConverter) logErrror(task VideoTask, message string, err error) {
	errorData := map[string]interface{}{
		"video_id": task.VideoID,
		"error":    message,
		"details":  err.Error(),
		"time":     time.Now(),
	}

	serializedError, _ := json.Marshal(errorData)
	slog.Error("Processing error", slog.String("error_details", string(serializedError)))

	RegisterError(vc.db, errorData, err)
}

func (vc *VideoConverter) extractNumber(fileName string) int {
	re := regexp.MustCompile(`\d+`)
	numStr := re.FindString(filepath.Base(fileName)) // String
	num, err := strconv.Atoi(numStr)
	if err != nil {
		return -1
	}
	return num
}

func (vc *VideoConverter) mergeChunks(inputDir, outputFile string) error {
	chunks, err := filepath.Glob(filepath.Join(inputDir, "*.chunk"))
	if err != nil {
		return fmt.Errorf("failed to find chhunks %v", err)
	}

	sort.Slice(chunks, func(i, j int) bool {
		return vc.extractNumber(chunks[i]) < vc.extractNumber(chunks[j])
	})

	output, err := os.Create(outputFile)
	if err != nil {
		return fmt.Errorf("failed to create output file %v", err)
	}
	defer output.Close()

	for _, chunk := range chunks {
		input, err := os.Open(chunk)
		if err != nil {
			return fmt.Errorf("failed to open chunk: %v", err)
		}

		_, err = output.ReadFrom(input)
		if err != nil {
			return fmt.Errorf("failed to write chunk %s to merge file: %v", chunk, err)
		}
		input.Close()
	}

	return nil
}

package main

import "imersaofc/transcoding/internal/converter"

func main() {
	vc := converter.NewVideoConverter()
	vc.Handle([]byte(`{"video_id": "1", "path": "mediatest/media/uploads/1"}`))
}

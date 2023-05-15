package entity

import (
	"errors"
	"time"

	"github.com/google/uuid"
	tiktoken_go "github.com/j178/tiktoken-go"
)

// Struct que representa A mensagem
type Message struct {
	ID        string
	Role      string
	Content   string
	Tokens    int
	Model     *Model
	CreatedAt time.Time
}

// NewMessage cria uma instancia de Message
func NewMessage(role, content string, model *Model) (*Message, error) {
	totalTokens := tiktoken_go.CountTokens(model.GetModelName(), content)
	msg := &Message{
		ID:        uuid.New().String(),
		Role:      role,
		Content:   content,
		Tokens:    totalTokens,
		Model:     model,
		CreatedAt: time.Now(),
	}
	if err := msg.Validate(); err != nil {
		return nil, err
	}
	return msg, nil
}

// Validate faz a validação dos campos na criação de uma instância
func (m *Message) Validate() error {
	if m.Role != "user" && m.Role != "system" && m.Role != "assistant" {
		return errors.New("invalid role")
	}
	if m.Content == "" {
		return errors.New("content is empty")
	}
	if m.CreatedAt.IsZero() {
		return errors.New("invalid created at")
	}
	return nil
}

// GetQtdTokens retorna a quantidade de to
func (m *Message) GetQtdTokens() int {
	return m.Tokens
}

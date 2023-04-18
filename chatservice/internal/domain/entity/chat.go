package entity

type ChatConfig struct {
	Model *Model
}

type Chat struct {
	ID         string
	UserID     string
	Status     string
	TokenUsage int
	Config     *ChatConfig
}

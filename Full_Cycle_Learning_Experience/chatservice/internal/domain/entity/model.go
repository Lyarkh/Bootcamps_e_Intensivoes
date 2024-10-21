package entity

type Model struct {
    Name string
    MaxTokens int
}

// NewModel cria uma instância de Model
func NewModel(name string, maxTokens int) *Model {
    return &Model{
        Name: name,
        MaxTokens: maxTokens,
    }
}

// GetMaxTokens retorna a quantidade maxima de tokens
func (m *Model) GetMaxTokens() int {
    return m.MaxTokens
}

// GetModelName retorna o nome do modelo
func (m *Model) GetModelName() string {
    return m.Name
}
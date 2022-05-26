//Type assertions
type JogoAssertion = {
    nome: string;
    descricao: string;
}

let jogo = {} as JogoAssertion;  // pode ser escrito da mesma maneira como <JogoAssetion> {}
jogo.nome = 'nome jogo';
jogo.descricao = 'descricao jogo'


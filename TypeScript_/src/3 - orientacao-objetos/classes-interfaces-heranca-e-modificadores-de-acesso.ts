// classes e Funções
class Usuario {
    public nome;
    public idade;

    constructor(nome: string, idade: number){
        this.nome = nome;
        this.idade = idade;
    }
}

// static e extends

class Player extends Usuario {
    public jogo;

    constructor(nome: string, idade: number, jogo:string){
        super(nome, idade);

        this.jogo = jogo;
    }

    dizerOJogoAtual() {
        return `Estou jogando, no momento: ${this.jogo}`
    }

   
    static queHorasSao() {
        return Date();
    }
}


const jogador = new Player('Carlos', 25, 'League of legends');
console.log(jogador.dizerOJogoAtual());
console.log(Player.queHorasSao());

// private, protected, public
class Jogo {
    protected nome; // O protected funciona como o privado mas classe herdada consegue acessar ela
    
    constructor(nome: string){
        this.nome = nome;
    }

    dizerNome() {
        return `O nome do jogo é: ${this.nome}`
    }
}

// const ghost = new Jogo('Ghost of Tsuchima');
//console.log(ghost.nome);   -> Erro por transformar o 'nome' em privado
// console.log(ghost.dizerNome())

/* class JogoComDescricao extends Jogo{
    private descricao;  // a propriedade so pode ser acessada dentro da classe, em algum método
    
    constructor(nome: string, descricao: string) {
        super(nome);

        this.descricao = descricao;
    }

    dizerNomeComDescricao() {
        return `O nome do jogo é: ${this.nome} e a descrição é ${this.descricao}`;
    }

}

const ghost = new JogoComDescricao('Ghost of Tsuchima', 'É um jogo very nice');
 */
// Resumo
// public: acessível de forma geral, dentro e fora da classe
// private: é acessível apenas dentro da classe onde o campo foi criado
// protected: acessível apenas dentro da classe (e subclasses) onde o campo foi criado


// interfaces e implements
interface IJogoComDescricao {
    // nome: string;      -> Interface não funciona para propriedade que não sejam publicas
    descricao: string;
    dizerNomeComDescricao(): string;
}

class JogoComDescricao extends Jogo implements IJogoComDescricao{
    public descricao;  // a propriedade so pode ser acessada dentro da classe, em algum método
    
    constructor(nome: string, descricao: string) {
        super(nome);

        this.descricao = descricao;
    }

    dizerNomeComDescricao() {
        return `O nome do jogo é: ${this.nome} e a descrição é ${this.descricao}`;
    }

}

// interface funciona com o mesmo principio do typem mais tomar cuidado caso for redeclarar
// interface é mais voltado para o caso de orientação à objetos 


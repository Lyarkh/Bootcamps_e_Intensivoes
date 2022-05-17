// Exemplo classe
class Matematica {
    soma(valorA, valorB){
        return valorA + valorB;
    }

    subtracao(valorA, valorB) {
        return valorA - valorB;
    }
}

// Criando objeto da classe e usando os métodos da classe
var classeMatematica = new Matematica();

var resultadoSoma = classeMatematica.soma(3, 5);

console.log(resultadoSoma);
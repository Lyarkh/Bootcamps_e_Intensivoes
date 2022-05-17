// Função sem retorno
function olaGama(nome){
    console.log('Olá Gama! Seu nome é ' + nome);
}

// Funções com parâmetros e com retorno
function soma(operadorA, operadorB) {
    var resultadoC = operadorA + operadorB;

    return resultadoC;
}


// Chamada das Funções
olaGama('Lucas');
var resultadoDaSoma = soma(1, 2);
console.log(resultadoDaSoma);
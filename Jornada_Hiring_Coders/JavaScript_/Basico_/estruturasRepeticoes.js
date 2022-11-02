// Estrutura de repetição 'for'

var numeroSorteado = 87;
var tabuada = 7;

for (var i = 0; i <= 10; i++) {
    console.log(tabuada + ' * ' + i + ' =', tabuada * i);
}

for (var i = 0; i < 100; i++) {
    if (numeroSorteado == i){
        console.log('Seu numero foi encontrado. ' +  i);
    }
}

// Estrutura de repetição 'while'

var achou = false;

var numeroSecreto = 15;
var contador = 0;

while (!achou) {

    if (contador == numeroSecreto) {
        console.log('Você achou o número.');
        achou = true;

    } else {
        console.log('O número ' + contador + ' não corresponde ao número secreto.');
    }

    contador += 1;
}
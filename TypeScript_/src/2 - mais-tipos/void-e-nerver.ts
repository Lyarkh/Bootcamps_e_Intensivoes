function principal(): void { // 'void' é utilizado para dizer que a função não tem retorno
    console.log('executando');
}

principal()


// never é usado para:
// laçou ou repetições infinitas
// funções que disparam erros
function funcaoQueNuncaRetorne(): never { // 'never' nunca vai ter um retorno
    throw new Error('ola')
}

funcaoQueNuncaRetorne()
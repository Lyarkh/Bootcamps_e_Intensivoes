const textNaoEstruturado = 'Meu cpf é 123.123.123-45';

const regex = new RegExp('[0-9]{3}.[0-9]{3}.[0-9]{3}-[0-9]{2}');

console.log(textNaoEstruturado.match(regex));
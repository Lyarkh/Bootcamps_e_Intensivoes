
let meuNome = 'Lucas';
let meuSobrenome = 'Emanuel';
let minhaProfissao = 'Back-End Developer';

// Sem template string
console.log('Meu nome é: ' + meuNome + 
    ' ' + meuSobrenome + 
    ', E minha profissão é ' +
    minhaProfissao
);

// Com template string utilizando ``
console.log(`-----------
Meu nome é: ${meuNome} ${meuSobrenome}, 
e minha profissão é: ${minhaProfissao}
-----------`);

console.log(`O resultado de 1 + 1 = ${1 + 1}`);

console.log(`O objeto json ${{chave : 'valor'}}`);

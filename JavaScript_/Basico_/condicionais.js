// Condição if

var nome = 'Edyane';

if (nome == 'Lucas') {
    console.log('Este é seu nome mesmo.');

} else if (nome == 'Edyane') {
    console.log('Oii Edyane');
}
else {
    console.log('Eu não te conheço!');
}

// Condição Switch

nome = 'Carlos';

switch (nome) {
    case 'Lucas':
        console.log('Este é seu nome mesmo.');
        break;

    case 'Edyane':
        console.log('Oii Edyane');
        break;
    
    default:
        console.log('Eu não te conheço!');
        break;

}
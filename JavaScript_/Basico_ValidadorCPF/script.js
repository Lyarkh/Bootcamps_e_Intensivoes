// Verificando se foi carregado corretamento do HTML
console.log('Javascript carregado!');

// Função onde será feita a validação do cpf
function validaCPF(cpf){

    // Verificando a quantidade de numeros do cpf
    if (cpf.length != 11){
        return false;
    } else {

        // Subdividindo a string 'cpf' para validar
        var numerosParaValidacaoPrimeiroDigito = cpf.substring(0, 9);
        var numerosParaValidacaoSegundoDigito = cpf.substring(0, 10);

        // Os dígitos depois do '-' são usados para fazer a validação
        var digitos = cpf.substring(9);

        var somaPrimeiroDigito = 0;
        var somaSegundoDigito = 0;
        
        // Fazendo a soma para cada uma das substrings
        for (var i = 10; i > 1; i--){
            somaPrimeiroDigito += numerosParaValidacaoPrimeiroDigito.charAt(10 - i) * i;
        }

        for (var k = 11; k > 1; k--){
            somaSegundoDigito += numerosParaValidacaoSegundoDigito.charAt(11 - k) * k;
        }

        // Resultado para cada um dos dígitos
        var resultadoPrimeiroDigito = somaPrimeiroDigito % 11 < 2 ? 0 : 11 - (somaPrimeiroDigito % 11);
        var resultadoSegundoDigito = somaSegundoDigito % 11 < 2 ? 0 : 11 - (somaSegundoDigito % 11);

        // Validando os dígitos
        if (resultadoPrimeiroDigito != digitos.charAt(0) ||
        resultadoSegundoDigito != digitos.charAt(1)){
            return false;
        }
        return true;
    }
}

// Função onde pega as informações para validação e envia a resposta para o HTML
function validacao() {
    console.log('Iniciando validação do CPF');

    // Ocultando os blocks para não aparecer na validação seguinte
    document.getElementById('success').style.display = 'none';
    document.getElementById('error').style.display = 'none';

    // Pegando cpf no input HTML
    var cpf = document.getElementById('cpf_digitado').value;
    var resultadoValidacao = validaCPF(cpf);

    // Colocando display: block de acordo com a verificação feita
    if (resultadoValidacao) {
        document.getElementById('success').style.display = 'block';
    } else {
        document.getElementById('error').style.display = 'block';
    }
}
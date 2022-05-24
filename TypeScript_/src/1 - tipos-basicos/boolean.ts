let estaAtivo: boolean;

function mapearStatusUsuario(status: boolean): string {
    if (status){
        return 'Usuário está ativo'
    } else {
        return 'Usuário NÃO  está ativo'
    }

}

mapearStatusUsuario(true);
enum Permissoes {
    admin,          // refenciando como '0'
    editor,         // refenciando como '1'
    comum           // refenciando como '2'
    
}

enum Cores {
    red = '#ff0000',   // referenciando a cor
    black = '#000'
}

const usuario = {
    perfil: Cores.red,
    nivel: Permissoes.admin
}

console.log(usuario)
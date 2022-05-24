const gatos : string[] = [
    'iris', 
    'vlad',
    'diana'
]

function exibeGatos(gatos: string[]){
    return `O nome dos gatos são ${gatos.join(', ')}`
}

exibeGatos(gatos);
let lista = [1, 2, 5];
let listaIncluir = [3, 4];

for (let i = 0; i < listaIncluir.length; i++){
    for (let j = 0; j < lista.length; j++){
        if (lista[j] >= listaIncluir[i]){
            lista.splice(j, 0, listaIncluir[i]);
            j++;
        }
    }
}

const listResult = [1, 2, ...listaIncluir, 5];
console.log(listResult);


let arr = ['a', 'b', 'c'];
// Sem operador spread
// let arr2 = arr;

// com operador spread
let arr2 = [...arr];

arr2.push('d');

console.log(`Arr = ${arr}
Arr2 = ${arr2}`)
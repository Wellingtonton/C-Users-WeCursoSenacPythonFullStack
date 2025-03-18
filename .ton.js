let notas = [];
while (true) {
    let nota = prompt("Insira uma nota (ou digite 'sair' para finalizar):");
    if (nota.toLowerCase() === 'sair') break;
    if (!isNaN(nota) && nota !== "") notas.push(parseFloat(nota));
}
let media = notas.length > 0 ? (notas.reduce((a, b) => a + b) / notas.length).toFixed(2) : 0;
alert("A média das notas é: " + media);
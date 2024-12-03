let Valor1 = 0;
let Valor2 = 0;
let Operacion = "";
function Calcular (Valor1, Valor2, Operacion){
    if (Operacion === "1") {
        return Valor1 + Valor2;
    } else if (Operacion === "2"){
        return Valor1 - Valor2;
    } else if (Operacion === "3"){
        return Valor1 * Valor2;
    } else if (Operacion === "4"){
        if (Valor1 === 0 || Valor2 === 0){
            return "Error: no se puede dividir entre 0"
        }
        return Valor1 / Valor2;
    } else {
        return "Error: Escoja una de las cuatro opciones"
    }
}

let Seguir = true;

while (Seguir){
    Operacion = prompt("Que operación desea realizar?\n 1 = Suma\n 2 = Resta\n 3 = Multiplicación\n 4 = División\n 0 = Salir\n : ");
    Valor1 = parseFloat(prompt("Ingrese un valor: "));
    Valor2 = parseFloat(prompt("Ingrese otro valor: "));
    
    if (Operacion === "0"){
        console.log("Finalizando...");
        break;
    } else {
        let Resultado = Calcular (Valor1, Valor2, Operacion);
        console.log("El resultado es: " + Resultado);
    }
    Continuar = prompt("Desea continuar?\n 1 = Si\n 2 = No\n : ");
    if (Continuar === "1") {
        Seguir = true;
    } else if (Continuar === "2"){
        console.log("Finalizando...")
        break;
    }
}
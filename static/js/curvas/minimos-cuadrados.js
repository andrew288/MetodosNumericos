function generarTabla(){
    let dimension = document.getElementById('puntos').value;
    console.log(dimension);
    let codeHTML="";

    for(let i=0; i<parseInt(dimension); i++){
        codeHTML+='[ <input class="punto" type="number" value=2> , <input class="punto" type="number" value=2> ]';
        codeHTML+="<br>";
    }

    // Ahora agregamos el input
    codeHTML+='<div class="box-botones"><input class="boton" onclick="enviarDatos()" value="Mostrar solución"></div>';

    document.getElementById('matrix').innerHTML=codeHTML;
}

function enviarDatos(){
    let matriz = document.getElementsByClassName('punto');
    let dimension = parseInt(document.getElementById('puntos').value);
    let matrix = []
    let count = 0;
    let solucion;
    let valueHMTL = "";
    console.log(matriz.length);
    for(let i=0; i<dimension; i++){
        let matrixFila = [];
        matrixFila.push(parseFloat(matriz[count].value));
        count++;
        matrixFila.push(parseFloat(matriz[count].value));
        count++;
        matrix.push(matrixFila);
    }
    console.log(matrix);
    console.log(JSON.stringify(matrix))
    fetch('/Ajuste-interpolacion/Minimos_Cuadrados_Ajax',{
        method: 'POST',
        body: JSON.stringify(matrix),
        headers:{
            "Content-type": "application/json; charset=UTF-8",
            "X-CSRFToken": csrftoken,
        }
    }).then(res => res.json())
    .then(data =>{
        console.log(data);
        solucion = JSON.parse(data)
        console.log(solucion)
        valueHMTL+=`<p>Pendiente: ${solucion.m}</p> <br>`;
        valueHMTL+=`<p>Valor de b: ${solucion.b}</p> <br>`;
        valueHMTL+=`<p>Coeficiente de correlación: ${solucion.c}</p> <br>`;
        valueHMTL+=`<P>Función: ${solucion.funcion}</P> <br>`
        document.getElementById('tabla').innerHTML = valueHMTL;
    })
}
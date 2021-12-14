function generarMatriz(){
    let dimension = document.getElementById('dimension').value;
    console.log(dimension);
    let codeHTML="";

    for(let i=0; i<parseInt(dimension); i++){
        for(let j=0; j<parseInt(dimension)+1; j++){
            if(j!=dimension){
                codeHTML+='<input class=" intervalo indice" type="number" value=2> + ';
            }
            else{
                codeHTML+='<input class="intervalo indice" type="number" value=2>';
            }
        }
        codeHTML+="<br>";
    }

    // Ahora agregamos el input
    codeHTML+='<button type="button" onclick="enviarDatos()">Resolver</button>';

    document.getElementById('matrix').innerHTML=codeHTML;
}

function enviarDatos(){
    let matriz = document.getElementsByClassName('indice');
    let dimension = parseInt(document.getElementById('dimension').value);
    let matrix = []
    let count = 0;
    let solucion;
    let valueHMTL = "";
    console.log(matriz.length);
    for(let i=0; i<dimension; i++){
        let matrixFila = [];
        for(let j=0; j<(matriz.length/dimension);j++){
            matrixFila.push(parseInt(matriz[count].value));
            count++;
        }
        matrix.push(matrixFila);
    }
    console.log(matrix);
    console.log(JSON.stringify(matrix))
    fetch('/Ecuaciones-algebraicas/Gauss_Jordan_Ajax',{
        method: 'POST',
        body: JSON.stringify(matrix),
        headers:{
            "Content-type": "application/json; charset=UTF-8",
            "X-CSRFToken": csrftoken,
        }
    }).then(res => res.json())
    .then(data =>{
        solucion = JSON.parse(data)
        console.log(solucion)
        for(let i=0; i< solucion.length;i++){
            valueHMTL+=`<p>x${i}: ${solucion[i]}</p> <br>`;
        }
        document.getElementById('tabla').innerHTML = valueHMTL;
    })
}
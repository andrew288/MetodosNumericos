function generarMatriz(){
    let dimension = document.getElementById('dimension').value;
    console.log(dimension);
    let codeHTML="";

    for(let i=0; i<parseInt(dimension); i++){
        for(let j=0; j<parseInt(dimension)+1; j++){
            if(j==dimension){
                codeHTML+=`<input class="indice" type="number">`;
            }
            else{
                if(j==(parseInt(dimension)-1)){
                    codeHTML+=`<span class="s-variable">x${j}:</span> <input class="indice" type="number"> = `;
                }
                else{
                    codeHTML+=`<span class="s-variable">x${j}:</span> <input class="indice" type="number"> + `;
                }            
            }
        }
        codeHTML+="<br>";
    }

    // Ahora agregamos el input
    codeHTML+='<div class="box-botones"><input class="boton" type="button" onclick="enviarDatos()" value="Mostrar solución"></div>';

    document.getElementById('matrix').innerHTML=codeHTML;
}

function enviarDatos(){
    let matriz = document.getElementsByClassName('indice');
    let dimension = parseInt(document.getElementById('dimension').value);
    let error = document.getElementById('error').value;
    let Decimales = document.getElementById('decimales').value;
    let matrix = []
    let count = 0;
    let solucion;
    let valueHTML = "";
    console.log(matriz.length);
    for(let i=0; i<dimension; i++){
        let matrixFila = [];
        for(let j=0; j<(matriz.length/dimension);j++){
            matrixFila.push(parseFloat(matriz[count].value));
            count++;
        }
        matrix.push(matrixFila);
    }
    console.log(matrix);
    console.log(JSON.stringify(matrix))
    let values ={
        "Matrix":matrix,
        "Error":error
    }
    console.log( JSON.stringify(values))
    fetch('/Ecuaciones-algebraicas/Jacobi_Ajax',{
        method: 'POST',
        body: JSON.stringify(values),
        headers:{
            "Content-type": "application/json; charset=UTF-8",
            "X-CSRFToken": csrftoken,
        }
    }).then(res => res.json())
    .then(data =>{
        console.log(data)
        solucion = JSON.parse(data)
        console.log(solucion)
        //Limitar todos los números a la cantidad de decimales dicha
        for(let i = 0; i < solucion.Variables.length;i++){
            for(let j = 0 ; j< solucion.Variables[i].length;j++){
                solucion.Variables[i][j]=solucion.Variables[i][j].toFixed(Decimales)
                solucion.Errores[i][j] = solucion.Errores[i][j].toFixed(Decimales)
            }
            
        }
        valueHTML+=`<table>`;
        valueHTML+=`<tr>`;
        for(let i=0; i< solucion.Variables[i].length;i++){
            valueHTML+=`<th>x${i+1}</th>`;
        }
        for(let i=0; i< solucion.Variables[i].length;i++){
            valueHTML+=`<th>Error X${i+1}</th>`;
        }
        valueHTML+=`</tr>`;

        for(let  i = 0 ; i< solucion.Variables.length; i++){
            valueHTML+=`<tr>`;
            for(let j = 0 ; j< solucion.Variables[i].length;j++){
                valueHTML+=`<td>${solucion.Variables[i][j]}</td>`;
            }
            for(let j = 0 ; j< solucion.Variables[i].length;j++){
                valueHTML+=`<td>${solucion.Errores[i][j]}</td>`;
            }
            valueHTML+=`</tr>`;
        }
        valueHTML+=`</table>`;
        console.log(valueHTML)
        document.getElementById('tabla').innerHTML = valueHTML;
    })
}
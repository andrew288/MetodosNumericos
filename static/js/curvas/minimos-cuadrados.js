let funcion;
let puntos;

function generarTabla(){
    let dimension = document.getElementById('puntos').value;
    console.log(dimension);
    let codeHTML="";

    for(let i=0; i<parseInt(dimension); i++){
        codeHTML+=`<span class="s-variable">Punto ${(i+1)}: </span> [ <input class="indice" type="number"> , <input class="indice" type="number"> ]`;
        codeHTML+="<br>";
    }

    // Ahora agregamos el input
    codeHTML+='<div class="box-botones"><input class="boton" onclick="enviarDatos()" value="Mostrar solución"></div>';

    document.getElementById('matrix').innerHTML=codeHTML;
}

function enviarDatos(){
    let matriz = document.getElementsByClassName('indice');
    let dimension = parseInt(document.getElementById('puntos').value);
    let matrix = []
    let count = 0;
    let solucion;
    let valueHMTL = "";
    let tablaHTML = "";
    let graficoHTML = "";
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
    puntos = matrix;
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
        funcion = solucion.funcion;
        tablaHTML+=`<table class="table table-striped">
                        <thead class="table-dark">
                            <th>#</th>
                            <th>x</th>
                            <th>y</th>
                            <th>xy</th>
                            <th>x^2</th>
                            <th>y^2</th>
                        </thead>`;
        
        for(let i=0; i<solucion.n; i++){
            tablaHTML+=`<tr>
                <td scope="row">${(i+1)}</td>
                <td>${solucion.puntos[i][0]}</td>
                <td>${solucion.puntos[i][1]}</td>
                <td>${solucion.xy[i]}</td>
                <td>${solucion.x2[i]}</td>
                <td>${solucion.y2[i]}</td>
            </tr>`
        }

        tablaHTML+= `<tr>
            <td>Σ</td>
            <td>${solucion.sx}</td>
            <td>${solucion.sy}</td>
            <td>${solucion.sxy}</td>
            <td>${solucion.sx2}</td>
            <td>${solucion.sy2}</td>
        </tr>`

        tablaHTML+=`</table>`

        // Tabla HTML
        document.getElementById('tabla-solucion').innerHTML = tablaHTML;
        // Resultados

        valueHMTL+=`<p class="p-solucion-ajustes">Pendiente: <span class="s-solucion">${solucion.m}</span></p> <br>`;
        valueHMTL+=`<p class="p-solucion-ajustes">Valor de b: <span class="s-solucion">${solucion.b}</span></p> <br>`;
        valueHMTL+=`<p class="p-solucion-ajustes">Coeficiente de correlación: <span class="s-solucion">${solucion.c}</span></p> <br>`;
        valueHMTL+=`<P class="p-solucion-ajustes">Función: <span class="s-solucion">${solucion.funcion}</span></P> <br>`;
        valueHMTL+=`<button class="boton" onclick="mostrarGrafico()">Mostrar Gráfica</button>`
        document.getElementById('tabla').innerHTML = valueHMTL;

    })
}

function evalInput(strInput) {
    ggbApplet.evalCommand(strInput);
    return false;
  }

function mostrarGrafico(){
    grafica.style.display="block";
    console.log("muestragrafica");
    evalInput(funcion);
    for(let i=0;puntos.length;i++){
        evalInput(`(${puntos[i][0]},${puntos[i][1]})`);
    }
}
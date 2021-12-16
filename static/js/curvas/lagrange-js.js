function generarTabla(){
    let dimension = document.getElementById('puntos').value;
    console.log(dimension);
    let codeHTML="";

    for(let i=0; i<parseInt(dimension); i++){
        codeHTML+=`<span class="s-variable">Punto ${(i+1)}: </span> [ <input class="indice" type="number"> , <input class="indice1" type="number"> ]`;
        codeHTML+="<br>";
    }

    // Ahora agregamos el input
    codeHTML+='<div class="box-botones"><input class="boton" type="button" onclick="enviarDatos()" value="Mostrar solución"></div>';

    document.getElementById('matrix').innerHTML=codeHTML;
}

function enviarDatos(){
    let matriz0 = document.getElementsByClassName('indice');
    let matriz1 = document.getElementsByClassName('indice1');
    let dimension = parseInt(document.getElementById('puntos').value);
    let matriX = []
    let matriY = []
    let solucion;
    let respuestaHMTL = "";
    for(let i=0; i<dimension; i++){
        matriX.push(parseFloat(matriz0[i].value));
        matriY.push(parseFloat(matriz1[i].value));
    }

    console.log(JSON.stringify(matriX))
    fetch('/Ajuste-interpolacion/LagrangeAjax/',{
        method: 'POST',
        body: JSON.stringify({'X': matriX, 'Y': matriY}),
        headers:{
            "Content-type": "application/json; charset=UTF-8",
            "X-CSRFToken": csrftoken,
        }
    }).then(res => res.json())
    .then(data =>{
        console.log(data);
        solucion = data.respuesta
        console.log(solucion)
        respuestaHMTL+=`
            <p> P(x)=${solucion}</p>
        `

        document.getElementById('resultado').innerHTML = respuestaHMTL;
    })
}
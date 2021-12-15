function generarTabla(){
    let dimension = document.getElementById('puntos').value;
    console.log(dimension);
    let codeHTML="";

    for(let i=0; i<parseInt(dimension); i++){
        codeHTML+='[ <input class="punto indice" type="number"> , <input class="punto indice" type="number"> ]';
        codeHTML+="<br>";
    }

    // Ahora agregamos el input
    codeHTML+='<div class="box-botones"><input type="button" class="boton" onclick="enviarDatos()" value="Mostrar solución"></div>';

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
    fetch('/Ajuste-interpolacion/Diferencias_Divididas_Ajax',{
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
        console.log(solucion.data)
        
        valueHMTL+=`<P>Función : </P><br><textarea 
        style="text-align:center; 
            vertical-align: middle;  
            background: #000;
            color: #FFF;
            font-size : 25px;
        " 
        rows="3" cols="100" >P(x) = ${solucion.funcion}</textarea><br>`

        function tableCreate() {
            const body = document.body,
            tbl = document.createElement('table');
            const tr = tbl.insertRow();
            const td = tr.insertCell();
            td.appendChild(document.createTextNode(`Xi`));
            for (let i = 0; i < solucion.n; i++) {
                const td = tr.insertCell();
                td.appendChild(document.createTextNode(`${solucion.xis[i]}`));
            }
           
            it = solucion.n ;
            it2 = 0;
            for (let i = 0; i < solucion.n; i++) {
              const tr = tbl.insertRow();
              for (let j = -1; j <  it; j++) {
                 const td = tr.insertCell();
                  if(i == 0 && j ==-1 ){
                    td.appendChild(document.createTextNode(`Yi`));
                  }else if(j == -1){
                    td.appendChild(document.createTextNode(""));
                  }else{
                    td.appendChild(document.createTextNode(`${solucion.data[it2]}`));
                    it2++;
                  }   
              }
              it--;
            }
            body.appendChild(tbl);
        }
        valueHMTL+=`<P>Solución: </P> <br>`
        tableCreate();
        
       
        document.getElementById('tabla').innerHTML = valueHMTL;
    })
}

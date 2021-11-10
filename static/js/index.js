var select = document.getElementById("seleccionMetodo");
select.addEventListener("change",(event)=>{
    const funcionG = document.getElementById("funcionG");
    const puntoB =  document.getElementById("puntoB");
    const evento = event.target.value;
    if(evento == "biseccion" || evento == "falsaPosicion" ){
        funcionG.disabled = true;
        puntoB.disabled =  false;
    }
    else{
        if(evento == "puntoFijo"){
            funcionG.disabled = false;
            puntoB.disabled =  true;
        }
    }
})

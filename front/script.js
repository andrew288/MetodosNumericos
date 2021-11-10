console.log("ta conectado")
tabla=document.getElementById("grafica")
grafica =document.getElementById("tabla")

function mostrarGrafica(){
    grafica.style.display="block";
    tabla.style.display="none";

}
function mostrarTabla(){
    grafica.style.display="none";
    tabla.style.display="block";
}
//Bisección pero este script debería ser general
tabla=document.getElementById("tabla")
grafica =document.getElementById("grafica")

function mostrarGrafica(){
    grafica.style.display="block";
    tabla.style.display="none";
    console.log("muestragrafica");
}
function mostrarTabla(){
    grafica.style.display="flex";
    tabla.style.display="block";
}
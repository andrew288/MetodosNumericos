let listElements = document.querySelectorAll('.list__button--click');
let navbar = document.getElementById("sidebar");
var cont = 0;
let rayitas = document.getElementById('rayitas');
rayitas.addEventListener('click', ()=>{
    cont++;
    if(cont%2 == 0){
        navbar.classList.toggle('retroceder');
    }
    else{
        navbar.classList.remove("retroceder");
    }
});

listElements.forEach(listElement => {
    listElement.addEventListener('click', ()=>{
        listElement.classList.toggle('arrow');
        
        let height = 0;
        let menu = listElement.nextElementSibling;
        console.log(listElement)
        if(menu.clientHeight == "0"){
            height = menu.scrollHeight;
        }

        menu.style.height = `${height}px`;
        //Code para que se cierren los otros
        let listita0 = listElements[0].nextElementSibling;
        let listita1 = listElements[1].nextElementSibling; 
        let listita2 = listElements[2].nextElementSibling;
        if(listElement == listElements[0]){
            listElements[1].classList.remove('arrow');
            listita1.style.height = `0px`;
            listElements[2].classList.remove('arrow');
            listita2.style.height = `0px`;
        }
        else if(listElement == listElements[1]){
            listElements[0].classList.remove('arrow');
            listita0.style.height = `0px`;
            listElements[2].classList.remove('arrow');
            listita2.style.height = `0px`;
        }
        else{
            listElements[0].classList.remove('arrow');
            listita0.style.height = `0px`;
            listElements[1].classList.remove('arrow');
            listita1.style.height = `0px`;
        }
    })
});


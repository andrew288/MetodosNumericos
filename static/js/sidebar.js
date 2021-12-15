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

        if(menu.clientHeight == "0"){
            height = menu.scrollHeight;
        }

        menu.style.height = `${height}px`;
        //Code para que se cierren los otros
        let listita1 = listElements[1].nextElementSibling;
        let listita2 = listElements[2].nextElementSibling; 
        let listita3 = listElements[3].nextElementSibling;

        if(listElement == listElements[1]){
            listElements[2].classList.remove('arrow');
            listita2.style.height = `0px`;
            listElements[3].classList.remove('arrow');
            listita3.style.height = `0px`;
        }
        else if(listElement == listElements[2]){
            listElements[1].classList.remove('arrow');
            listita1.style.height = '0px';
            listElements[3].classList.remove('arrow');
            listita3.style.height = `0px`;
        }
        else{
            listElements[1].classList.remove('arrow');
            listita1.style.height = '0px';
            listElements[2].classList.remove('arrow');
            listita2.style.height = `0px`;
        }
    })
});


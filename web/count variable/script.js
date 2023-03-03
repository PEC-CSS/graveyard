let btnAdd= document.querySelector('#add');
let btnSubtract= document.querySelector('#subtract');
let input= document.querySelector('input');
btnAdd.addEventListener("keydown", () =>{
    input.value= parseInt(input.value) + 1;
});
btnAdd.addEventListener('keyup', () =>{
    input.value= parseInt(input.value) - 1;
});

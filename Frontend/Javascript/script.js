const button = document.querySelector('.button');
const cover = document.querySelector('.cover');



/****************   EVENTOS *******************/

button.addEventListener('click', function() {
    // Adiciona a classe '.invisible' ao botão quando clicado
    cover.classList.add('invisible');
});
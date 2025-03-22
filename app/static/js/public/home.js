const phrases = [
    "grande sucesso do mercado",
    "negócio que todos comentam",
    "destaque no seu setor",
    "visionário que muda as regras do jogo",
    "nome que ninguém esquece",
    "empreendedor que redefine tendências",
    "fenômeno que inspira milhares",
    "líder de um império global",
    "criador de uma nova categoria de mercado",
    "dono da loja onde todos querem comprar"
];

let index = 0;
const textElement = document.getElementById("changing-text");

function changeText() {
    textElement.classList.add("fade-out");

    setTimeout(() => {
        textElement.innerHTML = phrases[index];
        index = (index + 1) % phrases.length;

        textElement.classList.remove("fade-out");
        textElement.classList.add("fade-in");
    }, 500);
}

setInterval(changeText, 3000);

document.addEventListener("DOMContentLoaded", function () {
    const navbar = document.querySelector(".navbar");

    window.addEventListener("scroll", function () {
        if (window.scrollY > 50) { // Quando rolar mais de 50px
            navbar.classList.add("scrolled");
        } else {
            navbar.classList.remove("scrolled");
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const fadeElements = document.querySelectorAll(".fade-in");

    function fadeInOnScroll() {
        fadeElements.forEach(element => {
            if (element.getBoundingClientRect().top < window.innerHeight * 0.9) {
                element.classList.add("show");
            }
        });
    }

    window.addEventListener("scroll", fadeInOnScroll);
    fadeInOnScroll();
});


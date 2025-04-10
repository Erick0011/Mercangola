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

        setTimeout(() => {
            textElement.classList.remove("fade-in");
        }, 500); // Remove "fade-in" para permitir a próxima animação
    }, 500);
}

setInterval(changeText, 3000);

// Navbar transparente ao rolar
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

// Animação de fade-in ao rolar
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

    document.querySelectorAll('input[name="billing"]').forEach((radio) => {
        radio.addEventListener('change', function () {
            let tipo = this.value; // Pega o tipo selecionado (mensal, semestral ou anual)

            document.querySelectorAll('.pricing-card .price').forEach((priceElement) => {
                let valorMensal = priceElement.getAttribute("data-mensal");

                // Se o plano não tem "data-mensal", significa que é Enterprise e não deve mudar
                if (!valorMensal) return;

                valorMensal = parseInt(valorMensal);

                if (tipo === "semestral") {
                    priceElement.textContent = (valorMensal * 0.75).toLocaleString() + " Kz/mês";
                } else if (tipo === "anual") {
                    priceElement.textContent = (valorMensal * 0.50).toLocaleString() + " Kz/mês";
                } else {
                    priceElement.textContent = valorMensal.toLocaleString() + " Kz/mês";
                }
            });
        });
    });

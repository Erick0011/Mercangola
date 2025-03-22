const phrases = [
    "grande sucesso do mercado",
    "negócio que todos comentam",
    "referência no seu setor",
    "visionário que muda as regras do jogo",
    "nome que ninguém esquece",
    "empreendedor que redefine tendências",
    "fenômeno que inspira milhares",
    "líder de um império global",
    "criador de uma nova categoria de mercado",
    "loja onde todos querem comprar"
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

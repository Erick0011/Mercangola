document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("loginForm");

    // Validação do formulário
    form.addEventListener("submit", function(event) {
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        if (email === "" || password === "") {
            alert("Por favor, preencha todos os campos.");
            event.preventDefault();
        }
    });

    // Mostrar/Ocultar senha
    const togglePassword = document.querySelector(".toggle-password");
    const passwordField = document.getElementById("password");

    togglePassword.addEventListener("click", function() {
        if (passwordField.type === "password") {
            passwordField.type = "text";
            this.innerHTML = '<i class="fas fa-eye-slash"></i>'; // Ícone de ocultar
        } else {
            passwordField.type = "password";
            this.innerHTML = '<i class="fas fa-eye"></i>'; // Ícone de mostrar
        }
    });
});

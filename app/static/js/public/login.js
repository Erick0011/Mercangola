document.addEventListener("DOMContentLoaded", function () {
    const togglePassword = document.querySelector("#togglePassword");
    const passwordField = document.querySelector("#password");

    if (togglePassword && passwordField) {
        togglePassword.addEventListener("click", function () {
            // Alterna o tipo do campo entre 'password' e 'text'
            const type = passwordField.type === "password" ? "text" : "password";
            passwordField.type = type;

            // Alterna o ícone do botão
            this.classList.toggle("fa-eye");
            this.classList.toggle("fa-eye-slash");
        });
    }
});

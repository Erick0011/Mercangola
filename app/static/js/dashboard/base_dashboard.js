        // Sidebar automática
        const sidebar = document.getElementById("sidebar");
        const dropdownContainers = document.querySelectorAll(".dropdown-container");

        sidebar.addEventListener("mouseenter", () => {
            sidebar.classList.remove("collapsed");
            document.querySelector(".main-content").classList.remove("collapsed");
        });

        sidebar.addEventListener("mouseleave", () => {
            sidebar.classList.add("collapsed");
            document.querySelector(".main-content").classList.add("collapsed");

            // Fechar dropdowns ao colapsar a sidebar
            dropdownContainers.forEach(container => container.style.display = "none");
        });

        // Dropdowns personalizados
        let dropdownBtns = document.querySelectorAll(".dropdown-btn");
        dropdownBtns.forEach(btn => {
            btn.addEventListener("click", function () {
                let dropdown = this.nextElementSibling;
                dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
            });
        });

        document.addEventListener("DOMContentLoaded", function () {
            function mostrarSecao(hash) {
                // Oculta todas as seções
                document.querySelectorAll(".content-section").forEach(secao => {
                    secao.style.display = "none";
                });

                // Oculta o dashboard
                document.getElementById("dashboard").style.display = "none";

                // Mostra a seção correspondente ao hash
                if (hash) {
                    let secaoAtiva = document.querySelector(hash);
                    if (secaoAtiva) {
                        secaoAtiva.style.display = "block";
                    }
                } else {
                    // Se não houver hash, exibir o dashboard por padrão
                    document.getElementById("dashboard").style.display = "block";
                }
            }

            // Detectar mudanças no hash da URL
            window.addEventListener("hashchange", function () {
                mostrarSecao(window.location.hash);
            });

            // Inicializar com a seção correta ao carregar a página
            mostrarSecao(window.location.hash);
        });

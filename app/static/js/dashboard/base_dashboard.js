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
        // Definição das cores da paleta
        const mercangolaColors = {
            primary: "#780116",
            secondary: "#D8572A",
            accent: "#FFC107",
            neutral: "#FFFFFF"
        };
            // Gráfico de linha - Faturamento
        new Chart(document.getElementById("faturamentoGrafico"), {
            type: "line",
            data: {
                labels: ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"],
                datasets: [{
                    label: "Faturamento (KZ)",
                    data: [200000, 180000, 250000, 220000, 300000, 350000, 400000],
                    borderColor: mercangolaColors.primary,
                    backgroundColor: "rgba(120, 1, 22, 0.2)",
                    tension: 0.3,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });

        // Gráfico de barras - Pedidos por categoria
        new Chart(document.getElementById("pedidosGrafico"), {
            type: "bar",
            data: {
                labels: ["Eletrônicos", "Roupas", "Alimentos", "Acessórios"],
                datasets: [{
                    label: "Pedidos",
                    data: [50, 80, 40, 70],
                    backgroundColor: [mercangolaColors.primary, mercangolaColors.secondary, mercangolaColors.accent, "#8B0000"]
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });

        // Gráfico de pizza - Distribuição de produtos
        new Chart(document.getElementById("categoriasGrafico"), {
            type: "pie",
            data: {
                labels: ["Smartphones", "Notebooks", "Fones", "Outros"],
                datasets: [{
                    label: "Produtos",
                    data: [40, 30, 20, 10],
                    backgroundColor: [mercangolaColors.primary, mercangolaColors.secondary, mercangolaColors.accent, "#8B0000"]
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });
    // Gráfico de Linha - Crescimento Mensal
    new Chart(document.getElementById("crescimentoGrafico"), {
        type: "line",
        data: {
            labels: ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul", "Ago", "Set", "Out", "Nov", "Dez"],
            datasets: [{
                label: "Crescimento (%)",
                data: [5, 7, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55],
                borderColor: mercangolaColors.secondary,
                backgroundColor: "rgba(216, 87, 42, 0.2)",
                tension: 0.3,
                fill: true
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });

    //Gráfico de Barras - Vendas por Região (Angola)
    new Chart(document.getElementById("regioesGrafico"), {
        type: "bar",
        data: {
            labels: ["Luanda", "Benguela", "Huíla", "Huambo", "Cabinda"],
            datasets: [{
                label: "Vendas (KZ)",
                data: [50000, 30000, 20000, 15000, 10000],
                backgroundColor: [mercangolaColors.primary, mercangolaColors.secondary, mercangolaColors.accent, "#8B0000", "#4BC0C0"]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
        }
    });
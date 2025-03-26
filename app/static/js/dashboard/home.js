
document.addEventListener("DOMContentLoaded", () => {
    fetch("/dashboard/get_data")
        .then(response => response.json())
        .then(data => {
            document.getElementById("faturamentoTotal").innerText = `KZ ${data.faturamento_total}`;
            document.getElementById("pedidosHoje").innerText = data.pedidos_hoje;
            document.getElementById("produtosAtivos").innerText = data.produtos_ativos;

            // Definição das cores
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
                        data: data.grafico_faturamento,
                        borderColor: mercangolaColors.primary,
                        backgroundColor: "rgba(120, 1, 22, 0.2)",
                        tension: 0.3,
                        fill: true
                    }]
                },options: {
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
                        data: data.grafico_pedidos,
                        backgroundColor: [mercangolaColors.primary, mercangolaColors.secondary, mercangolaColors.accent, "#8B0000"]
                    }]
                },options: {
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
                        data: data.grafico_categorias,
                        backgroundColor: [mercangolaColors.primary, mercangolaColors.secondary, mercangolaColors.accent, "#8B0000"]
                    }]
                },options: {
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
                        data: data.grafico_crescimento,
                        borderColor: mercangolaColors.secondary,
                        backgroundColor: "rgba(216, 87, 42, 0.2)",
                        tension: 0.3,
                        fill: true
                    }]
                },options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });

            // Gráfico de Barras - Vendas por Região
            new Chart(document.getElementById("regioesGrafico"), {
                type: "bar",
                data: {
                    labels: ["Luanda", "Benguela", "Huíla", "Huambo", "Cabinda"],
                    datasets: [{
                        label: "Vendas (KZ)",
                        data: data.grafico_regioes,
                        backgroundColor: [mercangolaColors.primary, mercangolaColors.secondary, mercangolaColors.accent, "#8B0000", "#4BC0C0"]
                    }]
                },options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
            // Atualizando a tabela de pedidos
            let tabelaPedidos = document.getElementById("tabela-pedidos");
            tabelaPedidos.innerHTML = "";  // Limpa a tabela antes de adicionar os novos pedidos

            data.pedidos.forEach(pedido => {
                let linha = `
                    <tr>
                        <td>${pedido.id}</td>
                        <td>${pedido.cliente}</td>
                        <td>${pedido.valor}</td>
                        <td><span class="badge ${pedido.status === "Concluído" ? "bg-success" : "bg-warning"}">${pedido.status}</span></td>
                        <td>${pedido.data}</td>
                    </tr>
                `;
                tabelaPedidos.innerHTML += linha;
            });

        })
        .catch(error => console.error("Erro ao carregar os dados:", error));
});

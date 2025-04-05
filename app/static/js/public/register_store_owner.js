<!-- Intl-Tel-Input para selecionar código de país -->
var inputTelefone = document.querySelector("#telefone");
var inputPhone = document.querySelector("#phone");

var itiTelefone = intlTelInput(inputTelefone, {
    initialCountry: "ao",  // Define Angola como padrão
    separateDialCode: true,
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js"
});

var itiPhone = intlTelInput(inputPhone, {
    initialCountry: "ao",
    separateDialCode: true,
    utilsScript: "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js"
});

// Captura o telefone formatado ao submeter o formulário
document.querySelector("form").addEventListener("submit", function() {
    inputTelefone.value = itiTelefone.getNumber();
    inputPhone.value = itiPhone.getNumber();
});

<!-- Leaflet.js para o mapa -->
var map = L.map('map').setView([-8.839988, 13.289437], 12); // Posição inicial em Luanda
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

var marker;
map.on('click', function(e) {
    if (marker) {
        map.removeLayer(marker);
    }
    marker = L.marker(e.latlng).addTo(map);
    document.getElementById("latitude").value = e.latlng.lat;
    document.getElementById("longitude").value = e.latlng.lng;
});

$(document).ready(function() {
    // Carregar os dados de Angola via rota
    $.getJSON('/get-angola_data', function(angolaData) {
        console.log(angolaData);  // Verifique se os dados estão chegando

        // Preencher as províncias de Angola automaticamente
        $('#state').html('<option value="">Selecione uma província</option>');
        angolaData.provincias.forEach(function(provincia) {
            $('#state').append(`<option value="${provincia.nome}">${provincia.nome}</option>`);
        });

        // Quando a província é alterada
        $('#state').change(function() {
            const provinciaSelecionada = $(this).val();
            $('#city').prop('disabled', false).html('<option value="">Selecione um município</option>');

            // Encontrar a província selecionada e preencher os municípios
            const provincia = angolaData.provincias.find(p => p.nome === provinciaSelecionada);
            if (provincia) {
                provincia.municipios.forEach(function(municipio) {
                    $('#city').append(`<option value="${municipio}">${municipio}</option>`);
                });
            }
        });
        // Quando o município é alterado, habilita o campo "Endereço"
        $('#city').change(function() {
            if ($(this).val()) {
                $('#address').prop('disabled', false);
            } else {
                $('#address').prop('disabled', true).val('');
            }
        });

    }).fail(function() {
        alert("Erro ao carregar os dados de Angola.");
    });
});

$(document).ready(function() {
    // Função para gerar o slug
    function generateSlug(text) {
        return text
            .toLowerCase() // converte para minúsculas
            .replace(/[^a-z0-9\s-]/g, '') // remove caracteres especiais
            .replace(/\s+/g, '-') // substitui espaços por hífens
            .replace(/-+/g, '-'); // remove hífens extras
    }

    // Ao digitar no campo de nome da loja
    $('#store_name').on('input', function() {
        const storeName = $(this).val(); // Obtém o nome da loja digitado
        const slug = generateSlug(storeName); // Gera o slug
        $('#slug').val(slug); // Preenche o campo slug com o valor gerado
    });
});
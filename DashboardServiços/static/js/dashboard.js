fetch("/api/clima")
    .then(response => response.json())
    .then(data => {
        document.getElementById("clima-info").innerText =
            `${data.cidade}: ${data.temp}°C - ${data.descricao}`;
    })
    .catch(() => {
        document.getElementById("clima-info").innerText =
            "Erro ao carregar clima";
    });

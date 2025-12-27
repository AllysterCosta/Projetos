// Carregamento de informações de clima
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


//  Função para carregar as taxas de câmbio
async function carregarMoedas() {
    const res = await fetch("/api/moedas");
    const dados = await res.json();

    document.getElementById("usd-brl").innerText = dados.BRL;
    document.getElementById("usd-eur").innerText = dados.EUR;
}
carregarMoedas();

// Carregando notícias
async function carregarNoticias() {
    const res = await fetch("/api/noticias");
    const noticias = await res.json();

    const lista = document.getElementById("lista-noticias");
    lista.innerHTML = "";

    if (noticias.erro) {
        lista.innerHTML = `<li>${noticias.erro}</li>`;
        return;
    }

    noticias.forEach(noticia => {
        const li = document.createElement("li");
        li.innerHTML = `<a href="${noticia.url}" target="_blank">
            ${noticia.titulo} <small>(${noticia.fonte})</small>
        </a>`;
        lista.appendChild(li);
    });
}

carregarNoticias();

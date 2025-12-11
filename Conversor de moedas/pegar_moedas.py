import xmltodict


def nomes_moedas():

    with open("Conversor de moedas/moedas.xml", "rb") as arquivo_moedas:
        dic_moedas = xmltodict.parse(arquivo_moedas)

    moedas = dic_moedas["xml"]
    return moedas


def obter_conversoes():
    with open("Conversor de moedas/conversoes.xml", "rb") as arquivo_conversoes:
        dic_conversoes = xmltodict.parse(arquivo_conversoes)

    conversoes = dic_conversoes["xml"]
    dict_conversoes_disponiveis = {}
    for par_conversao in conversoes:
        moeda_origem, moeda_destino = par_conversao.split("-")
        if moeda_origem in dict_conversoes_disponiveis:
            dict_conversoes_disponiveis[moeda_origem].append(moeda_destino)
        else:
            dict_conversoes_disponiveis[moeda_origem] = [moeda_destino]
    return dict_conversoes_disponiveis

# O conversor de moedas é um projeto que trará uma janela onde o usuário poderá realizar a conversão entre uma moeda de origem para uma moeda de destino com base na cotação atual
# Será uma janela de 500x500 pixels
# Com titulo
# Campos de seleção de moeda de origem e destino (campos de listas)
# Botão de conversão
# Lista de exibição com uma lista de moedas

import customtkinter as ctk
from pegar_moedas import nomes_moedas, obter_conversoes

# Criar e configurar a janela principal
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()
janela.geometry("500x500")

dict_conversoes_disponiveis = obter_conversoes()

# Criar os botões, textos e outros elementos da interface
titulo = ctk.CTkLabel(janela, text="Conversor de Moedas", font=("", 20))
texto_moeda_origem = ctk.CTkLabel(janela, text="Selecione moeda de Origem")
texto_moeda_destino = ctk.CTkLabel(janela, text="Selecione moeda de Destino")


def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dict_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_destino.configure(values=lista_moedas_destino)
    campo_moeda_destino.set(lista_moedas_destino[0])


campo_moeda_origem = ctk.CTkOptionMenu(
    janela, values=list(dict_conversoes_disponiveis.keys()), command=carregar_moedas_destino)
campo_moeda_destino = ctk.CTkOptionMenu(
    janela, values=["Selecione uma moeda de origem"])


def converter_moeda():
    print("converter moeda")


botao_converter = ctk.CTkButton(
    janela, text="Converter", command=converter_moeda)

lista_de_moedas = ctk.CTkScrollableFrame(janela)

moedas_disponiveis = nomes_moedas()
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = ctk.CTkLabel(
        lista_de_moedas, text=f"{codigo_moeda}: {nome_moeda}")
    texto_moeda.pack()

# Criar todos os elementos da interface gráfica
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10)
texto_moeda_destino.pack(padx=10, pady=3)
campo_moeda_destino.pack(padx=10)
botao_converter.pack(padx=10, pady=10)
lista_de_moedas.pack(padx=10, pady=10, fill="both", expand=True)

# Rodas a janela
janela.mainloop()

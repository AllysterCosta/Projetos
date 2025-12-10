# O conversor de moedas é um projeto que trará uma janela onde o usuário poderá realizar a conversão entre uma moeda de origem para uma moeda de destino com base na cotação atual
# Será uma janela de 500x500 pixels
# Com titulo
# Campos de seleção de moeda de origem e destino (campos de listas)
# Botão de conversão
# Lista de exibição com uma lista de moedas

import customtkinter as ctk

# Criar e configurar a janela principal
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

janela = ctk.CTk()
janela.geometry("500x500")

# Criar os botões, textos e outros elementos da interface
titulo = ctk.CTkLabel(janela, text="Conversor de Moedas")
texto_moeda_origem = ctk.CTkLabel(janela, text="Selecione moeda de Origem")
texto_moeda_destino = ctk.CTkLabel(janela, text="Selecione moeda de Destino")

campo_moeda_origem = ctk.CTkOptionMenu(
    janela, values=["USD", "EUR", "BRL", "JPY", "GBP", "BTC"])
campo_moeda_destino = ctk.CTkOptionMenu(
    janela, values=["USD", "EUR", "BRL", "JPY", "GBP", "BTC"])


def converter_moeda():
    print("converter moeda")


botao_converter = ctk.CTkButton(
    janela, text="Converter", command=converter_moeda)

lista_de_moedas = ctk.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD - Dólar Americano",
                      "EUR - Euro",
                      "BRL - Real Brasileiro",
                      "JPY - Iene Japonês",
                      "GBP - Libra Esterlina",
                      "BTC - Bitcoin"]
for moeda in moedas_disponiveis:
    texto_moeda = ctk.CTkLabel(lista_de_moedas, text=moeda)
    texto_moeda.pack()

# Criar todos os elementos da interface gráfica
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=10)
campo_moeda_origem.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx=10, pady=10)
campo_moeda_destino.pack(padx=10, pady=10)
botao_converter.pack(padx=10, pady=10)
lista_de_moedas.pack(padx=10, pady=10, fill="both", expand=True)

# Rodas a janela
janela.mainloop()

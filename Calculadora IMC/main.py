# Calculadora de IMC usando Tkinter

import tkinter as tk

# Função para calcular o IMC
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get()) / 100  # Convertendo cm para metros
        imc = peso / (altura ** 2)
        label_resultado.config(text=f"Seu IMC é: {imc:.2f}")
    except ValueError:
        label_resultado.config(text="Por favor, insira valores válidos.")


# Criando a janela principal
window = tk.Tk()
window.title("Calculadora de IMC")
window.geometry("300x200")
window.resizable(False, False)
window.configure(bg="#f0f0f0")

# Criando os elementos da interface
label_peso = tk.Label(window, text="Peso (kg):", bg="#f0f0f0")
label_peso.pack(pady=(20, 5))
entry_peso = tk.Entry(window)
entry_peso.pack(pady=5)
label_altura = tk.Label(window, text="Altura (cm):", bg="#f0f0f0")
label_altura.pack(pady=5)
entry_altura = tk.Entry(window)
entry_altura.pack(pady=5)
button_calcular = tk.Button(window, text="Calcular IMC", command=calcular_imc)
button_calcular.pack(pady=10)
label_resultado = tk.Label(window, text="", bg="#f0f0f0")
label_resultado.pack(pady=5)
# Iniciando o loop principal da interface
window.mainloop()

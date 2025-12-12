# Importando bicliotecas necessárias
import customtkinter as ctk
from agenda import adicionar_contato, buscar_contatos, salvar_agenda

# Inicializando personalização do tema da interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
windowAgenda = ctk.CTk()
windowAgenda.geometry("510x500")
windowAgenda.title("Agenda de Contatos")


# =======================
#   FRAME ESQUERDO
# =======================

# Função para atualizar a lista de contatos após adicionar um novo contato

def salvar_contato():
    nome = campo_nome.get().strip()
    telefone = campo_telefone.get().strip()
    email = campo_email.get().strip()

    if nome == "":
        mensagem_status.configure(
            text="Digite um nome válido!", text_color="red")
        return
    if telefone == "":
        mensagem_status.configure(
            text="Digite um telefone válido!", text_color="red")
        return
    if email == "":
        mensagem_status.configure(
            text="Digite um email válido!", text_color="red")
        return
    adicionar_contato(nome, telefone, email)

    mensagem_status.configure(
        text="Contato salvo com sucesso!", text_color="lightgreen")

    campo_nome.delete(0, "end")
    campo_telefone.delete(0, "end")
    campo_email.delete(0, "end")

    atualizar_lista_contatos()


# Criar os botões, textos e outros elementos da interface
frame_campos = ctk.CTkFrame(windowAgenda, width=550, height=490)
frame_campos.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

titulo = ctk.CTkLabel(frame_campos, text="Agenda de Contatos", font=("", 20))
texto_nome = ctk.CTkLabel(frame_campos, text="Nome do Contato")
campo_nome = ctk.CTkEntry(
    frame_campos, placeholder_text="Digite o nome do contato")
texto_telefone = ctk.CTkLabel(frame_campos, text="Telefone do Contato")
campo_telefone = ctk.CTkEntry(
    frame_campos, placeholder_text="Digite o telefone do contato")
texto_email = ctk.CTkLabel(frame_campos, text="Email do Contato")
campo_email = ctk.CTkEntry(
    frame_campos, placeholder_text="Digite o email do contato")
botao_salvar = ctk.CTkButton(
    frame_campos, text="Salvar Contato", command=salvar_contato)
mensagem_status = ctk.CTkLabel(frame_campos, text="", text_color="lightgreen")
mensagem_status.pack(pady=5)


# Criar todos os elementos da interface gráfica
titulo.pack(padx=10, pady=10)
texto_nome.pack(padx=10, pady=1)
campo_nome.pack(padx=10, pady=5)
texto_telefone.pack(padx=10, pady=1)
campo_telefone.pack(padx=10, pady=5)
texto_email.pack(padx=10, pady=1)
campo_email.pack(padx=10, pady=5)
botao_salvar.pack(padx=10, pady=50)


# =======================
#   FRAME DIREITO
# =======================
# Criar os botões, textos e outros elementos da interface
frame_contatos = ctk.CTkFrame(windowAgenda, width=250, height=460)
frame_contatos.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")

lista_contatos_titulo = ctk.CTkLabel(
    frame_contatos, text="Contatos Salvos", font=("", 20))
lista_contatos = ctk.CTkScrollableFrame(frame_contatos, width=220, height=400)


def confirmar_exclusao(nome, popup):
    contatos = buscar_contatos()
    contatos = [c for c in contatos if c["nome"] != nome]
    agenda_dict = {
        c["nome"]: {"telefone": c["telefone"], "email": c["email"]} for c in contatos
    }
    salvar_agenda(agenda_dict)
    popup.destroy()
    atualizar_lista_contatos()


def excluir_contato(nome):
    popup = ctk.CTkToplevel(windowAgenda)
    popup.title("Confirmar Exclusão")
    popup.geometry("300x150")
    popup.grab_set()

    label_confirmacao = ctk.CTkLabel(popup, text=f"Excluir contato {nome}?")
    label_confirmacao.pack(pady=20)

    frame_botoes = ctk.CTkFrame(popup)
    frame_botoes.pack(pady=10)

    botao_sim = ctk.CTkButton(frame_botoes, text="Sim", width=80,
                              command=lambda: confirmar_exclusao(nome, popup))
    botao_sim.pack(side="left", padx=10)
    botao_nao = ctk.CTkButton(frame_botoes, text="Não",
                              width=80, command=popup.destroy)
    botao_nao.pack(side="right", padx=10)


def atualizar_lista_contatos():
    for widget in lista_contatos.winfo_children():
        widget.destroy()

    contatos = buscar_contatos()
    # lista_contatos.delete("1.0", ctk.END)

    for contato in contatos:
        nome = contato['nome']
        telefone = contato["telefone"]
        email = contato["email"]
        item_lista_frame = ctk.CTkFrame(lista_contatos)
        item_lista_frame.pack(padx=5, pady=5, fill="x")

        label_contato_lista = ctk.CTkLabel(item_lista_frame,
                                           text=f'{nome} | {telefone} | {email}',
                                           anchor="w")
        label_contato_lista.pack(padx=5, pady=5, fill="x")
        botao_excluir_contato = ctk.CTkButton(item_lista_frame, text="Excluir", width=60,
                                              fg_color="red", hover_color="#ff4d4d", command=lambda n=nome: excluir_contato(n))
        botao_excluir_contato.pack(padx=5, pady=5, side="right")
        # lista_contatos.insert(
        #     ctk.END, f"Nome: {contato[0]}\nTelefone: {contato[1]}\nEmail: {contato[2]}\n\n"
        # )
    if not contatos:
        lista_contatos.insert(ctk.END, "Nenhum contato na agenda.\n")
        return


# Criar todos os elementos da interface gráfica
lista_contatos_titulo.pack(padx=10, pady=10)
lista_contatos.pack(padx=10, pady=5)

# Atualizar a lista de contatos ao iniciar o programa
atualizar_lista_contatos()

# Rodas a janela
windowAgenda.mainloop()

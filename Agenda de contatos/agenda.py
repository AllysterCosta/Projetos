# Agenda de Contatos em Python
import json
arquivo_agenda = 'agenda_contatos.json'


def carregar_agenda():
    try:
        with open(arquivo_agenda, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}


def salvar_agenda(agenda):
    with open(arquivo_agenda, 'w') as arquivo:
        json.dump(agenda, arquivo, indent=4)


def adicionar_contato(nome, telefone, email):
    agenda = carregar_agenda()
    agenda[nome] = {'telefone': telefone, 'email': email}
    salvar_agenda(agenda)

# A busca de contatos retornará uma lista de dicionários


def buscar_contatos():
    agenda = carregar_agenda()
    lista_contatos = []
    for nome, info in agenda.items():
        lista_contatos.append({"nome": nome,
                               "telefone": info['telefone'],
                               "email": info['email']})
    return lista_contatos

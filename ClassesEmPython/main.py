# Criando classe de Cliente em Python

class Cliente:
    def __init__(self, nome, email, plano):
        self.nome = nome
        self.email = email
        self.planos = ["basic", "premium"]
        if plano in self.planos:
            self.plano = plano
        else:
            raise Exception("Plano inválido")

    def mudar_plano(self, novo_plano):
        if novo_plano in self.planos:
            print(f"Mudando plano de {self.plano} para {novo_plano}")
            self.plano = novo_plano
        else:
            raise Exception("Plano inválido")


# Instanciando um objeto Cliente
cliente = Cliente("Ana Silva", "ana@email.com", "premium")
print(cliente.nome)  # Saída: Ana Silva
print(cliente.plano)  # Saída: premium
cliente.mudar_plano("basic")  # Mudando plano de premium para basic
print(cliente.plano)  # Saída: basic

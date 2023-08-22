class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de {valor} realizado. Saldo atual: {self.saldo}"
        else:
            return "Valor de depósito inválido."

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de {valor} realizado. Saldo atual: {self.saldo}"
        else:
            return "Saldo insuficiente ou valor de saque inválido."

    def extrato(self):
        return f"Saldo atual: {self.saldo}"

class Banco:
    def __init__(self):
        self.clientes = {}

    def cadastrar_cliente(self, nome, cpf):
        if cpf not in self.clientes:
            self.clientes[cpf] = {"nome": nome, "conta": None}
            return f"Cliente {nome} cadastrado com sucesso."
        else:
            return "CPF já cadastrado."

    def cadastrar_conta_bancaria(self, cpf, conta):
        if cpf in self.clientes:
            self.clientes[cpf]["conta"] = conta
            return f"Conta bancária cadastrada para o cliente {self.clientes[cpf]['nome']}."
        else:
            return "CPF não cadastrado."

def main():
    banco = Banco()

    while True:
        print("\nEscolha uma opção:")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Conta Bancária")
        print("3. Depositar")
        print("4. Sacar")
        print("5. Extrato")
        print("6. Sair")

        escolha = int(input("Opção: "))

        if escolha == 1:
            nome = input("Digite o nome do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            print(banco.cadastrar_cliente(nome, cpf))
        elif escolha == 2:
            cpf = input("Digite o CPF do cliente: ")
            conta = ContaBancaria()
            print(banco.cadastrar_conta_bancaria(cpf, conta))
        elif escolha == 3:
            cpf = input("Digite o CPF do cliente: ")
            valor = float(input("Digite o valor para depósito: "))
            print(banco.clientes[cpf]["conta"].depositar(valor))
        elif escolha == 4:
            cpf = input("Digite o CPF do cliente: ")
            valor = float(input("Digite o valor para saque: "))
            print(banco.clientes[cpf]["conta"].sacar(valor))
        elif escolha == 5:
            cpf = input("Digite o CPF do cliente: ")
            print(banco.clientes[cpf]["conta"].extrato())
        elif escolha == 6:
            print("Saindo do sistema.")
            break
        else:
            print("Opção inválida. Escolha novamente.")


if __name__ == "__main__":
    main()

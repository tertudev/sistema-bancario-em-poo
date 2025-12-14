from datetime import datetime


# ================== CLIENTE ==================
class Cliente:
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco
        self.conta = None

    def criar_conta(self, numero):
        self.conta = ContaCorrente(numero, self)
        return self.conta


# ================== CONTA ==================
class Conta:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.historico = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.registrar_transacao("Depósito", valor)
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido!")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido!")
        elif valor > self.saldo:
            print("Saldo insuficiente!")
        else:
            self.saldo -= valor
            self.registrar_transacao("Saque", valor)
            print("Saque realizado com sucesso!")

    def registrar_transacao(self, tipo, valor):
        self.historico.append({
            "tipo": tipo,
            "valor": valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M")
        })

    def extrato(self):
        print("\n===== EXTRATO =====")
        if not self.historico:
            print("Nenhuma movimentação.")
        else:
            for t in self.historico:
                print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("===================")


# ================== CONTA CORRENTE ==================
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500):
        super().__init__(numero, cliente)
        self.limite = limite

    def sacar(self, valor):
        if valor > self.limite:
            print("Valor excede o limite de saque!")
        else:
            super().sacar(valor)


# ================== SISTEMA ==================
class Banco:
    def __init__(self):
        self.clientes = []
        self.contas = []

    def criar_cliente(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        endereco = input("Endereço: ")

        if self.buscar_cliente(cpf):
            print("Cliente já existe!")
            return

        cliente = Cliente(nome, cpf, endereco)
        self.clientes.append(cliente)
        print("Cliente criado com sucesso!")

    def criar_conta(self):
        cpf = input("CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)

        if not cliente:
            print("Cliente não encontrado!")
            return

        numero = len(self.contas) + 1
        conta = cliente.criar_conta(numero)
        self.contas.append(conta)
        print("Conta criada com sucesso!")

    def buscar_cliente(self, cpf):
        for cliente in self.clientes:
            if cliente.cpf == cpf:
                return cliente
        return None

    def operar_conta(self):
        cpf = input("CPF do cliente: ")
        cliente = self.buscar_cliente(cpf)

        if not cliente or not cliente.conta:
            print("Cliente ou conta não encontrada!")
            return

        conta = cliente.conta

        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        opcao = input("Escolha: ")

        if opcao == "1":
            valor = float(input("Valor: "))
            conta.depositar(valor)

        elif opcao == "2":
            valor = float(input("Valor: "))
            conta.sacar(valor)

        elif opcao == "3":
            conta.extrato()

        else:
            print("Opção inválida!")


# ================== MAIN ==================
def main():
    banco = Banco()

    while True:
        print("\n===== MENU =====")
        print("[1] Criar cliente")
        print("[2] Criar conta")
        print("[3] Operar conta")
        print("[0] Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            banco.criar_cliente()

        elif opcao == "2":
            banco.criar_conta()

        elif opcao == "3":
            banco.operar_conta()

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


main()

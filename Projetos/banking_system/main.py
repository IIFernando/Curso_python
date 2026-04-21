class BankAccount:

    def __init__(self):
        self.saldo = 0

    def deposito(self, saldo):
        self.saldo += saldo

    def saque(self, saldo):
        self.saldo -= saldo

    def mostrar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")

# Instânciado a classe, sempre tomar cuidado onde ela for instanciada.
conta = BankAccount()

system = True
while system:
    print("\n===== MENU =====")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Saldo")
    print("0 - Sair")
    print("================\n")

    opcao = input("Escolha a operação: ")

    match opcao:

        case "1":
            print("Depositar")
            valor = float(input("Informe o valor R$: "))
            saldo = conta.deposito(valor)

        case "2":
            print("Sacar")
            valor = float(input("Informe o valor R$: "))
            saldo = conta.saque(valor)

        case "3":
            print("Extrato")
            conta.mostrar_saldo()

        case "0":
            print("Atendimento encerrado.")
            system = False


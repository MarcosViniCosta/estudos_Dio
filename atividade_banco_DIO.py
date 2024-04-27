import textwrap
from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_de_nasc, endereco):
        super().__init__(endereco)
        self._cpf = cpf
        self._nome = nome
        self.data_de_nasc = data_de_nasc


class Conta(Cliente):
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._Cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return (numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def _agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        if valor > saldo:
            self._saldo -= valor
            print('------Saldo insuficiente! Operação falhou------')
        elif valor > 0:
            print('\n-------Saque realizado com sucesso!-------')
            return True
        else:
            print("Falha\nValor informado não é valido")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('---Deposito realizado com sucesso!---')
            return True
        else:
            print("---Falha na operação\nValor de depósito não é valido---")
            return False


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.
                            transacoes if transacao["tipo"] == Saque.__name__]
                            )

        if numero_saques > self._limite_saques:
            print('FALHA\nLIMITE DIARIO DE SAQUES EXCEDIDO')
        elif valor > self._limite:
            print('FALHA\nVALOR SUPERIOR AO PERMITIDO PARA SAQUE')
        else:
            print('----OPERAÇÃO REALIZADA COM SUCESSO----')
            print(f'\n------SAQUE : R${valor:.2f}---------')
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
            Agencia:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    def adicionar_transação(self, transacao):
        self._transacoes.append({
            'tipo': transacao.__class__.__name__,
            'valor': transacao.valor,
            'data': datetime.now().strftime("%d-%m-%Y %H:%M:%s")

        })


class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)



def menu():
    menu = """\n
    ____________________________MENU______________________________
    
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    ==>
    """
    return input(textwrap.dedent(menu))



def filtrar_clientes(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente ainda não possui conta")
        return

    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)

    if not cliente:
        print("\n------ Cliente não encontrado! ---------\n")
        return
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print("\n------ Cliente não encontrado! ---------\n")
        return
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_clientes(cpf,clientes)

    if not cliente:
        print("\n------ Cliente não encontrado! ---------\n")
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("-----------------EXTRATO----------------------")
    transacoes = conta.historico._transacoes
    extrato = ""
    if not transacoes:
        extrato = "Nenhuma movimentação localizada"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}: \t R$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\t R${conta.saldo:.2f}")
    print("---------------------------------------------")




def criar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa)")
        endereco = input("Informe o endereço residencial (rua, numero, bairro, cidade/sigla")
        clientes.append(cliente)
        print("\n\n\tCliente cadastrado com sucesso")
    else:
        print("CPF ENCONTRADO EM NOSSA BASE DE DADOS")
        return
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o cpf do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)
    if not cliente:
        print("\n------ Cliente não encontrado! ---------\n")
        return
    conta = ContaCorrente.nova_conta(cliente=cliente,numero=numero_conta)
    contas.append(conta)
    cliente.conta.append(conta)
    print("\n\nConta criada com sucesso!")

def listar_contas(contas):
    for conta in contas:
        print("="*100)
        print(textwrap.dedent(str(conta)))




def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("OPERAÇÃO SELECIONADA NÃO É VALIDA\n\nESCOLHA NOVAMENTE A OPERACAO QUE DESEJA")



main()
import textwrap

saldo = 0
limite = 500
user_list = []
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
accounts_list = []

def users_filter(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def create_user(user_list):
    cpf = input('Informe o CPF do usuário (somente os números): ')
    usuario = users_filter(cpf,user_list)

    if usuario:
        print("\n\n USUÁRIO JÁ CADASTRADO \n\n")
        return

    nome = input('Informe o nome do usuário: ')
    data_de_nasc = input('Informe a data de nascimento: ')
    address = input('Informe o endereço (logradouro - bairro - cidade/sigla estado): ')
    user_list.append({'nome':nome,'data_de_nasc':data_de_nasc, 'cpf':cpf, 'endereco': address})
    print('\n\n USUARIO CRIADO COM SUCESSO!! \n\n')
def create_account(users_list, accounts):
    AGENCY_NUMBER = '0001'
    account_number = len(accounts) + 1
    cpf = input('Informe o cpf vinculado a conta: ')
    usuario = users_filter(cpf, users_list)

    if usuario:
        print('\n\n CONTA CRIADA COM SUCESSO!! \n\n')
        return accounts.append({'agency_number': AGENCY_NUMBER, 'account_number': account_number, 'usuario':usuario})

    print('USUARIO NÃO ENCONTRADO\nNÃO FOI POSSIVEL CRIAR A CONTA\n\n')

def deposit(deposito,saldo,extrato,/):
    if deposito > 0:
        saldo += deposito
        extrato += f'Deposito: R${deposito:.2f}\nSaldo: R${saldo:.2f}\n'
    else:
        print("Valor inválido para depósito")
    return saldo,extrato

def saque_conta(*,saque,saldo,extrato, numero_saques):

    if saque > 500:
        print("Valor superior ao limite de saque")
    elif saldo < saque:
        print("Valor do saldo indisponivel")
    elif saque <= 0:
        print("Operação inválida")
    else:
        saldo -= saque
        numero_saques += 1
        extrato += f'Saque: R${saque:.2f}\nSaldo: R${saldo:.2f}\n'

    return saldo, extrato


def mostrar_extrato(saldo, extrato=extrato):
    print('\nExtrato')
    print(extrato)
    print(f"\n\n\nSaldo atualizado: R${saldo:.2f}")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Agência:\t{conta['agency_number']}
        C/C\t\t{conta['account_number']}
        Titular:\t{conta['usuario']['nome']}
"""
        print("="*100)
        print(textwrap.dedent(linha))
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[cu] criar usuarios
[cc] criar conta
[contas] contas

=> """
while True:
    opcao = input(menu)

    if opcao == 'd':
        print('\nDeposito')
        deposito = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposit(deposito,saldo,extrato)
    elif opcao == 's':
        if LIMITE_SAQUES > numero_saques:
            print('\nSaque')
            saque = float(input("Informe o valor do saque: "))
            saldo, extrato = saque_conta(saque,saldo,extrato,numero_saques)
        else:
            print("LIMITE DE SAQUES DIARIOS ATINGIDO")
    elif opcao == 'e':
        mostrar_extrato(saldo,extrato)
    elif opcao == 'cu':
        create_user(user_list)
    elif opcao == 'cc':
        create_account(user_list,accounts_list)
    elif opcao == 'contas':
        listar_contas(accounts_list)
    elif opcao == 'q':
        break
    else:
        print('Opção inválida')

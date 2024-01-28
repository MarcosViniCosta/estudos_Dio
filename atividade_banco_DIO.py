menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500

extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print('\nDeposito')
        deposito = float(input("Informe o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            extrato += f'Deposito: R${deposito:.2f}\nSaldo: R${saldo:.2f}\n'
        else:
            print("Valor inválido para depósito")
    elif opcao == 's':
        if LIMITE_SAQUES > numero_saques:
            print('\nSaque')
            saque = float(input("Informe o valor do saque: "))
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
        else:
            print("LIMITE DE SAQUES DIARIOS ATINGIDO")
    elif opcao == 'e':
        print('\nExtrato')
        print(extrato)
        print(f"\n\n\nSaldo atualizado: R${saldo:.2f}")
    elif opcao == 'q':
        break
    else:
        print('Opção inválida')

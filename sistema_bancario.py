saldo = 0
limite_por_saque = 500
extrato = """

"""
numero_saques = 0
LIMITE_SAQUES = 3



menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato 
[s] - Sair

"""

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor_deposito = float(input("Informe o valor do depósito: "))
        print()

        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito:.2f}"
            print("Depósito realizado com sucesso!\nSelecione a próxima operação.")
        else:
            print("Operação falhou! O valor informado é inválido.")
            
    
    elif opcao == "s":
        valor_saque = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor_saque > saldo 
        excedeu_limite = valor_saque > limite_por_saque
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! Limite insuficiente.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        
        elif valor_saque > 0:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"Saque: R$ {valor_saque:.2f}"
            print("Saque realizado com sucesso!\nSelecione a próxima operação.")
            
        
        else: 
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "e":
        print("\n============= EXTRATO =============") 
        print("Não foram realizadas movimentações." if not extrato else extrato)  
        print(f"Saldo: R$ {saldo:.2f}")  
        print("\n===================================")  
        
    elif opcao == "s":
        break
    
    else: 
        print("Operação inválida, por favor selecione uma opção válida!")
        
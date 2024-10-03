menu = """

=========  MENU =========

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair do menu

=========================
"""

saldo = 0
limite = 500
extrato = ""
LIMITE_SAQUES = 3
contador_saque = 1

### Criando LOOP para acessar MENU.
while True:

    opcao = input(menu)
    
    ### Verificação para opção 1 = Depositar.
    if opcao == "1":
       deposito = float(input("Qual valor deseja depositar? : "))
       if deposito > 0 :
            saldo += deposito # Adiciona depósito no saldo.
            extrato += f'Depósito: R$ {deposito:.2f}\n'# Adiciona depósito no histórico do extrato.
            print("Depósito realizado com sucesso!")
    
    # Verificação para opção 2 = Saque.
    elif opcao == "2":
       if contador_saque > LIMITE_SAQUES: # Verifica se o número de operações de saque excedeu o limite de saque.
            print("Você excedeu o número de saques diários.")
       else:
           saque = float(input("Qual valor deseja sacar?: "))
           
           if saque > 0 and saque <= saldo and saque <= limite: # Verifica se cumprir todos os requisitos para saque.
               saldo -= saque
               contador_saque += 1
               extrato += f'Saque: R$ {saque:.2f}\n'
               print ("Saque realizado com sucesso!")
           
           elif saque > limite: # Caso não passe na verificação acima, verifica se o valor excede o limite para saque.
               print("Valor acima do permitido para saque!") 
           else: 
               print("Não possui saldo suficiente!")
    
    # Verifição para opção 3 = Extrato.
    elif opcao == "3":
        if extrato == "": # Verifca se o Extrato está vazio.
            print(f'======== EXTRATO ======== \nSaldo:R$ {saldo:.2f}\n\nNão houve movimentações!\n=========================')
        else:
            print(f'======== EXTRATO ======== \nSaldo:R$ {saldo:.2f}\n\n{extrato}\n=========================')  
   
    elif opcao =="4":
        print("Saindo do menu...")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a opção desejada no menu.")
               
               
          


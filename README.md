# 🏆 Desafio Sistema Bancário - Versão 01

Nesse desafio o objetivo era criar um sistema bancário onde deveria haver 4 opções de operações: Depósito, Saque, Extrato e Sair do Menu.
Além disso esse sistema deveria ter limite de saques diários igual a 3 e o limite de valor desses saque não deveria ultrapassar R$ 500,00.


## 🛠 Ferramentas e Linguagens Utilizadas

![Vscode](https://img.shields.io/badge/Vscode-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)



## 💻 Trecho do Código

```python
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
```


## 📌 Funcionalidades

- Sistema Bancário para Depositar, Sacar, Visualizar Extrato.



## 📖 Documentação

[Documentação Python](https://docs.python.org/pt-br/3/tutorial/controlflow.html)

[Bootcamp DIO](https://web.dio.me/project/desafio-de-projeto-criando-um-sistema-bancario/learning/fa812356-0da6-4a85-9ffb-8b255748a288?back=/track/engenharia-dados-python&tab=undefined&moduleId=undefined)


## 👩‍💻 Autora

- [@laryssabueno](https://www.github.com/laryssabueno)

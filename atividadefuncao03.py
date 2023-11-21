# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.

def bagulho():
    salario = float(input("Digite o seu salário: R$"))
    aumento = salario * 0.15
    novosalario = salario + aumento
    print(f"Seu novo salário é: R${novosalario}")

bagulho()
#ex037
#Escreve um programa que leia um número inteiro qualuqer e peça para o usuário escolher qual será a base de conversao
import math

n1 = int(input("Digite um numero inteiro: "))
print("Vocé digitou {}, agora vamos decidir a conversão.".format(n1))

choice = int(input("Digite um numero de 1 a 3: "))

if choice == 1:
    binario = bin(n1)
    print("O valor {} em binário fica {}!".format(n1, binario))
elif choice == 2:
    octal = oct(n1)
    print("O valor {} em octal fica {}!".format(n1, octal))
elif choice == 3:
    hexa = hex(n1)
    print("O valor {} em hexadecimal fica {}!".format(n1, hexa))
else:
    print("Você digitou um valor que não era 1, 2 ou 3!\nTente novamente!!")
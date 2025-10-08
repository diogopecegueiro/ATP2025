def menu():
    print("""
(1) Criar Lista 
(2) Ler Lista
(3) Soma
(4) Média
(5) Maior
(6) Menor
(7) estaOrdenada por ordem crescente
(8) estaOrdenada por ordem decrescente
(9) Procura um elemento
(0) Sair
--------------------------------------------""")    
    
import random
def opçao_1():
    res = []
    n = random.randint(1,30)
    while n > 0:
        res.append(random.randint(1,100))
        n = n - 1
    return res

def opçao_2():
    res = []
    n1 = int(input("Qual o tamanho da sua lista?"))
    while n1 > 0:
        num = int(input("Introduza um número à lista:"))
        n1 = n1 - 1
        res.append(num)
    return res

def opçao_3(lista):
    soma = 0
    for i in lista:
        soma = soma + i
    return soma

def opçao_4(lista):
    soma = opçao_3(lista)
    return soma / len(lista)

def opçao_5(lista):
    maior = lista[0]
    for elem in lista[1:]:
        if elem > maior:
            maior = elem
    print(f"O maior elemento da tua lista é {maior}")

def opçao_6(lista):
    menor = lista[0]
    for elem in lista[1:]:
        if elem < menor:
            menor = elem
    print(f"O menor elemento da tua lista é {menor}")

def opçao_7(lista):
    for i in range(len(lista)-1):
        if lista[i] > lista[i + 1]:
            print("A tua lista não está por ordem crescente")
            return
    print("A tua lista está por orndem crecente")
def opçao_8(lista):
    for i in range(len(lista)-1):
        if lista[i] < lista[i + 1]:
            print("A tua lista não está por ordem decrescente")
            return
    print("A tua lista está por ordem decrescente")

def opçao_9(lista):
    elem = int(input("Introduza o número que quer encontrar:"))
    for i in range(len(lista)):
        if lista[i] == elem:
            print(f"Está na posição {i}")
            return
    print(-1)

def opçao_0():
    print("Aplicação terminada")
    print("---------------------------------------------")

def app():
    lista = []
    primeira_vez = True
    while True:
        print("---------------------------------------------")
        menu()
        opçao = int(input("Escolhe uma das opções: "))
        if opçao == 1:
            lista = opçao_1()
            print(f"A tua lista está criada: {lista}")
        elif opçao == 2:
            lista = opçao_2()
            print(f"A tua lista é: {lista}")
        elif opçao == 3:
            soma = opçao_3(lista)
            print(f"A soma da tua lista dá: {soma}")
        elif opçao == 4:
            media = opçao_4(lista)
            print(f"A média dos elementos da tua lista é: {media}")
        elif opçao == 5:
            opçao_5(lista)
        elif opçao == 6:
            opçao_6(lista)
        elif opçao == 7:
            opçao_7(lista)
        elif opçao == 8:
            opçao_8(lista)
        elif opçao == 9:
            opçao_9(lista)
        elif opçao == 0:
            opçao_0()
            print(f"Lista final: {lista}")
            print("---------------------------------------------")
            break

app()
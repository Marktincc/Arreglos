#1

import random
lista = []
numeros = (int(input("Digite El Rango: \n")))
for i in range(numeros):
    enteros = int(random.randint(-100, 100))
    lista.append(enteros)
def bubbleSort(lista):
    enteroslist = len(lista)
    for i in range(enteroslist - 1):
        for n in range(0, enteroslist - i - 1):
            if lista[n] > lista[n + 1]:
                lista[n], lista[n + 1] = lista[n + 1], lista[n]
    return lista
print(bubbleSort(lista))
print ()

#Elabore una aplicacion que permita introducir 20 elementos de mayor a menor

lista = []
print("Digite Sus 20 Numeros")
valores = 20
valor1 = 0
while valor1 < valores:
    print("Llevas Digitado", (valor1 + 1), "Elemento")
    enteros = int(input())
    lista.append(enteros)
    valor1 += 1
lista.sort(reverse=True)
print(("El Orden De Sus Elementos Esta De Mayor A Menor\n"), (lista))


#3

lista = []
lista1 = []
lista3 = []
print("Digite Sus 10 Numeros")
valores = 10
valor1 = 0
while valor1 < valores:
    print("Llevas Digitado", (valor1 + 1), "Numeros")
    enteros = int(input())
    lista.append(enteros)
    lista1.append(enteros)
    lista3.append(enteros)
    valor1 += 1
lista.sort(reverse=True)
lista1.sort()
print("Los Numeros Que Digito Son\n", str(lista3))
print(("El Orden De Sus Digitos Esta De Menor A Mayor\n"), str (lista1))
print(("El Orden De Sus Digitos Esta De Mayor A Menor\n"), str (lista))

#4

arreglo = [75, 3, 1, 54, 654, 87, 213, 0],
for posicion in arreglo:
    maximo = max(posicion)
    posicionmax = posicion.index(maximo)
    menor = min(posicion)
    posicionmin = posicion.index(menor)
print("El Arreglo Es: \n",str (arreglo))
print("El Valor Maximo Del Arreglo Es: ", str (maximo), "Y La Ubicacion Dentro Del Arreglo Es: ", str (posicionmax))
print("El Valor Minimo Del Arreglo Es: ", str (menor), "Y La Ubicacion Dentro Del Arreglo Es: ", str (posicionmin))

#5

lista = []
print("Digite Sus 10 Numeros")
valores = 10
valor1 = 0
asterisco = "*"
while valor1 < valores:
    print("Llevas Digitado", (valor1 + 1), "Numeros")
    enteros = int(input())
    lista.append(enteros)
    valor1 += 1
caracter1 = []
for i in lista:
    caracter = "*"
    a = (caracter * i)
    caracter1.append(a)
for n,c in zip(lista, caracter1):
    print (str(n)+ ":"+(c))

#6

lista = []
print("Digite Sus 25 Numeros")
valores = 25
valor1 = 0
while valor1 < valores:
    print("Llevas Digitado", (valor1 + 1), "Numeros")
    enteros = int(input())
    lista.append(enteros)
    valor1 += 1
print("El Arreglo Que Digitaste Fue :\n", (lista))
repetido=int(input("Digite El Numero Para Saber Cuantas Veces Se Encuentra En El Arreglo\n"))
cantidad = lista.count(repetido)
print("Las Veces Que Este Numero Esta Repetido En El Arreglo Es: ", (cantidad))

#7

lista = []
print("Digite Sus 8 Numeros")
valores = 8
valor1 = 0
lista = []
print("Digite Sus 8 Numeros")
valores = 8
valor1 = 0
impar = []
par = []
while valor1 < valores:
    print("Llevas Digitado", (valor1 + 1), "Numeros")
    enteros = int(input())
    lista.append(enteros)
    valor1 += 1
for i in range(valores):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
      impar.append(lista[i])
impar.sort()
par.sort()
print("El Arreglo Que Diste Fue: \n"+ str(lista),"\n""Los Numeros Impares Del Arreglo Son: \n"+ str(impar),"\n""Los Numeros Pares Del Arreglo Son: \n"+ str(par))
impar = []
par = []
while valor1 < valores:
    print("Llevas Digitado", (valor1 + 1), "Numeros")
    enteros = int(input())
    lista.append(enteros)
    valor1 += 1
for i in range(valores):
    if lista[i] % 2 == 0:
        par.append(lista[i])
    else:
      impar.append(lista[i])
impar.sort()
par.sort()
print("El Arreglo Que Diste Fue: \n"+ str(lista),"\n""Los Numeros Impares Del Arreglo Son: \n"+ str(impar),"\n""Los Numeros Pares Del Arreglo Son: \n"+ str(par))
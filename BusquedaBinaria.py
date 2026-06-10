numeros = []

while True:
    n = int(input("Ingrese un numero (0 para terminar): "))
    if n == 0:
        break
    elif 1 <= n <= 100:
        numeros.append(n)
    else:
        print("Número fuera de rango. Ingrese un número entre 1 y 100000.")

print(numeros)


def burbuja(numeros):
    for i in range(len(numeros)-1):
        for j in range(len(numeros)-i-1):
            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
    return numeros

print("Números ordenados:", burbuja(numeros))



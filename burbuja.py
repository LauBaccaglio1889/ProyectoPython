import csv

# ORDENAMIENTO (BURBUJA)
filas = []
with open('Compras_supermercado_Desordenado.csv', 'r') as f:
    lector = csv.reader(f)
    header = next(lector)
    for linea in lector:
        filas.append(linea)

n = len(filas)

for i in range(n):
    for j in range(0, n - i - 1):
        if (filas[j][0] > filas[j+1][0]) or (filas[j][0] == filas[j+1][0] and filas[j][1] > filas[j+1][1]):
            filas[j], filas[j+1] = filas[j+1], filas[j]


with open('COMPRAS_ordenado.csv', 'w', newline='') as f:
    escritor = csv.writer(f)
    escritor.writerow(header)
    escritor.writerows(filas)

print("Archivo 'COMPRAS_ordenado.csv' ordenado con éxito.")
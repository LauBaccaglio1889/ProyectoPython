import csv
import os

# ORDENAMIENTO (BURBUJA)


def ordenar_burbuja(datos):
    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (datos[j][0] > datos[j+1][0]) or (datos[j][0] == datos[j+1][0] and datos[j][1] > datos[j+1][1]):
                datos[j], datos[j+1] = datos[j+1], datos[j]
    return datos


print("Menu de compras:")


path_archivo = input("Ingrese el nombre del archivo CSV (ej: Compras_supermercado_Desordenado.csv): ").strip()
esta_ordenado = input("¿El archivo ya está ordenado? (s/n): ").upper()


header = []
filas = []
if os.path.exists(path_archivo):
    with open(path_archivo, 'r') as f:
        lector = csv.reader(f)
        header = next(lector)
        for linea in lector:
            filas.append(linea)
else:
     print(f"Error: El archivo '{path_archivo}' no existe. Por favor, verifique el nombre.")
     exit()
    

if esta_ordenado == 'N':
    filas = ordenar_burbuja(filas)
    with open('salida.txt', 'w', newline='') as f:
        escritor = csv.writer(f)
        escritor.writerow(header)
        escritor.writerows(filas)
    print("Archivo 'COMPRAS_ordenado.csv' ordenado con éxito.")
else:
    print("ejecucion directa...")




n = len(filas)
i = 0


print(f"{'SUCURSAL':<10} | {'PRODUCTO':<10} | {'TOT_UNI':<8} | {'TOT_PES'}")
print("-" * 50)

while i < n:
    sucursal_actual = filas[i][0]
    
    while i < n and filas[i][0] == sucursal_actual:
        producto_actual = filas[i][1]
        tot_uni = 0
        tot_pes = 0
        
        while i < n and filas[i][0] == sucursal_actual and filas[i][1] == producto_actual:
            cant = int(filas[i][4])
            precio = float(filas[i][5])
            tot_uni += cant
            tot_pes += (cant * precio)
            i += 1 
        
        print(f"{sucursal_actual:<10} | {producto_actual:<10} | {tot_uni:<8} | ${tot_pes:,.2f}")

print("-" * 50)
print("Proceso finalizado.")







i = 0  
print(f"{'ESTADÍSTICAS POR SUCURSAL':^60}")
print("="*60)

while i < n:
    sucursal_actual = filas[i][0]
    

    totsuc = 0      
    myprod = ""     
    myimpor = 0.0    
    mnpro = ""       
    mnimpor = float('inf') 

   
    while i < n and filas[i][0] == sucursal_actual:
        producto = filas[i][1]
        cantidad = int(filas[i][4])
        precio = float(filas[i][5])
        importe_fila = cantidad * precio
        
       
        totsuc += cantidad
        
      
        if importe_fila > myimpor:
            myimpor = importe_fila
            myprod = producto
            
       
        if importe_fila < mnimpor:
            mnimpor = importe_fila
            mnpro = producto
            
        i += 1 

    print(f"\n>> INFORME SUCURSAL: {sucursal_actual}")
    print(f"   - Total Unidades Compradas (TOTSUC): {totsuc}")
    print(f"   - Mayor Compra (MYPROD): {myprod} | Importe (MYIMPOR): ${myimpor:,.2f}")
    print(f"   - Menor Compra (MNPRO): {mnpro} | Importe (MNIMPOR): ${mnimpor:,.2f}")
    print("-" * 60)

print("\nFin del procesamiento por sucursales.")






i = 0 
cansuc = 0      
totalimp = 0.0 


while i < n:
    cansuc += 1
    sucursal_actual = filas[i][0]
    
   
    while i < n and filas[i][0] == sucursal_actual:
        cantidad = int(filas[i][4])
        precio = float(filas[i][5])
        
       
        totalimp += (cantidad * precio)
        
        i += 1 


print("\n" + "="*60)
print(f"{'RESUMEN GLOBAL DEL SUPERMERCADO (Punto C)':^60}")
print("="*60)
print(f" > CANTIDAD TOTAL DE SUCURSALES (CANSUC): {cansuc}")
print(f" > COMPRA TOTAL EN PESOS (TOTALIMP): ${totalimp:,.2f}")
print("="*60)

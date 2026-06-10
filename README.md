# ProyectoPython — Sistema de Compras Supermercado

Trabajo Práctico Integrador — Tecnicatura  
Alumno: Lautaro Baccaglio

## Descripción

Sistema en Python para el procesamiento de compras de un supermercado. Lee un archivo CSV con datos de compras, los ordena por sucursal y producto usando el algoritmo de burbuja, y genera reportes con totales, estadísticas por sucursal y resumen global.

## Archivos

- `compras.py` — programa principal: ordenamiento, totales y estadísticas
- `burbuja.py` — ordenamiento burbuja standalone
- `BusquedaBinaria.py` — búsqueda binaria con ordenamiento
- `test_compras.py` — tests unitarios automatizados
- `Compras_supermercado_Desordenado.csv` — datos de entrada
- `COMPRAS_ordenado.csv` — datos ordenados

## Cómo ejecutar

```bash
python3 compras.py
```

## Cómo correr los tests

```bash
python3 -m unittest test_compras -v
```

## CI/CD

El proyecto usa GitHub Actions para ejecutar los tests automáticamente en cada Push y Pull Request. El pipeline se define en `.github/workflows/ci.yml`.

## Requisitos

Ver `requeriments.txt`. No se requieren librerías externas, solo Python 3.

## Ramas

- `master` — rama principal protegida
- `rama-feature` — ejemplo de PR exitoso con pipeline verde
- `rama-error` — ejemplo de PR con error intencional y pipeline roja (abierto)
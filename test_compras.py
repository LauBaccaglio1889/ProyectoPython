import unittest

# ── Función copiada de compras.py para poder testearla ──────────────────────
def ordenar_burbuja(datos):
    n = len(datos)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (datos[j][0] > datos[j+1][0]) or (
                datos[j][0] == datos[j+1][0] and datos[j][1] > datos[j+1][1]
            ):
                datos[j], datos[j+1] = datos[j+1], datos[j]
    return datos


# ── Funciones auxiliares que replican la lógica de compras.py ────────────────
def calcular_totales(filas, sucursal, producto):
    """Devuelve (tot_uni, tot_pes) para una sucursal+producto dados."""
    tot_uni = 0
    tot_pes = 0.0
    for fila in filas:
        if fila[0] == sucursal and fila[1] == producto:
            cant = int(fila[4])
            precio = float(fila[5])
            tot_uni += cant
            tot_pes += cant * precio
    return tot_uni, tot_pes


def estadisticas_sucursal(filas, sucursal):
    """Devuelve (totsuc, myprod, myimpor, mnpro, mnimpor) para una sucursal."""
    totsuc = 0
    myprod = ""
    myimpor = 0.0
    mnpro = ""
    mnimpor = float('inf')

    for fila in filas:
        if fila[0] == sucursal:
            cantidad = int(fila[4])
            precio = float(fila[5])
            importe = cantidad * precio
            totsuc += cantidad
            if importe > myimpor:
                myimpor = importe
                myprod = fila[1]
            if importe < mnimpor:
                mnimpor = importe
                mnpro = fila[1]
    return totsuc, myprod, myimpor, mnpro, mnimpor


def resumen_global(filas):
    """Devuelve (cansuc, totalimp)."""
    sucursales_vistas = set()
    totalimp = 0.0
    for fila in filas:
        sucursales_vistas.add(fila[0])
        totalimp += int(fila[4]) * float(fila[5])
    return len(sucursales_vistas), totalimp


# ── TESTS ────────────────────────────────────────────────────────────────────
class TestOrdenarBurbuja(unittest.TestCase):

    def test_ordena_por_sucursal(self):
        """Con 2 elementos desordenados, burbuja debe ordenarlos."""
        datos = [
            ['SUC_B', 'Pan',   '', '', '3', '3.0'],
            ['SUC_A', 'Arroz', '', '', '2', '5.0'],
        ]
        resultado = ordenar_burbuja(datos)
        self.assertEqual(resultado[0][0], 'SUC_A')
        self.assertEqual(resultado[1][0], 'SUC_B')

    def test_ordena_por_producto_dentro_sucursal(self):
        """Con 2 productos desordenados en la misma sucursal, debe ordenarlos."""
        datos = [
            ['SUC_A', 'Leche', '', '', '1', '10.0'],
            ['SUC_A', 'Arroz', '', '', '2', '5.0'],
        ]
        resultado = ordenar_burbuja(datos)
        self.assertEqual(resultado[0][1], 'Arroz')
        self.assertEqual(resultado[1][1], 'Leche')

    def test_lista_vacia(self):
        """Una lista vacía debe devolver lista vacía."""
        self.assertEqual(ordenar_burbuja([]), [])

    def test_un_elemento(self):
        """Una lista con un solo elemento no debe cambiar."""
        datos = [['SUC_A', 'Arroz', '', '', '1', '5.0']]
        self.assertEqual(ordenar_burbuja(datos), datos)


class TestCalcularTotales(unittest.TestCase):

    def setUp(self):
        self.filas = [
            ['SUC_A', 'Leche', '', '', '3', '50.0'],
            ['SUC_A', 'Leche', '', '', '2', '50.0'],
            ['SUC_A', 'Arroz', '', '', '5', '20.0'],
            ['SUC_B', 'Leche', '', '', '1', '50.0'],
        ]

    def test_total_unidades(self):
        """Debe sumar correctamente las unidades de SUC_A / Leche."""
        tot_uni, _ = calcular_totales(self.filas, 'SUC_A', 'Leche')
        self.assertEqual(tot_uni, 5)

    def test_total_pesos(self):
        """Debe calcular correctamente el importe de SUC_A / Leche."""
        _, tot_pes = calcular_totales(self.filas, 'SUC_A', 'Leche')
        self.assertAlmostEqual(tot_pes, 250.0)

    def test_producto_distinto_no_se_mezcla(self):
        """Los totales de Arroz no deben incluir filas de Leche."""
        tot_uni, tot_pes = calcular_totales(self.filas, 'SUC_A', 'Arroz')
        self.assertEqual(tot_uni, 5)
        self.assertAlmostEqual(tot_pes, 100.0)


class TestEstadisticasSucursal(unittest.TestCase):

    def setUp(self):
        self.filas = [
            ['SUC_A', 'Leche', '', '', '10', '50.0'],   # importe 500
            ['SUC_A', 'Arroz', '', '', '1',  '20.0'],   # importe 20
            ['SUC_A', 'Pan',   '', '', '3',  '30.0'],   # importe 90
        ]

    def test_total_unidades_sucursal(self):
        totsuc, _, _, _, _ = estadisticas_sucursal(self.filas, 'SUC_A')
        self.assertEqual(totsuc, 14)

    def test_mayor_compra(self):
        _, myprod, myimpor, _, _ = estadisticas_sucursal(self.filas, 'SUC_A')
        self.assertEqual(myprod, 'Leche')
        self.assertAlmostEqual(myimpor, 500.0)

    def test_menor_compra(self):
        _, _, _, mnpro, mnimpor = estadisticas_sucursal(self.filas, 'SUC_A')
        self.assertEqual(mnpro, 'Arroz')
        self.assertAlmostEqual(mnimpor, 20.0)


class TestResumenGlobal(unittest.TestCase):

    def setUp(self):
        self.filas = [
            ['SUC_A', 'Leche', '', '', '2', '50.0'],
            ['SUC_A', 'Arroz', '', '', '3', '20.0'],
            ['SUC_B', 'Pan',   '', '', '1', '30.0'],
        ]

    def test_cantidad_sucursales(self):
        cansuc, _ = resumen_global(self.filas)
        self.assertEqual(cansuc, 2)

    def test_importe_total(self):
        _, totalimp = resumen_global(self.filas)
        # 2*50 + 3*20 + 1*30 = 100 + 60 + 30 = 190
        self.assertAlmostEqual(totalimp, 190.0)

    def test_lista_vacia(self):
        cansuc, totalimp = resumen_global([])
        self.assertEqual(cansuc, 0)
        self.assertAlmostEqual(totalimp, 0.0)


if __name__ == '__main__':
    unittest.main()
# ==============================================================================
# Universidad Nacional Abierta y a Distancia - UNAD
# Escuela de Ciencias Básicas, Tecnología e Ingeniería (ECBTI)
# Curso: Fundamentos de Programación (Código: 213022)
# Actividad: Fase 5 - Evaluación Final POA
# Problema 3: Inventario
# Autor: Camilo Gómez Bayona
# ==============================================================================

def calcular_cantidad_pedir(stock_actual, stock_minimo):
    """
    Calcula cuántas unidades deben solicitarse de un artículo.
    Si el stock actual es menor al mínimo, retorna la diferencia.
    De lo contrario, retorna 0.
    """
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0
    return cantidad


def generar_informe_reabastecimiento(matriz_inventario):
    """
    Recorre la matriz de inventario, invoca el cálculo de pedido
    y muestra el reporte final en pantalla.
    """
    print("=" * 55)
    print("       INFORME DE REABASTECIMIENTO DE INVENTARIO       ")
    print("=" * 55)
    print(f"{'ARTÍCULO':<32} | {'CANTIDAD A PEDIR':>18}")
    print("-" * 55)

    for articulo in matriz_inventario:
        # Extraemos los datos de cada fila según el formato:
        # [Código, Nombre, Stock actual, Stock mínimo]
        codigo = articulo[0]
        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        # Llamamos a la función modular para determinar el pedido
        pedido = calcular_cantidad_pedir(stock_actual, stock_minimo)

        # Mostramos la salida solicitada
        print(f"{nombre:<32} | {pedido:>15} und.")

    print("=" * 55)


# --- BLOQUE PRINCIPAL ---
if __name__ == "__main__":
    # Matriz con 5 artículos (Formato: [Código, Nombre, Stock actual, Stock mínimo])
    inventario = [
        ["ART-01", "Resistencia 10k Ohm", 45, 100],
        ["ART-02", "Condensador Electrolítico 100uF", 80, 50],
        ["ART-03", "Microcontrolador Arduino Uno", 12, 20],
        ["ART-04", "Protoboard 830 puntos", 15, 15],
        ["ART-05", "Sensor Ultrasónico HC-SR04", 8, 25]
    ]

    # Ejecución del informe
    generar_informe_reabastecimiento(inventario)

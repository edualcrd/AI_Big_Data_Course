import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Práctica Final
    """)
    return


@app.cell
def _():
    print("==========================================")
    print(" PARTE 1: EJERCICIOS Y COMPROBACIONES")
    print("==========================================\n")

    # 1. Diccionario de productos
    productos = {'manzana': 1.5, 'pan': 0.8, 'leche': 1.2}
    print("1. Producto inexistente:", productos.get('naranja', "No encontrado"))

    # 2. Frecuencia de palabras
    texto = "la casa es casa grande y la luz es luz"
    frecuencias = {}
    for palabra in texto.split():
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    mas_frecuentes = {k: v for k, v in frecuencias.items() if v == max(frecuencias.values())}
    print("\n2. Frecuencias:", frecuencias)
    print("   Más frecuentes:", mas_frecuentes)

    # 3. Conjuntos Lunes y Martes
    lunes = {'Ana', 'Luis'}
    martes = {'Ana', 'Luis', 'Marta', 'Jon'}
    print("\n3. Ambos días:", list(lunes & martes))
    print("   Solo el lunes:", list(lunes - martes))

    # 4. Lista a conjunto
    lista_original = [1, 2, 2, 3, 3, 3]
    print("\n4. Conjunto sin duplicados:", set(lista_original))

    # 5. Agenda (Diccionario anidado)
    agenda = {
        'Ana': {'telefono': '111222333', 'email': 'ana@email.com'},
        'Luis': {'telefono': '444555666', 'email': 'luis@email.com'}
    }
    print("\n5. Email Luis:", agenda.get('Luis', {}).get('email', 'No encontrado'))

    # 6. Importe Máximo
    pedidos = [
        {'cliente': 'Ana', 'importe': 30.5}, {'cliente': 'Ana', 'importe': 43.96},
        {'cliente': 'Luis', 'importe': 100.2}, {'cliente': 'Luis', 'importe': 186.45},
        {'cliente': 'Marta', 'importe': 59.9}, {'cliente': 'Jon', 'importe': 312.0}
    ]
    importe_maximo = {}
    for p in pedidos:
        if p['importe'] > importe_maximo.get(p['cliente'], 0):
            importe_maximo[p['cliente']] = p['importe']
    print("\n6. Importe máximo por cliente:", importe_maximo)

    # 7. Ranking (Ampliación)
    clientes_ordenados = sorted(importe_maximo.items(), key=lambda x: x[1], reverse=True)
    print("\n7. Ranking:")
    for i, (cliente, gasto) in enumerate(clientes_ordenados[:3], 1):
        print(f"   {i}. {cliente} ({gasto}€)")
    




    return


@app.cell
def _():
    print("\n==========================================")
    print(" PARTE 2: PRODUCTO EVALUABLE")
    print("==========================================\n")

    # 1. Contador propio y agenda
    texto_propio = "el aprendizaje de programacion en python es un aprendizaje continuo y python es muy potente"
    conteo_propio = {}
    for _p in texto_propio.split():
        conteo_propio[_p] = conteo_propio.get(_p, 0) + 1
    print("1. Contador texto propio:", conteo_propio)

    # 2. Resumen ventas propio
    pedidos_propios = [
        {'cliente': 'Carlos', 'dia': 'lunes', 'importe': 50},
        {'cliente': 'Maria', 'dia': 'lunes', 'importe': 120},
        {'cliente': 'Carlos', 'dia': 'lunes', 'importe': 20},
        {'cliente': 'Lucia', 'dia': 'lunes', 'importe': 90},
        {'cliente': 'Carlos', 'dia': 'martes', 'importe': 15},
        {'cliente': 'Maria', 'dia': 'martes', 'importe': 200},
        {'cliente': 'Jorge', 'dia': 'martes', 'importe': 110},
        {'cliente': 'Lucia', 'dia': 'martes', 'importe': 30}
    ]

    totales_dia = {}
    totales_cliente = {}
    clientes_lunes_v = set()
    clientes_martes_v = set()

    for _p2 in pedidos_propios:
        _d, _c, _i = _p2['dia'], _p2['cliente'], _p2['importe']
        totales_dia[_d] = totales_dia.get(_d, 0) + _i
        totales_cliente[_c] = totales_cliente.get(_c, 0) + _i
        if _d == 'lunes': clientes_lunes_v.add(_c)
        if _d == 'martes': clientes_martes_v.add(_c)

    print("\n2. Resumen Ventas:")
    print("   Total por día:", totales_dia)
    print("   Mejor cliente:", max(totales_cliente, key=totales_cliente.get))
    print("   Compraron ambos días:", clientes_lunes_v & clientes_martes_v)

    # 3. Operaciones de conjuntos
    A = {1, 2, 3}
    B = {3, 4, 5}
    print("\n3. Operaciones de conjuntos:")
    print("   A & B (Intersección): ->", A & B)
    print("   A | B (Unión): ->", A | B)
    print("   A - B (Diferencia): ->", A - B)
    print("   A ^ B (Diferencia simétrica): ->", A ^ B)

    return


@app.cell
def _(mo):
    mo.md("""
    **4. TABLA COMPARATIVA DE COLECCIONES**

    | Estructura  | Ejemplo               | ¿Qué pregunta responde?                         |
    |-------------|-----------------------|-------------------------------------------------|
    | Lista       | `[10, 25, 12, 10]`    | ¿Cuál es el orden exacto en el que llegaron estos valores? |
    | Tupla       | `(40.41, -3.70)`      | ¿Cuáles son las coordenadas exactas e inmutables? |
    | Diccionario | `{'Ana': 10, 'Jon': 5}`| ¿Cuántos puntos tiene cada jugador por su nombre?  |
    | Conjunto    | `{'rojo', 'azul'}`    | ¿Cuáles son los colores únicos, descartando repetidos? |
    """)
    return


if __name__ == "__main__":
    app.run()

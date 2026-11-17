import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Boletín 2 · Estructuras de datos, funciones y cadenas

    **Programación de IA · Unidad 1 · Capítulos 1.6 a 1.9**
    (listas y tuplas, diccionarios y conjuntos, funciones y cadenas)

    Este boletín tiene **10 ejercicios**. Los tres primeros trabajan listas y
    tuplas; el cuarto y el quinto, diccionarios y conjuntos; del sexto al octavo,
    funciones; el noveno, cadenas; y el décimo combina todo lo anterior.
    """)
    return


@app.cell
def _():
    # Rellena tus datos antes de empezar.
    alumno = "Eduardo Alcaide Rodríguez"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Cómo trabajar con este boletín

    **Estructura de cada ejercicio.**

    1. Una celda con el **enunciado**.
    2. Una celda de **código** con los datos ya escritos y huecos para tu solución.
       Escribe tu código debajo de cada apartado.
    3. En algunos ejercicios, una celda **«Tu respuesta»**: es texto en Markdown.
       Haz **doble clic** sobre ella para editarla y escribe tu explicación.

    **Reglas de marimo que debes conocer.**

    - En marimo **un nombre solo puede crearse en una celda**: eso incluye
      variables, variables de un `for`, funciones y clases. Si dos celdas crean el
      mismo nombre, marimo marca un error. La solución es usar nombres distintos en
      cada ejercicio o empezar el nombre por `_` (`_total`), que lo deja como
      privado de esa celda.
    - **No modifiques** las variables de datos que aparecen al principio de cada
      celda, salvo que el enunciado lo pida.
    - Muestra los resultados con `print()`. Aparecen en la salida de la celda.
    - No uses `input()`: los datos que "escribiría una persona" ya están en
      variables.
    - La **primera celda** (`import marimo as mo`) es necesaria para que
      funcionen las celdas de texto: no la borres ni la modifiques. En VS Code
      se ve aunque esté marcada como oculta.
    - Antes de entregar, comprueba que **no queda ninguna celda con error**.

    **Qué se valora.** Cada ejercicio puntúa sobre 1 punto. Se valora que el
    resultado sea correcto, que el código esté **comentado y sea legible** (nombres
    descriptivos) y que **justifiques** las decisiones cuando el enunciado lo pide.
    Un resultado correcto sin explicación no obtiene la puntuación completa.

    **Entrega.** Guarda el archivo y entrégalo en la tarea correspondiente de Moodle.

    **Ampliaciones.** Los apartados marcados como *Ampliación (opcional)* no son
    necesarios para entregar el boletín.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    # Bloque 1 · Listas y tuplas

    ## Ejercicio 1 · Los pedidos del día

    *Nivel: básico · Capítulo 1.6*

    La caja de TechShop ha registrado los importes de los pedidos del día en una
    lista, en el orden en que llegaron.

    **Se pide**, en este orden (la lista se va modificando):

    1. Muestra el **primer** importe, el **último** (con índice negativo) y los
       **tres primeros** (con un rebanado).
    2. Muestra la lista en **orden inverso** con un rebanado, sin modificarla.
    3. Actualiza la lista: llega un pedido de `75.00` (añádelo **al final**),
       otro de `15.00` que debe quedar en la **posición 2** (insértalo) y se anula
       el pedido de `59.90` (elimínalo por su valor). Muestra la lista y su
       longitud.
    4. Con la lista ya actualizada, muestra el total, la media (con dos decimales),
       el mayor y el menor.
    5. Muestra un **ranking** con los tres importes mayores, de mayor a menor,
       **sin modificar** la lista. Comprueba que la lista conserva su orden.

    En «Tu respuesta»: ¿qué valor devuelve `lista.sort()`? ¿Por qué escribir
    `ranking = importes_dia.sort()` es un error típico y qué tendría `ranking`?
    """)
    return


@app.cell
def _():
    # Datos del ejercicio (no los modifiques)
    # Esta lista guarda los importes de todos los pedidos del día.
    # Cada valor es un precio en euros.
    importes_dia = [43.96, 186.45, 59.90, 312.00, 27.50, 94.38]

    # 1. Primero, último y tres primeros
    # Accedemos al primer elemento con índice 0.
    print("Primer importe:", importes_dia[0])

    # Con índice -1 accedemos al último elemento.
    print("Último importe:", importes_dia[-1])

    # Con [:3] cogemos los tres primeros elementos, sin tocar el resto.
    print("Tres primeros:", importes_dia[:3])

    # 2. Orden inverso sin modificar la lista
    # Con [::-1] invertimos el orden de la lista.
    # Esto devuelve una nueva lista invertida, pero no cambia importes_dia.
    print("Orden inverso:", importes_dia[::-1])

    # 3. Actualizar la lista
    # append() añade un nuevo elemento al final.
    importes_dia.append(75.00)

    # insert(posición, valor) mete un valor en la posición indicada.
    # Aquí lo ponemos en la posición 2, empujando el resto hacia la derecha.
    importes_dia.insert(2, 15.00)

    # remove(valor) borra la primera aparición de ese valor.
    # En este caso se elimina el pedido de 59.90.
    importes_dia.remove(59.90)

    # Mostramos la lista ya modificada.
    print("Lista actualizada:", importes_dia)

    # len() devuelve cuántos elementos hay en la lista.
    print("Número de pedidos:", len(importes_dia))

    # 4. Resumen
    # sum() calcula la suma total de todos los importes.
    total_importes_dia = sum(importes_dia)

    # Dividimos el total entre la cantidad de elementos para obtener la media.
    media_importes_dia = total_importes_dia / len(importes_dia)

    print("Total:", total_importes_dia)
    print(f"Media: {media_importes_dia:.2f}")

    # max() y min() devuelven el importe más alto y más bajo de la lista.
    print("Mayor importe:", max(importes_dia))
    print("Menor importe:", min(importes_dia))

    # 5. Ranking sin modificar la lista
    # sorted() crea una nueva lista ordenada de menor a mayor o de mayor a menor.
    # Como ponemos reverse=True, la ordena de mayor a menor.
    # Con [:3] nos quedamos solo con los tres mayores.
    ranking_importes_dia = sorted(importes_dia, reverse=True)[:3]

    print("Tres importes mayores:", ranking_importes_dia)

    # Comprobamos que la lista original no se ha modificado, porque la hemos
    # ordenado con sorted() y no con sort().
    print("La lista conserva su orden:", importes_dia)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    lista.sort() ordena la lista en el mismo sitio y nos devuelve None.
    ranking = importes_dia.sort() modifica importes_dia y deja
    ranking con el valor de None; no guarda la lista ordenada. Para obtener una
    lista nueva ordenada sin alterar la original, podemos  usar
    ranking = sorted(importes_dia, reverse=True).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 2 · ¿Copia o referencia? Y tuplas

    *Nivel: medio · Capítulo 1.6*

    Un compañero ha escrito este código para calcular los precios de una oferta del
    10 %, pero después de ejecutarlo **los precios originales también han
    cambiado**:

    ```python
    precios = [100.0, 250.0, 80.0]
    precios_oferta = precios
    for posicion in range(len(precios_oferta)):
        precios_oferta[posicion] = precios_oferta[posicion] * 0.9
    print(precios)         # los originales han cambiado
    ```

    **Se pide:**

    1. Explica en «Tu respuesta» por qué ocurre.
    2. Escribe una versión correcta con `.copy()` y un bucle. Muestra las dos
       listas y comprueba con `is` que son objetos distintos.
    3. Escribe otra versión correcta con una *comprehension* que cree la lista de
       oferta (redondea a dos decimales). Muestra las dos listas.
    4. Un producto se guarda como tupla `(código, nombre, precio)`. **Desempaquétala**
       en tres variables y crea una **nueva** tupla con el precio subido un 10 %.

    En «Tu respuesta»: ¿qué error produce `producto[2] = 27.0` y por qué una tupla
    es adecuada para registrar un producto del catálogo? (No ejecutes esa línea.)
    """)
    return


@app.cell
def _():
    # Datos del ejercicio (no los modifiques)
    precios_originales = [100.0, 250.0, 80.0]
    producto_catalogo = ("TS-0042", "Ratón inalámbrico", 24.90)

    # 2. Copia con .copy() y un bucle
    # Creo una copia  de la lista para no tocar la original, porque si no, los precios originales cambiarían.
    precios_oferta_bucle = precios_originales.copy()

    # Recorro la nueva lista y aplico el descuento del 10% a cada elemento.
    # Lo hago con un bucle porque asi aprendo mejor como funciona.
    for posicion_oferta in range(len(precios_oferta_bucle)):
        precios_oferta_bucle[posicion_oferta] *= 0.9

    # Muestro los resultados para comprobar que la lista original se queda igual.
    print("Precios originales:", precios_originales)
    print("Oferta con copia y bucle:", precios_oferta_bucle)
    print("Son objetos distintos:", precios_originales is not precios_oferta_bucle)

    # 3. Con una comprehension
    # Aquí hago lo mismo pero de forma más corta, usando una "comprehension".
    precios_oferta_comprehension = [round(precio * 0.9, 2) for precio in precios_originales]
    print("Precios originales:", precios_originales)
    print("Oferta con comprehension:", precios_oferta_comprehension)

    # 4. Desempaquetar y crear una tupla nueva
    # Desempaqueto la tupla para guardar cada campo en una variable diferente.
    codigo_producto, nombre_producto, precio_producto = producto_catalogo

    # Creo una nueva tupla con el precio subido un 10% y redondeado.
    # No modifico la tupla original, porque las tuplas son inmutables.
    producto_actualizado = (codigo_producto, nombre_producto, round(precio_producto * 1.10, 2))
    print("Producto original:", producto_catalogo)
    print("Producto con subida del 10 %:", producto_actualizado)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    En el código original, precios_oferta = precios NO crea una lista nueva:
    las dos variables se refieren al mismo objeto. Al modificar los elementos a
    través de precios_oferta, cambian los que se ven en
    precios.

    producto[2] = 27.0 nos da un TypeError porque las tuplas no se pueden mutar:
    no nos permiten darle un valor a una de sus posiciones. Una tupla es adecuada
    para un producto del catálogo porque agrupa sus campos en un registro de
    estructura fija y evita cambios accidentales; para actualizarlo se crea una
    tupla nueva.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 3 · El catálogo en tres listas

    *Nivel: medio · Capítulo 1.6*

    Tres listas paralelas describen el catálogo: la posición `i` de cada lista
    corresponde al mismo producto.

    **Se pide**, con *comprehensions* cuando se indique:

    1. `precios_iva`: lista con cada precio más el 21 % de IVA, redondeado a dos
       decimales (*comprehension*).
    2. `productos_caros`: lista de los nombres de los productos que cuestan más de
       100 € (*comprehension* con `if`, y `zip` para recorrer nombres y precios).
    3. Con `enumerate` (empezando en 1), muestra el catálogo así:
       `1. teclado · 43.96 €`.
    4. `sin_existencias`: lista de los productos con 0 existencias (usa `zip`).
    5. Con `any` y `all`: ¿hay algún producto de más de 300 €? ¿Todos los precios
       son mayores que cero? Muestra los dos resultados.

    En «Tu respuesta»: ¿qué ocurriría con el apartado 4 si `existencias` tuviera
    solo 4 valores? ¿Por qué puede ser peligroso?
    """)
    return


@app.cell
def _():
    # Datos del ejercicio (no los modifiques)
    # Aquí tenemos dos listas paralelas: cada nombre está relacionado con su precio y su número de existencias en la misma posición.
    nombres_catalogo = ["teclado", "monitor", "webcam", "portátil", "hub"]
    precios_catalogo = [43.96, 186.45, 59.90, 312.00, 27.50]
    existencias_catalogo = [12, 0, 5, 3, 0]

    # 1. Precios con IVA
    # Para cada precio del catálogo, calculamos su valor con un 21% de IVA.
    # round(..., 2) redondea a dos decimales para que salga en formato de euros.
    precios_iva = [round(precio * 1.21, 2) for precio in precios_catalogo]
    print("Precios con IVA:", precios_iva)

    # 2. Productos de más de 100 €
    # Con zip() recorremos a la vez los nombres y los precios.
    # Solo añadimos al resultado los productos cuyo precio sea mayor que 100.
    productos_caros = [nombre for nombre, precio in zip(nombres_catalogo, precios_catalogo) if precio > 100]
    print("Productos caros:", productos_caros)

    # 3. Catálogo numerado
    # enumerate(..., start=1) nos da el índice empezando en 1.
    # También usamos zip() para recorrer cada nombre con su precio al mismo tiempo.
    for indice, (nombre, precio) in enumerate(zip(nombres_catalogo, precios_catalogo), start=1):
        print(f"{indice}. {nombre} · {precio:.2f} €")

    # 4. Productos sin existencias
    # Aquí comprobamos qué productos tienen 0 unidades disponibles.
    # Si existencias == 0, añadimos ese nombre a la lista.
    sin_existencias = [nombre for nombre, existencias in zip(nombres_catalogo, existencias_catalogo) if existencias == 0]
    print("Sin existencias:", sin_existencias)

    # 5. any y all
    # any() devuelve True si al menos un elemento cumple la condición.
    # En este caso, mira si hay algún precio superior a 300.
    hay_alguno_mas_300 = any(precio > 300 for precio in precios_catalogo)

    # all() devuelve True solo si todos los elementos cumplen la condición.
    # Aquí comprobamos que todos los precios sean mayores que cero.
    todos_precios_positivos = all(precio > 0 for precio in precios_catalogo)

    print("¿Hay algún producto de más de 300 €?:", hay_alguno_mas_300)
    print("¿Todos los precios son mayores que cero?:", todos_precios_positivos)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    Si existencias tuviera solo 4 valores, zip(nombres_catalogo, existencias_catalogo) solo emparejaría los primeros 4 nombres con los 4 valores. El último producto quedaría sin comprobar, porque zip se corta al elemento más corto y no lanza error. En ese caso, sin_existencias podría quedar incompleta y se perdería información.

    Es peligroso porque este tipo de error pasa “silenciosamente”: el programa sigue funcionando, pero con datos incompletos. En un catálogo real, eso puede provocar que un producto con existencias cero no se detecte o que un análisis de datos sea incorrecto sin avisar al usuario.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    # Bloque 2 · Diccionarios y conjuntos

    ## Ejercicio 4 · Contar, acumular y agrupar

    *Nivel: medio · Capítulo 1.7*

    La tabla de pedidos de la semana es una **lista de diccionarios**: cada pedido
    tiene `cliente`, `producto`, `importe` y `dia`.

    **Se pide:**

    1. `gasto_por_cliente`: diccionario `cliente → total gastado` (acumular).
    2. `pedidos_por_dia`: diccionario `día → número de pedidos` (contar).
    3. `productos_por_cliente`: diccionario `cliente → lista de productos`
       comprados, en orden de llegada (agrupar).
    4. El cliente que **más** ha gastado y su gasto (con `max` y `key=`).
    5. El gasto de `"Eva"`, que no ha comprado, sin que el programa falle: muestra
       `0.0`.

    En «Tu respuesta»: ¿por qué en los apartados 1 y 2 se usa `get` con un valor
    por defecto? ¿Qué pasaría en el apartado 5 con `gasto_por_cliente["Eva"]`?
    """)
    return


@app.cell
def _():
    # Datos del ejercicio (no los modifiques)
    pedidos_semana = [
        {"cliente": "Ana", "producto": "teclado", "importe": 43.96, "dia": "lunes"},
        {"cliente": "Luis", "producto": "monitor", "importe": 186.45, "dia": "lunes"},
        {"cliente": "Ana", "producto": "hub", "importe": 27.50, "dia": "martes"},
        {"cliente": "Marta", "producto": "webcam", "importe": 59.90, "dia": "martes"},
        {"cliente": "Jon", "producto": "portátil", "importe": 312.00, "dia": "martes"},
        {"cliente": "Luis", "producto": "hub", "importe": 27.50, "dia": "miércoles"},
        {"cliente": "Ana", "producto": "teclado", "importe": 43.96, "dia": "miércoles"},
    ]

    # 1. Gasto por cliente
    # Voy recorriendo cada pedido y acumulo el importe del cliente.
    # Si el cliente ya está en el diccionario, le sumo el importe.
    # Si no está, lo creo con valor inicial 0.0.
    gasto_por_cliente = {}
    for pedido in pedidos_semana:
        cliente = pedido["cliente"]
        importe = pedido["importe"]
        gasto_por_cliente[cliente] = gasto_por_cliente.get(cliente, 0.0) + importe

    print("Gasto por cliente:", gasto_por_cliente)

    # 2. Pedidos por día
    # Aquí cuento cuántos pedidos hubo cada día.
    # Para cada pedido, aumento el contador del día correspondiente.
    pedidos_por_dia = {}
    for pedido in pedidos_semana:
        dia = pedido["dia"]
        pedidos_por_dia[dia] = pedidos_por_dia.get(dia, 0) + 1

    print("Pedidos por día:", pedidos_por_dia)

    # 3. Productos por cliente
    # Quiero guardar para cada cliente la lista de productos que ha comprado.
    # Como la lista original está en orden de llegada añado cada producto al final.
    productos_por_cliente = {}
    for pedido in pedidos_semana:
        cliente = pedido["cliente"]
        producto = pedido["producto"]

        if cliente not in productos_por_cliente:
            productos_por_cliente[cliente] = []

        productos_por_cliente[cliente].append(producto)

    print("Productos por cliente:", productos_por_cliente)

    # 4. Mejor cliente
    # max() devuelve el elemento con el mayor valor según la clave que le damos.
    # En este caso, la clave es el gasto del cliente.
    cliente_mas_gasto, gasto_maximo = max(gasto_por_cliente.items(), key=lambda par: par[1])
    print(f"Cliente que más ha gastado: {cliente_mas_gasto} ({gasto_maximo:.2f} €)")

    # 5. Cliente sin pedidos
    # "Eva" no aparece en el diccionario, así que .get("Eva", 0.0) devuelve 0.0.
    # Esto evita que el programa falle si consultamos un cliente que no ha comprado.
    gasto_eva = gasto_por_cliente.get("Eva", 0.0)
    print("Gasto de Eva:", gasto_eva)
    return cliente, gasto_por_cliente


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Se usa get(..., valor) porque la clave puede aparecer por primera vez; si intentamos leerla antes de existir, Python da KeyError. Con get inicializamos el valor en 0.0 o 0 y luego sumamos/contamos.
    En el apartado 5, gasto_por_cliente["Eva"] falla porque "Eva" no existe en el diccionario. Gasto_por_cliente.get("Eva", 0.0) devuelve 0.0 y no rompe el programa.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5 · Conjuntos y elección de estructura

    *Nivel: medio · Capítulo 1.7*

    TechShop registra qué clientes compran cada día. Las listas **pueden tener
    repetidos** (un cliente puede comprar dos veces el mismo día).

    **Se pide:**

    1. Convierte cada lista en un conjunto y muestra, para cada día, el número de
       **pedidos** (longitud de la lista) y el de **clientes distintos**
       (longitud del conjunto).
    2. Clientes que compraron el lunes **y** el martes.
    3. Clientes que compraron **algún** día de los tres.
    4. Clientes que compraron **solo** el lunes (ni el martes ni el miércoles).
    5. Clientes que compraron el lunes **o** el martes, pero **no ambos**.
    6. En «Tu respuesta», completa la tabla: para cada pregunta, indica qué
       estructura usarías (lista, tupla, diccionario o conjunto) y por qué.
    """)
    return


@app.cell
def _():
    # Datos del ejercicio (no los modifiques)
    compras_lunes = ["Ana", "Luis", "Ana", "Eva"]
    compras_martes = ["Luis", "Marta", "Jon", "Luis"]
    compras_miercoles = ["Ana", "Jon", "Marta"]

    # 1. Conjuntos y comparación de longitudes
    # Convertimos cada lista en un conjunto para quitar repeticiones.
    # Así podremos contar clientes distintos sin que el mismo cliente aparezca dos veces.
    lunes_set = set(compras_lunes)
    martes_set = set(compras_martes)
    miercoles_set = set(compras_miercoles)

    print("Lunes: pedidos =", len(compras_lunes), "clientes distintos =", len(lunes_set))
    print("Martes: pedidos =", len(compras_martes), "clientes distintos =", len(martes_set))
    print("Miércoles: pedidos =", len(compras_miercoles), "clientes distintos =", len(miercoles_set))

    # 2. Clientes que compraron el lunes y el martes
    # La intersección nos da los clientes que están en ambos conjuntos.
    clientes_lunes_y_martes = lunes_set & martes_set
    print("Clientes que compraron el lunes y el martes:", sorted(clientes_lunes_y_martes))

    # 3. Clientes que compraron algún día de los tres
    # La unión de los tres conjuntos incluye a todos los clientes que han comprado en alguno de los días.
    clientes_alguna_vez = lunes_set | martes_set | miercoles_set
    print("Clientes que compraron algún día:", sorted(clientes_alguna_vez))

    # 4. Clientes que compraron solo el lunes
    # Restamos los clientes de martes y miércoles al conjunto del lunes.
    # Los que queden son los que compraron solo en lunes.
    solo_lunes = lunes_set - martes_set - miercoles_set
    print("Clientes que compraron solo el lunes:", sorted(solo_lunes))

    # 5. Clientes que compraron el lunes o el martes, pero no ambos
    # Primero unimos lunes y martes, y luego quitamos la intersección.
    # Así nos quedamos con los clientes que están en uno solo de los dos días.
    lunes_o_martes_no_ambos = (lunes_set | martes_set) - (lunes_set & martes_set)
    print("Clientes que compraron lunes o martes, pero no ambos:", sorted(lunes_o_martes_no_ambos))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    | Pregunta | Estructura | Por qué |
    |---|---|---|
    | Guardar los importes de la semana en el orden en que llegaron | lista | Nos deja guardar valores repetidos y conserva el orden de llegada. |
    | Saber a qué clientes hemos enviado un cupón, sin repetir ninguno | conjunto | Un conjunto elimina duplicados y es ideal para comprobar pertenencia o hacer operaciones como unión e intersección. |
    | Guardar la latitud y la longitud de una tienda | tupla | Es un par fijo de valores que están relacionados, con un orden específico: (latitud, longitud). |
    | Consultar el precio de un producto a partir de su nombre | diccionario | Permite asociar cada producto a su precio y acceder al valor directamente con la clave del nombre. |
    | Contar cuántas reseñas ha recibido cada producto | diccionario | Cada producto es una clave y el valor puede ser el número de reseñas acumuladas. |
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    # Bloque 3 · Funciones

    ## Ejercicio 6 · Mostrar no es devolver

    *Nivel: básico · Capítulo 1.8*

    Esta función calcula un precio con IVA, pero **no se puede usar en un cálculo**:

    ```python
    def precio_con_iva(precio, iva=0.21):
        print(round(precio * (1 + iva), 2))


    total = precio_con_iva(100) + precio_con_iva(50)   # TypeError
    ```

    **Se pide:**

    1. Escribe una versión correcta de `precio_con_iva` que **devuelva** el valor,
       con una *docstring* de una línea y el IVA como parámetro con valor por
       defecto `0.21`. Calcula con ella `total` para 100 € y 50 € y muéstralo.
    2. Llámala una vez con un IVA del 10 %, pasándolo **por nombre**.
    3. Escribe `estado_stock(unidades)`, que **devuelva** `"Agotado"` si no hay
       unidades, `"Pocas unidades"` si hay 5 o menos y `"Disponible"` en otro caso.
       Usa `return` en cada caso (sin variable auxiliar). Pruébala con 0, 3 y 20.
    4. Escribe `resumen_importes(importes)`, que devuelva **dos valores**: el total y
       la media. Recíbelos con desempaquetado y muéstralos.
    5. Escribe **dos `assert`** que comprueben `precio_con_iva` y uno que compruebe
       `estado_stock`.

    En «Tu respuesta»: ¿qué recibe `total` en el código original y por qué da
    error? ¿Qué diferencia hay entre `print` y `return`?
    """)
    return


@app.cell
def _():
    # Datos del ejercicio (no los modifiques)
    importes_resumen = [43.96, 186.45, 59.90]

    # 1. precio_con_iva
    # Defino la función para calcular un precio con IVA.
    # Tiene un valor por defecto de 0.21, así que si no se pasa IVA,
    # Python usará ese porcentaje.
    def precio_con_iva(precio, iva=0.21):
        """Devuelve el precio con IVA."""
        return round(precio * (1 + iva), 2)

    # Pruebo la función con los valores del ejemplo.
    total_100_50 = precio_con_iva(100) + precio_con_iva(50)
    print("Total de 100 € y 50 € con IVA:", total_100_50)

    # También puedo usar la lista de importes del ejercicio para hacer un resumen.
    total_lista = sum(precio_con_iva(precio) for precio in importes_resumen)
    print("Total de la lista con IVA:", total_lista)

    # 2. Con otro IVA, por nombre
    # Aquí paso el IVA por nombre para que se vea claramente.
    precio_iva_10 = precio_con_iva(100, iva=0.10)
    print("100 € con IVA del 10%:", precio_iva_10)

    # 3. estado_stock
    # Esta función devuelve un texto según cuántas unidades haya.
    def estado_stock(unidades):
        """Devuelve el estado del stock según la cantidad disponible."""
        if unidades == 0:
            return "Agotado"
        elif unidades <= 5:
            return "Pocas unidades"
        else:
            return "Disponible"

    # Pruebo varios casos para ver que funciona.
    print("Stock 0:", estado_stock(0))
    print("Stock 3:", estado_stock(3))
    print("Stock 20:", estado_stock(20))

    # 4. resumen_importes
    # Esta función devuelve dos valores: el total y la media.
    def resumen_importes(importes):
        """Devuelve el total y la media de una lista de importes."""
        total = sum(importes)
        media = total / len(importes)
        return total, media

    # Desempaqueto los dos valores que devuelve la función.
    total, media = resumen_importes(importes_resumen)
    print("Total:", total)
    print(f"Media: {media:.2f}")

    # 5. Comprobaciones con assert
    # assert sirve para comprobar que una condición es cierta. Si no lo es,
    # el programa lanza un error y nos dice que algo está mal.
    assert precio_con_iva(100) == 121.0
    assert precio_con_iva(50, iva=0.10) == 55.0
    assert estado_stock(0) == "Agotado"
    return (total,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    En el código original, precio_con_iv a solo usa print(), así que no devuelve ningún número. print() muestra el valor en pantalla, pero en realidad devuelve None. Por eso la expresión total = precio_con_iva(100) + precio_con_iva(50) falla con un TypeError, porque intenta sumar None + None.

    La diferencia es clara: print() sirve para mostrar un resultado, mientras que return sirve para devolverlo y poder usarlo en cálculos, asignaciones o comparaciones. Por eso, la versión correcta de la función debe return round(precio * (1 + iva), 2), y entonces total puede guardar ese valor y operar con él.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 7 · Refactorizar: no repitas código

    *Nivel: medio · Capítulo 1.8*

    La caja calcula el total de tres pedidos copiando el mismo código tres veces.
    La regla es: si el subtotal supera 50 €, se aplica un 5 % de descuento; después
    se añade el 21 % de IVA y se redondea a dos decimales.

    **Se pide:**

    1. Escribe una función `total_pedido(precio, unidades, ...)` que aplique esa
       regla. El umbral del descuento (`50`), el descuento (`0.05`) y el IVA
       (`0.21`) deben ser **parámetros con valor por defecto**. Incluye docstring.
    2. Calcula con ella los totales de los tres pedidos y guárdalos en
       `total_a_func`, `total_b_func` y `total_c_func`.
    3. Comprueba con `assert` que son **exactamente iguales** a los totales del
       código original, y muestra `Refactorización correcta`.

    En «Tu respuesta»: ¿qué ventaja concreta tiene tu versión si mañana la regla
    del descuento pasa del 5 % al 8 %? ¿Qué ha cambiado y qué se ha mantenido en la
    refactorización?
    """)
    return


@app.cell
def _():
    # Código original (repetido). No lo modifiques.
    precio_a = 24.90
    unidades_a = 3
    subtotal_a = precio_a * unidades_a
    if subtotal_a > 50:
        subtotal_a = subtotal_a * 0.95
    total_a = round(subtotal_a * 1.21, 2)

    precio_b = 12.50
    unidades_b = 2
    subtotal_b = precio_b * unidades_b
    if subtotal_b > 50:
        subtotal_b = subtotal_b * 0.95
    total_b = round(subtotal_b * 1.21, 2)

    precio_c = 99.90
    unidades_c = 1
    subtotal_c = precio_c * unidades_c
    if subtotal_c > 50:
        subtotal_c = subtotal_c * 0.95
    total_c = round(subtotal_c * 1.21, 2)

    print("Originales:", total_a, total_b, total_c)

    # Tu refactorización
    def total_pedido(precio, unidades, umbral=50, descuento=0.05, iva=0.21):
        """Calcula el total del pedido aplicando descuento e IVA."""
        subtotal = precio * unidades
        if subtotal > umbral:
            subtotal *= 1 - descuento
        return round(subtotal * (1 + iva), 2)


    total_a_func = total_pedido(precio_a, unidades_a)
    total_b_func = total_pedido(precio_b, unidades_b)
    total_c_func = total_pedido(precio_c, unidades_c)

    assert total_a_func == total_a
    assert total_b_func == total_b
    assert total_c_func == total_c

    print("Totales refactorizados:", total_a_func, total_b_func, total_c_func)
    print("Refactorización correcta")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    Si el descuento pasa del 5 % al 8 %, basta con cambiar el valor por defecto del parámetro `descuento` en un solo sitio. La refactorización elimina la repetición y facilita mantener la regla; se mantiene el mismo cálculo y los mismos resultados para los tres pedidos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 8 · Ámbito y la trampa de la lista por defecto

    *Nivel: medio · Capítulo 1.8*

    **Parte A · Ámbito.** Lee el código de la celda, **predice** qué mostrarán los
    dos `print` y escribe tu predicción en el comentario. Después ejecuta y
    explica el resultado.

    **Parte B · La lista por defecto.** La función `registrar_venta_mala` de la
    celda guarda las ventas de un día en una lista que es su valor por defecto.
    Llámala para dos días distintos y observa qué ocurre. Después:

    1. Explica en «Tu respuesta» el fallo.
    2. Escribe `registrar_venta` corregida (con `None` como valor por defecto) y
       demuestra con dos llamadas que cada día tiene su propia lista.
    """)
    return


@app.cell
def _():
    # Parte A · Ámbito
    descuento_global = 0.10


    def aplicar_oferta(precio):
        descuento_global = 0.20
        return precio * (1 - descuento_global)


    # Predicción: aplicará un descuento del 20 % y mostrará 80.0.
    # La variable global conservará el valor 0.10, así que mostrará 0.1.
    print(aplicar_oferta(100), descuento_global)


    # Parte B · La lista por defecto
    def registrar_venta_mala(importe, ventas=[]):
        ventas.append(importe)
        return ventas


    dia_lunes = registrar_venta_mala(20.0)
    dia_martes = registrar_venta_mala(35.0)
    # Ambas variables muestran la misma lista compartida: [20.0, 35.0].
    print("Lunes:", dia_lunes)
    print("Martes:", dia_martes)


    # Versión corregida: cada llamada sin lista crea una lista nueva.
    def registrar_venta(importe, ventas=None):
        if ventas is None:
            ventas = []
        ventas.append(importe)
        return ventas


    ventas_lunes = registrar_venta(20.0)
    ventas_martes = registrar_venta(35.0)
    print("Lunes (corregido):", ventas_lunes)
    print("Martes (corregido):", ventas_martes)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    La función que está incorrecta utiliza una lista mutable por defecto. Lo que Python hace es crear esa lista una sola vez y reutilizarla en cada llamada; por eso las ventas del lunes y del martes terminan en la misma lista: [20.0, 35.0].

    La versión corregida usa None como valor por defecto y crea una lista nueva dentro de la función. Así, las dos llamadas producen listas independientes: [20.0] y [35.0].
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    # Bloque 4 · Cadenas

    ## Ejercicio 9 · Analizar reseñas

    *Nivel: medio · Capítulo 1.9*

    TechShop ha recibido cuatro reseñas con espacios sobrantes, mayúsculas y signos
    de puntuación.

    **Se pide:**

    1. Escribe `normalizar(texto)`, que devuelva el texto sin espacios en los
       extremos, en minúsculas y **sin** los signos `. , ; ! ¡ ? ¿`.
    2. Con `split` y un diccionario, cuenta las palabras de **todas** las reseñas
       ya normalizadas, ignorando las de `palabras_vacias`.
    3. Muestra las **tres** palabras más frecuentes con su recuento, ordenadas de
       mayor a menor recuento y, si empatan, por orden alfabético. Para ordenar,
       puedes usar `sorted(conteo.items(), key=lambda par: (-par[1], par[0]))`
       (es una ampliación del capítulo 1.8: puedes copiarla).
    4. Cuenta cuántas reseñas contienen alguna de las palabras de queja
       (`roto`, `tarde`, `mal`), usando `any`.

    En «Tu respuesta»: ¿por qué hay que normalizar **antes** de contar? ¿Cuántas
    palabras distintas habría contado sin normalizar? ¿Por qué `palabras_vacias` es
    un conjunto?
    """)
    return


@app.cell
def _():
    # Datos del ejercicio (no los modifiques)
    # Estas son las reseñas que vamos a analizar.
    resenas = [
        "  Muy buen teclado, llegó rápido.  ",
        "El monitor LLEGÓ roto... ¡Muy mal!",
        "buen precio y buen envío",
        "Teclado MUY bueno; el envío, tarde.",
    ]

    # Palabras que queremos ignorar al contar frecuencia.
    # Son artículos y palabras muy comunes que no aportan significado.
    palabras_vacias = {"el", "y", "muy"}

    # Palabras que indican queja en una reseña.
    palabras_queja = ("roto", "tarde", "mal")

    # 1. Normalizar el texto
    # Esta función elimina espacios al principio y al final, pasa todo a minúsculas y quita signos de puntuación para que el texto sea comparable.
    def normalizar(texto):
        """Limpia y pasa el texto a minúsculas."""
        # Quitamos espacios sobrantes al principio y al final.
        texto = texto.strip().lower()

        # Eliminamos los signos de puntuación que pueden aparecer en las reseñas.
        # Los signos que quitamos son: punto, coma, punto y coma, exclamación, signos de apertura/cierre de interrogación.
        for signo in ".,;!¡?¿":
            texto = texto.replace(signo, "")

        return texto

    # Aplicamos la normalización a cada reseña para obtener texto uniforme.
    resenas_normalizadas = [normalizar(resena) for resena in resenas]
    print("Reseñas normalizadas:", resenas_normalizadas)

    # 2. Contar palabras que no estén en palabras_vacias
    # Usamos un diccionario para guardar la frecuencia de cada palabra.
    # La clave es la palabra y el valor es cuántas veces aparece.
    conteo_palabras = {}
    for resena in resenas_normalizadas:
        # Dividimos cada reseña en palabras.
        for palabra in resena.split():
            # Ignoramos las palabras vacías (muy comunes y poco útiles para análisis).
            if palabra not in palabras_vacias:
                # Si la palabra ya existe, incrementamos su contador.
                # Si no existe, la creamos con valor inicial 1.
                conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

    print("Recuento de palabras:", conteo_palabras)

    # 3. Ordenar por frecuencia y después alfabéticamente
    # sorted() recibe una lista de pares (palabra, frecuencia).
    # Ordenamos primero por frecuencia descendente y, si empatan, por palabra en orden alfabético.
    palabras_ordenadas = sorted(
        conteo_palabras.items(),
        key=lambda par: (-par[1], par[0])
    )

    # Mostramos solo las tres palabras más frecuentes.
    print("Tres palabras más frecuentes:", palabras_ordenadas[:3])

    # 4. Contar las reseñas que contienen alguna palabra de queja
    # Una reseña cuenta como "con queja" si alguna de las palabras indicadas aparece dentro de su lista de palabras.
    resenas_con_queja = 0
    for resena in resenas_normalizadas:
        # any() devuelve True si alguna condición se cumple.
        # Aquí comprobamos si alguna palabra clave está en la reseña.
        if any(palabra in resena.split() for palabra in palabras_queja):
            resenas_con_queja += 1

    print("Reseñas con alguna queja:", resenas_con_queja)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    Hay que normalizar antes de contar para que una palabra escrita con mayúsculas o signos de puntuación se cuente como la misma palabra. Sin normalizar, habría contado 18 palabras distintas (sin contar las palabras vacías que coinciden exactamente). palabras_vacias es un conjunto porque evita duplicados y permite comprobar rápidamente si una palabra se debe ignorar.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 10 · El parte de pedidos (ejercicio integrador)

    *Nivel: integrador · Capítulos 1.6 a 1.9*

    Soporte recibe los pedidos como líneas de texto con campos separados por `|`,
    con espacios y mayúsculas irregulares. El importe usa coma decimal y el símbolo
    del euro, y las unidades van pegadas al producto (`teclado x2`):

    ```text
    TS-0042 | ana garcía | teclado x2 | 43,96 €
    ```

    El último campo es el **precio de una unidad**.

    **Se pide:**

    1. `convertir_importe(texto)`: recibe `"43,96 €"` y devuelve `43.96` (`float`).
    2. `parsear_linea(linea)`: devuelve un diccionario con `codigo`, `cliente`
       (con la primera letra de cada palabra en mayúscula), `producto`, `unidades`
       (`int`), `precio_unitario` (`float`) y `total` (redondeado a 2 decimales).
       Usa `split("|")`, `strip`, `title` y `partition`.
    3. `registros`: lista con el resultado de `parsear_linea` para todas las líneas.
    4. `gasto_por_cliente`: diccionario `cliente → total`.
    5. Una tabla con f-strings, una fila por pedido, con estas anchuras: código (8),
       cliente (14), producto (10), unidades (3, a la derecha) y total (9, a la
       derecha, con dos decimales), seguido de ` €`. Después, el gasto de cada
       cliente.

    **Ampliación (opcional).** Valida el código con `re.fullmatch(r"TS-\d{4}", ...)`
    y descarta las líneas que no cumplan.

    En «Tu respuesta»: indica qué estructura has usado en cada paso (lista,
    diccionario, tupla…) y por qué, y qué función tiene cada una de las dos
    funciones que has escrito.
    """)
    return


@app.cell
def _(cliente, gasto_por_cliente, total):
    # Datos del ejercicio (no los modifiques)
    lineas_parte = [
        "TS-0042 | ana garcía | teclado x2 | 43,96 €",
        "TS-0043|LUIS PÉREZ|monitor x1|186,45 €",
        "TS-0044 | marta ruiz | hub x3 | 27,50 €",
        "TS-0045 | ana garcía | webcam x1 | 59,90 €",
    ]

    # 1. convertir_importe
    # Esta función toma un texto como "43,96 €" y lo convierte a número decimal.
    # Lo importante es cambiar la coma por punto, quitar el símbolo del euro y
    # dejarlo listo para hacer cálculos.
    def convertir_importe(texto):
        """Convierte un importe con coma y símbolo € en float."""
        texto = texto.strip().replace(",", ".").replace("€", "").strip()
        return float(texto)


    # 2. parsear_linea
    # Aquí leo cada línea del pedido y la convierto en un diccionario con los
    # datos bien separados: código, cliente, producto, unidades, precio y total.
    def parsear_linea(linea):
        """Devuelve un diccionario con los datos de una línea de pedido."""
        partes = [parte.strip() for parte in linea.split("|")]

        # Separamos la línea en 4 partes:
        # 1) código
        # 2) cliente
        # 3) producto y unidades
        # 4) precio unitario
        codigo, cliente, producto_y_unidades, precio_texto = partes

        # Normalizamos el nombre del cliente para que todas las palabras empiecen por mayúscula.
        cliente = cliente.title()

        # El producto viene escrito como "teclado x2", así que lo separamos en
        # nombre del producto y número de unidades.
        producto, separador, unidades_texto = producto_y_unidades.lower().partition("x")
        producto = producto.strip()
        unidades = int(unidades_texto.strip())

        # Convierto el precio del texto a float.
        precio_unitario = convertir_importe(precio_texto)

        # Calculo el total del pedido redondeado a dos decimales.
        total = round(precio_unitario * unidades, 2)

        # Devuelvo un diccionario con todos los datos.
        return {
            "codigo": codigo,
            "cliente": cliente,
            "producto": producto,
            "unidades": unidades,
            "precio_unitario": precio_unitario,
            "total": total,
        }


    # 3. Registros
    # Aquí creo la lista con todos los pedidos ya parseados.
    registros = [parsear_linea(linea) for linea in lineas_parte]

    # Lo imprimo para comprobar que la conversión ha salido bien.
    for pedido_ in registros:
        print(pedido_)


    # 4. Gasto por cliente
    # Acumulo el total de cada cliente en un diccionario.
    gasto_por_cliente_ = {}

    for pedido_ in registros:
        cliente_ = pedido_["cliente"]
        total_ = pedido_["total"]

        # Si el cliente ya existe, le sumo el total del nuevo pedido.
        # Si no existe, lo creo con ese total.
        gasto_por_cliente[cliente] = gasto_por_cliente.get(cliente, 0.0) + total

    print("\nGasto por cliente:")
    for cliente_, total_ in sorted(gasto_por_cliente_.items()):
        print(f"{cliente_}: {total_:.2f} €")


    # 5. Tabla
    # Muestro los pedidos en formato de tabla con anchuras fijas.
    print("\nTabla de pedidos:")
    print(f"{'CODIGO':<8} {'CLIENTE':<14} {'PRODUCTO':<10} {'UND':>3} {'TOTAL':>9}")
    for pedido_ in registros:
        print(
            f"{pedido_['codigo']:<8} "
            f"{pedido_['cliente']:<14} "
            f"{pedido_['producto']:<10} "
            f"{pedido_['unidades']:>3} "
            f"{pedido_['total']:>9.2f} €"
        )

    print("\nGasto por cliente en tabla:")
    for cliente_, total_ in sorted(gasto_por_cliente_.items()):
        print(f"{cliente:<14} {total:>9.2f} €")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    He usado una lista para guardar las líneas de entrada y otra lista, registros para reunir los pedidos ya procesados. Cada pedido se representa con un **diccionario**, porque así se accede a sus datos mediante claves como cliente o total. También uso un diccionario para acumular el gasto de cada cliente.

    convertir_importe transforma un importe escrito como texto en un número float. parsear_linea separa y normaliza los campos de una línea, calcula el total y devuelve un diccionario con los datos del pedido.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Antes de entregar

    - [ ] He rellenado `alumno` al principio.
    - [ ] No queda ninguna celda con error.
    - [ ] He escrito la respuesta en las celdas «Tu respuesta» donde se pide.
    - [ ] Mis funciones tienen docstring y nombres descriptivos.
    - [ ] Mi código tiene comentarios donde la lógica no es evidente.
    """)
    return


if __name__ == "__main__":
    app.run()

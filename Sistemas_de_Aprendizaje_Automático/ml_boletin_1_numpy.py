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
    # Boletín 1 · NumPy: arrays, formas y operaciones

    **Machine Learning · Unidad 1 · Capítulo 1.4**

    Este boletín tiene **10 ejercicios** y sigue el orden del capítulo, con el caso
    conductor de TechShop:

    | Bloque | Ejercicios | Tema |
    |---|---|---|
    | 1 · Forma y tipo | 1 a 3 | dimensiones, `shape`, `dtype`, creación de arrays y construcción de `X` e `y` |
    | 2 · Seleccionar y operar | 4 a 6 | indexación, operaciones vectorizadas y máscaras booleanas |
    | 3 · Estadística y datos incompletos | 7 y 8 | `axis`, orden, percentiles, `NaN`, copias y vistas |
    | 4 · Hacia el modelo | 9 y 10 | *broadcasting*, distancias, simulación reproducible y predicción con `X @ w` |

    La dificultad **sube de forma gradual**: los ejercicios 1 a 3 son básicos y
    el 10 integra casi todo lo anterior.
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
    3. Una celda **«Tu respuesta»**: es texto en Markdown. Haz **doble clic**
       sobre ella para editarla y escribe tu explicación.

    **Reglas de marimo que debes conocer.**

    - En marimo **un nombre solo puede crearse en una celda**: eso incluye
      variables, variables de un `for`, funciones y las importaciones. Si dos
      celdas crean el mismo nombre, marimo marca un error. La solución es usar
      nombres distintos en cada ejercicio o empezar el nombre por `_`
      (`_columna`), que lo deja como privado de esa celda.
    - **No modifiques** los arrays de datos que aparecen al principio de cada
      celda, salvo que el enunciado lo pida. Cuando necesites cambiar uno,
      trabaja sobre una **copia** (`.copy()`).
    - Muestra los resultados con `print()`. Aparecen en la salida de la celda.
    - Las operaciones deben ser **vectorizadas**: sin bucles de Python sobre los
      elementos de un array, salvo que el enunciado lo pida.
    - Cuando el enunciado pida **comprobar** algo, hazlo con `assert` o con
      `np.allclose`; no basta con mirar los números a ojo.
    - La **primera celda** (`import marimo as mo`) es necesaria para que
      funcionen las celdas de texto: no la borres ni la modifiques.
    - Antes de entregar, comprueba que **no queda ninguna celda con error**.

    **Qué se valora.** Cada ejercicio puntúa sobre 1 punto. Se valora que el
    resultado sea correcto, que el código esté **comentado y sea legible**
    (nombres descriptivos) y que **justifiques** las decisiones en las celdas
    «Tu respuesta». Un resultado correcto sin explicación no obtiene la
    puntuación completa.

    **Un hábito que te ayudará.** Antes de ejecutar una celda, **predice en voz
    alta la `shape`** de cada resultado. Casi todos los errores de NumPy y de
    scikit-learn se resuelven mirando las formas.

    **Entrega.** Guarda el archivo y entrégalo en la tarea correspondiente de Moodle.

    **Ampliaciones.** Los apartados marcados como *Ampliación (opcional)* no son
    necesarios para entregar el boletín.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Importaciones

    No modifiques esta celda salvo para **añadir** importaciones.
    """)
    return


@app.cell
def _():
    import time

    import numpy as np

    return (np,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    # Bloque 1 · Forma y tipo

    ## Ejercicio 1 · Radiografía de arrays

    *Nivel: básico · Capítulo 1.4 · sección 2*

    Antes de que un modelo reciba datos, hay que saber **qué estructura** son:
    ¿un número, una lista, una tabla, un montón de tablas? Para el equipo de
    TechShop se han preparado siete arrays. Antes de ejecutar nada, **intenta
    predecir** su `shape`.

    **Se pide:**

    1. Con un bucle sobre el diccionario `arrays_ej1`, imprime **una línea por
       array** con este formato (con los valores reales):
       `nombre: ndim=…, shape=…, size=…, dtype=…`.
    2. Comprueba con `assert` que `ventas_tensor.size` es igual al producto de los
       números de su `shape` (`4 * 7 * 3`).
    3. Muestra `columna_vector`, `columna_matriz` y `fila_matriz`. Observa que
       los tres contienen números de una sola «línea», pero no son lo mismo.

    En «Tu respuesta»: completa la tabla y contesta las preguntas.
    """)
    return


@app.cell
def _(np):
    # Datos del ejercicio (no los modifiques)
    precio_producto = np.array(24.90)
    visitas_semana = np.array([120, 250, 80, 300])
    tabla_producto = np.array([[120, 4.2], [250, 4.8], [80, 2.5]])
    ventas_tensor = np.zeros((4, 7, 3))  # 4 productos × 7 días × 3 medidas
    columna_vector = tabla_producto[:, 0]
    columna_matriz = tabla_producto[:, [0]]
    fila_matriz = np.array([[1, 2, 3]])

    arrays_ej1 = {
        "precio_producto": precio_producto,
        "visitas_semana": visitas_semana,
        "tabla_producto": tabla_producto,
        "ventas_tensor": ventas_tensor,
        "columna_vector": columna_vector,
        "columna_matriz": columna_matriz,
        "fila_matriz": fila_matriz,
    }

    # 1. Una línea por array
    for _nombre, _arr in arrays_ej1.items():
            print(f"{_nombre}: ndim={_arr.ndim}, shape={_arr.shape}, size={_arr.size}, dtype={_arr.dtype}")

    # 2. size = producto de los números de shape
    assert ventas_tensor.size == np.prod(ventas_tensor.shape)
    assert ventas_tensor.size == 4 * 7 * 3

    # 3. Los tres «de una línea»
    print("columna_vector:\n", columna_vector)
    print("columna_matriz:\n", columna_matriz)
    print("fila_matriz:\n", fila_matriz)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    Clasifica cada array como **escalar, vector, matriz o tensor** y di en una
    frase qué representa en TechShop:

    | Array | Tipo | Qué representa |
    |---|---|---|
    | `precio_producto` | Escalar (0D) | El precio unitario de un solo producto en TechShop (24,90 €) |
    | `visitas_semana` | Vector (1D) | El número de visitas registradas en cuatro periodos o productos. |
    | `tabla_producto` | Matriz (2D) | Una tabla de 3 productos (filas) con 2 características cada uno: visitas y valoración (columnas). |
    | `ventas_tensor` | Tensor (3D) | Un cubo de datos con 4 productos, 7 días de la semana y 3 medidas distintas por día. |
    | `columna_vector` | Vector (1D) | Las visitas de los 3 productos extraídas como una lista plana sin estructura de columna. |
    | `columna_matriz` | Matriz (2D) | Las mismas visitas de los 3 productos, pero manteniendo la formas de tabla de 3 filas × 1 columna. |
    | `fila_matriz` | Matriz (2D) | Una tabla de una única observación (1 fila) con 3 características (3 columnas). |

    **Preguntas.**

    1. Porque un array de NumPy solo puede almacenar un solo tipo de dato (dtype) en todos sus elementos. Como la segunda columna contiene decimales (4.2, 4.8, 2.5), NumPy nos da automáticamente los enteros de las visitas a float64 para que no perdamos los decimales.
    2. Pasaría columna_matriz (forma (3, 1)) como X, porque scikit-leanr obliga que las características sean siempre una matriz 2D de forma (n_observaciones, n_caracteristicas), incluso cuando solo hay una característica. Pasaría columna_vector (forma (3,1)) como "y" porque la variable objetivo debe ser un vector 1D con un valor por cada observación.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 2 · Tipos de datos: ni todo es `float64` ni todo cabe

    *Nivel: básico · Capítulo 1.4 · secciones 3.1 a 3.3*

    Un array guarda **un solo tipo** (`dtype`). Eso lo hace rápido, pero trae dos
    sorpresas: NumPy convierte tipos sin avisar y los enteros pequeños **se
    desbordan** sin dar error.

    **Se pide:**

    1. Crea un array con `mezcla_numeros` y otro con `mezcla_con_texto`. Muestra
       cada array y su `dtype`.
    2. Convierte `valoraciones_decimales` a enteros con `astype(int)` y muestra el
       resultado. Después hazlo **bien**: redondea primero y convierte después.
       Muestra los dos resultados.
    3. Suma `50` a `stock_almacen` (un array de `int8`) y muestra el resultado.
       Después corrige el problema convirtiendo antes a `int64` y vuelve a
       sumar.
    4. Crea con funciones de NumPy (sin escribir los valores a mano) y muestra
       `shape` y `dtype` de cada uno:
       - cinco precios **equiespaciados** de 10 a 50 (ambos incluidos);
       - una matriz de ceros decimales de 3 filas × 4 columnas;
       - la matriz identidad de 3 × 3;
       - los enteros 0, 25, 50 y 75.

    En «Tu respuesta»: explica por qué mezclar un texto convierte todo el array
    en texto, y por qué el apartado 3 es peligroso aunque no dé ningún error.
    Explica también qué error daría `np.zeros(3, 4)` y cómo se escribe bien. (No
    ejecutes esa línea.)
    """)
    return


@app.cell
def _(np):
    # Datos del ejercicio (no los modifiques)
    mezcla_numeros = [3, 4.5, 7]
    mezcla_con_texto = [3, 4.5, "7"]
    valoraciones_decimales = np.array([4.8, 2.6, 3.9, 4.2])
    stock_almacen = np.array([100, 120, 90], dtype=np.int8)

    # 1. Mezcla de tipos
    arr_numeros = np.array(mezcla_numeros)
    arr_texto = np.array(mezcla_con_texto)
    print("arr_numeros:", arr_numeros, "| dtype:", arr_numeros.dtype)
    print("arr_texto:", arr_texto, "| dtype:", arr_texto.dtype)

    # 2. Decimales a enteros: truncar frente a redondear
    val_truncadas = valoraciones_decimales.astype(int)
    val_redondeadas = np.round(valoraciones_decimales).astype(int)
    print("Truncadas con astype(int):", val_truncadas)
    print("Redondeadas y luego int:", val_redondeadas)

    # 3. Desbordamiento
    stock_desbordado = stock_almacen + 50
    stock_correcto = stock_almacen.astype(np.int64) + 50
    print("Desbordado (int8 + 50):", stock_desbordado, "| dtype:", stock_desbordado.dtype)
    print("Corregido (int64 + 50):", stock_correcto, "| dtype:", stock_correcto.dtype)

    # 4. Funciones de creación
    precios_equi = np.linspace(10, 50, 5)
    matriz_ceros = np.zeros((3, 4), dtype=float)
    matriz_identidad = np.eye(3)
    enteros_salto = np.arange(0, 100, 25)

    for _nom, _a in [
        ("precios_equi", precios_equi),
        ("matriz_ceros", matriz_ceros),
        ("matriz_identidad", matriz_identidad),
        ("enteros_salto", enteros_salto),
    ]:
        print(f"{_nom}: shape={_a.shape}, dtype={_a.dtype}\n{_a}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    - Mezcla con texto: Como todos los elementos de un array deben compartir el mismo dtype, NumPy busca el tipo más general capaz de representar todos los valores sin perder información. Un número puede representarse como texto ("3", "4.5"), pero un texto genérico no siempre puede convertirse a número; por eso todo el array pasa a ser de cadenas (`<U32`), lo que impide hacer cálculos aritméticos directamente sobre él.

    - Peligro del apartado 3: Un int solo almacena valores entre -128 y 127. Al sumar 50 a [100, 120, 90], el resultado supera 127 y da la vuelta a números negativos ([-106, -86, -116]) de forma silenciosa, sin lanzar ninguna excepción. En producción o en un modelo de ML esto introduce datos corruptos imposibles de detectar si no se comprueba el tipo o el rango.

    - Error en np.zeros(3, 4): Lanzaría un TypeError: Cannot interpret '4' as a data type, porque el primer argumento de np.zeros es la forma (shape) y el segundo es el dtype. Para crear una matriz de 3 × 4 hay que pasar las dimensiones agrupadas en una tupla: np.zeros((3, 4)).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 3 · Construir `X` e `y`

    *Nivel: básico · Capítulo 1.4 · secciones 4 y 5*

    scikit-learn (Unidad 3) exige que las características sean una **matriz `X` de
    forma `(n, p)`** (`n` observaciones, `p` características) y el objetivo, un
    **vector `y` de forma `(n,)`**. Casi todos los errores de principiante son de
    forma. Vas a prepararlas a mano.

    **Se pide:**

    1. Construye `X` con `np.column_stack` a partir de `visitas`, `valoraciones` y
       `precios`, e `y` a partir de `unidades`. Muestra `shape` y `dtype` de cada
       uno. Comprueba con `assert` que `X` es 2D, que `y` es 1D y que tienen el
       **mismo número de filas**.
    2. Prepara una `X` con **una sola característica** (solo `visitas`) de forma
       `(8, 1)` de dos maneras distintas. Muestra también `visitas` tal cual y
       `visitas.reshape(1, -1)`, y escribe sus tres `shape`.
    3. `tensor_ventas` guarda, para cada uno de los 8 productos, 7 días × 2 medidas
       (unidades y devoluciones). Conviértelo en una **matriz con una fila por
       producto** usando `reshape` y el comodín `-1`. Comprueba con
       `np.array_equal` que la fila 0 de la matriz es `tensor_ventas[0].ravel()`.
    4. Haz ahora `tensor_ventas.reshape(7, -1)`. Muestra su `shape` y comprueba (de
       nuevo con `np.array_equal`) si su fila 0 coincide con
       `tensor_ventas[0].ravel()`.

    En «Tu respuesta»: ¿qué mensaje daría scikit-learn si le pasaras `visitas`
    de forma `(8,)` como `X`, y cómo se arregla? ¿Por qué el apartado 4 **no da
    error** aunque esté mal?
    """)
    return


@app.cell
def _(np):
    # Datos del ejercicio (no los modifiques)
    visitas = np.array([120, 250, 80, 300, 170, 210, 95, 140])
    valoraciones = np.array([4.2, 4.8, 2.5, 4.9, 3.1, 4.4, 3.6, 3.9])
    precios = np.array([43.96, 186.45, 59.90, 312.00, 27.50, 94.38, 120.00, 35.25])
    unidades = np.array([90, 150, 40, 210, 100, 130, 55, 85])
    # (producto, día, medida): números consecutivos para poder ver el orden
    tensor_ventas = np.arange(8 * 7 * 2).reshape(8, 7, 2)

    # 1. X e y
    X_ej3 = np.column_stack([visitas, valoraciones, precios])
    y_ej3 = unidades.copy()
    print(f"X_ej3: shape={X_ej3.shape}, dtype={X_ej3.dtype}")
    print(f"y_ej3: shape={y_ej3.shape}, dtype={y_ej3.dtype}")
    assert X_ej3.ndim == 2
    assert y_ej3.ndim == 1
    assert X_ej3.shape[0] == y_ej3.shape[0]

    # 2. Una sola característica
    X_visitas_reshape = visitas.reshape(-1, 1)
    X_visitas_newaxis = visitas[:, np.newaxis]
    visitas_fila = visitas.reshape(1, -1)
    print("visitas.shape:", visitas.shape)
    print("X_visitas_reshape.shape:", X_visitas_reshape.shape)
    print("X_visitas_newaxis.shape:", X_visitas_newaxis.shape)
    print("visitas_fila.shape:", visitas_fila.shape)

    # 3. De tensor a matriz, una fila por producto
    matriz_ventas_ok = tensor_ventas.reshape(8, -1)
    print("matriz_ventas_ok.shape:", matriz_ventas_ok.shape)
    assert np.array_equal(matriz_ventas_ok[0], tensor_ventas[0].ravel())

    # 4. El reshape que no avisa
    matriz_ventas_mal = tensor_ventas.reshape(7, -1)
    print("matriz_ventas_mal.shape:", matriz_ventas_mal.shape)
    print("¿Coincide la fila 0 con el producto 0?:", np.array_equal(matriz_ventas_mal[0], tensor_ventas[0].ravel()))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    - Mensaje de scikit-learn y solución: Si se pasa visitas con forma (8,) como X, scikit-learn lanza un ValueError: Expected 2D array, got 1D array instead y sugiere explícitamente redimensionarlo con .reshape(-1, 1) (si es una sola característica con 8 observaciones) o .reshape(1, -1) (si fuera una sola observación con 8 características). En este caso se arregla con visitas.reshape(-1, 1) o visitas[:, np.newaxis].

    - Por qué no da error el apartado 4: tensor_ventas tiene 8 * 7 * 2 = 112 elementos. Como 112 es divisible entre 7 (112 / 7 = 16), NumPy acepta reshape(7, -1) y crea una matriz (7, 16) sin quejarse. Sin embargo, el resultado es semánticamente incorrecto: al leer los datos en orden secuencial, cada fila mezcla días y medidas de productos distintos, rompiendo la correspondencia entre filas y productos.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    # Bloque 2 · Seleccionar y operar

    ## Ejercicio 4 · Elegir datos con índices y *slicing*

    *Nivel: medio · Capítulo 1.4 · sección 6*

    La matriz `unidades_mensuales` guarda las unidades vendidas por TechShop:
    **una fila por producto** y **una columna por mes** (de enero a junio). Los
    nombres de los productos están en el vector `productos_nombres`, en el mismo
    orden que las filas.

    **Se pide**, con índices (sin bucles):

    1. Muestra las ventas del **monitor en marzo**, las ventas de **todos los
       productos en junio** (última columna, con índice negativo) y la **fila
       completa del portátil**.
    2. Con *slicing*, muestra la submatriz de los **tres primeros productos** y
       los **tres últimos meses**, y la de **todos los productos en los meses
       alternos** (enero, marzo y mayo). Escribe la `shape` de cada una.
    3. Con una **lista de índices**, muestra las ventas completas de teclado, hub
       y ratón (filas 0, 4 y 5) y, usando la misma lista, sus nombres.
    4. Trabajando sobre una **copia**, corrige los datos: el hub vendió **240** en
       abril (no 230) y el portátil vendió **24** en enero (no 20). Muestra las
       dos filas corregidas y comprueba que `unidades_mensuales` **no ha
       cambiado**.
    5. Muestra la `shape` de `unidades_mensuales[:, 1]`, de
       `unidades_mensuales[:, [1]]`, de `unidades_mensuales[1]` y de
       `unidades_mensuales[1:2]`.

    En «Tu respuesta»: ¿incluye `unidades_mensuales[1:4]` la fila 4? ¿Qué
    diferencia hay entre `[:, 1]` y `[:, [1]]`, y cuándo necesitarías cada una?
    """)
    return


@app.cell
def _(np):
    # Datos del ejercicio (no los modifiques)
    productos_nombres = np.array(["teclado", "monitor", "webcam", "portátil", "hub", "ratón"])
    #                              ene  feb  mar  abr  may  jun
    unidades_mensuales = np.array([
        [120, 135, 150, 110, 160, 180],   # teclado
        [ 40,  38,  45,  50,  52,  60],   # monitor
        [ 75,  80,  70,  95,  90, 100],   # webcam
        [ 20,  25,  22,  30,  28,  35],   # portátil
        [200, 190, 210, 230, 220, 250],   # hub
        [150, 160, 155, 170, 185, 190],   # ratón
    ])

    # 1. Elementos, columna y fila
    # Escribe aquí tu código

    # 2. Submatrices con slicing
    # Escribe aquí tu código

    # 3. Lista de índices
    # Escribe aquí tu código

    # 4. Corregir sobre una copia
    # Escribe aquí tu código

    # 5. Formas
    # Escribe aquí tu código
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    *(Escribe aquí tu respuesta. Haz doble clic en esta celda para editarla.)*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 5 · Operaciones vectorizadas y rendimiento

    *Nivel: medio · Capítulo 1.4 · secciones 1 y 7*

    Vectorizar es aplicar una operación a **todo el array a la vez**, sin bucle de
    Python. Es más corto, más legible y mucho más rápido. Lo comprobarás con tus
    propias medidas.

    **Se pide**, sin bucles en los apartados 1 a 3:

    1. Con los arrays `precios_prod`, `costes_prod` y `unidades_prod`, calcula:
       - `importes`: el importe vendido de cada producto;
       - `precios_iva`: el precio con un 21 % de IVA, redondeado a 2 decimales;
       - `margen_pct`: el margen sobre el precio, en porcentaje y con 1 decimal
         (`(precio − coste) / precio · 100`).
       Muestra los tres.
    2. Los descuentos que han pedido los comerciales están en `descuentos_pedidos`
       (en %). La política de TechShop **no permite más de un 30 %**: usa
       `np.clip` para limitarlos (y que ninguno sea negativo). Calcula también el
       `np.log` de los `importes`, redondeado a 2 decimales. Muestra ambos.
    3. Calcula el importe con IVA de dos formas: `(precios_prod * 1.21) *
       unidades_prod` y `precios_prod * (unidades_prod * 1.21)`. Compara los dos
       resultados primero con `==` (usa `.all()`) y después con `np.allclose`.
       Muestra qué elementos difieren con `==`.
    4. **Rendimiento.** Con `precios_millon` (un millón de precios) y su versión en
       lista `lista_millon`, calcula el precio con IVA (×1.21) de dos formas:
       con una *list comprehension* y con una operación vectorizada. Mide el
       tiempo de cada una con `time.perf_counter()` y muestra los dos tiempos en
       milisegundos y cuántas veces es más rápida la de NumPy. Comprueba con
       `np.allclose` que los dos resultados coinciden.

    En «Tu respuesta»: ¿por qué la versión de NumPy es más rápida? ¿Por qué
    `==` falla en el apartado 3 aunque las dos fórmulas sean matemáticamente
    iguales? Y ¿en qué situación **no** compensa vectorizar?
    """)
    return


@app.cell
def _(np):
    # Datos del ejercicio (no los modifiques)
    precios_prod = np.array([43.96, 186.45, 59.90, 312.00, 27.50, 94.38])
    costes_prod = np.array([30.00, 140.00, 41.50, 250.00, 18.20, 70.00])
    unidades_prod = np.array([90, 150, 40, 210, 100, 130])
    descuentos_pedidos = np.array([5, 12, 40, 0, 22, 35])
    precios_millon = np.random.default_rng(0).uniform(5, 500, size=1_000_000)
    lista_millon = precios_millon.tolist()

    # 1. Importes, precio con IVA y margen
    # Escribe aquí tu código

    # 2. Limitar descuentos y logaritmo
    # Escribe aquí tu código

    # 3. Comparar decimales
    # Escribe aquí tu código

    # 4. Bucle frente a vectorización
    # Escribe aquí tu código
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    *(Escribe aquí tu respuesta. Haz doble clic en esta celda para editarla.)*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 6 · Máscaras booleanas: filtrar, contar y modificar

    *Nivel: medio · Capítulo 1.4 · sección 8*

    Una **máscara** es un array de `True`/`False` que se usa para seleccionar los
    elementos que cumplen una condición. Es la herramienta con la que filtrarás
    observaciones en todo el curso. Aquí tienes 40 productos con sus visitas,
    valoración y unidades vendidas. Cuidado: la captura de valoraciones tiene
    **errores** (valores mayores que 5).

    **Se pide:**

    1. Crea la máscara `populares` (más de **250 visitas**). Muestra cuántos
       productos hay y qué porcentaje del catálogo representan (con un decimal),
       **sin bucles**: usa las propiedades de la máscara.
    2. Crea la máscara `trampa`: populares **y** con valoración **menor que 3.0**
       (mucho tráfico, mala reputación). Muestra cuántos son y las **posiciones**
       en que están (`np.flatnonzero`).
    3. Filtra **`X` e `y` con la misma máscara** `populares` y comprueba con
       `assert` que siguen alineadas. Muestra las unidades medias de los
       populares y del resto (`~populares`), con un decimal.
    4. Cuenta cuántas valoraciones son **mayores que 5**. Sobre una **copia** de
       las valoraciones, ponlas a `5.0` modificando con la máscara y comprueba
       que el máximo es ahora `5.0` y que el array original no ha cambiado.
    5. Con `np.where`, crea un vector de etiquetas: `"alta"` si las unidades
       superan la **mediana** de las unidades y `"baja"` en caso contrario.
       Muestra cuántas de cada tipo hay.

    En «Tu respuesta»: ¿por qué `(visitas_cat > 250) and (valoraciones_cat < 3.0)` da error y
    cómo se escribe bien? ¿Qué ocurriría si filtraras `X` pero no `y`?
    """)
    return


@app.cell
def _(np):
    # Datos del ejercicio (no los modifiques)
    _rng = np.random.default_rng(11)
    visitas_cat = _rng.integers(50, 400, size=40)
    valoraciones_cat = np.round(_rng.uniform(2.0, 5.0, size=40), 1)
    unidades_cat = np.round(0.25 * visitas_cat + 12 * valoraciones_cat + _rng.normal(0, 8, size=40)).astype(int)
    valoraciones_cat[[5, 17, 30]] = [5.7, 6.2, 5.3]   # errores de captura
    X_cat = np.column_stack([visitas_cat, valoraciones_cat])
    y_cat = unidades_cat

    # 1. Populares
    # Escribe aquí tu código

    # 2. Mucho tráfico y mala valoración
    # Escribe aquí tu código

    # 3. Filtrar X e y con la misma máscara
    # Escribe aquí tu código

    # 4. Corregir valoraciones fuera de rango en una copia
    # Escribe aquí tu código

    # 5. Etiquetas con np.where
    # Escribe aquí tu código
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    *(Escribe aquí tu respuesta. Haz doble clic en esta celda para editarla.)*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    # Bloque 3 · Estadística y datos incompletos

    ## Ejercicio 7 · Estadísticas por eje, orden y percentiles

    *Nivel: medio · Capítulo 1.4 · sección 9*

    La matriz `ventas_semana` recoge las ventas diarias (en €) de cinco categorías
    de TechShop durante una semana: **una fila por categoría** y **una columna por
    día** (de lunes a domingo).

    **Se pide:**

    1. Calcula el total y la media de **toda** la matriz; la media **por
       categoría** (una por fila) y la media **por día** (una por columna).
       Muestra cada resultado con su `shape` y redondea las medias a 1 decimal.
    2. Con `argmax` y `argmin`, muestra el **nombre de la categoría** con más
       ventas totales y el **nombre del día** con menos ventas totales.
    3. Muestra un **ranking** de las categorías de mayor a menor ventas totales,
       con su total (usa `argsort`).
    4. Calcula con `np.percentile` el primer cuartil (25), el tercer cuartil (75) y
       el rango intercuartílico (`IQR = Q3 − Q1`) de **todos los valores** de la
       matriz. Un valor es *atípico* si queda fuera del intervalo
       `[Q1 − 1.5 · IQR, Q3 + 1.5 · IQR]`. Muestra **ambos umbrales** y, con
       `np.where(máscara)`, la categoría y el día de cada valor atípico (combina
       las dos condiciones con `|`).
    5. Calcula con `np.corrcoef` la correlación entre las ventas diarias de
       *Audio* y de *Periféricos* (con 2 decimales), y el acumulado semanal
       (`np.cumsum`) de *Portátiles*.

    En «Tu respuesta»: ¿qué forma tiene el resultado de `axis=0` y el de
    `axis=1`, y cuál de las dos «hace desaparecer» las columnas? Mira los valores
    atípicos del apartado 4: ¿es razonable llamarlos así? ¿Qué cambiarías en el
    cálculo? ¿Tiene sentido el umbral inferior con ventas? Y, sobre la correlación del apartado 5: ¿significa que vender audio
    **hace** vender periféricos?
    """)
    return


@app.cell
def _(np):
    # Datos del ejercicio (no los modifiques)
    categorias = np.array(["Audio", "Periféricos", "Monitores", "Portátiles", "Accesorios"])
    dias = np.array(["lun", "mar", "mié", "jue", "vie", "sáb", "dom"])
    ventas_semana = np.array([
        [ 820,  760,  910,  880, 1450, 1620, 1100],   # Audio
        [ 640,  700,  655,  690,  980, 1210,  890],   # Periféricos
        [1900, 2100, 1850, 2000, 2300, 3900, 1500],   # Monitores
        [4200, 3900, 4500, 4100, 5200, 5600, 2800],   # Portátiles
        [ 310,  295,  330,  305,  520,  610,  480],   # Accesorios
    ])

    # 1. Resúmenes globales y por eje
    # Escribe aquí tu código

    # 2. Categoría con más ventas y día con menos
    # Escribe aquí tu código

    # 3. Ranking de categorías
    # Escribe aquí tu código

    # 4. Cuartiles y valores atípicos
    # Escribe aquí tu código

    # 5. Correlación y acumulado
    # Escribe aquí tu código
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    *(Escribe aquí tu respuesta. Haz doble clic en esta celda para editarla.)*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 8 · Valores faltantes, copias y vistas

    *Nivel: medio-alto · Capítulo 1.4 · secciones 10 y 13*

    En datos reales faltan valores. En NumPy un decimal faltante es `np.nan`, y
    tiene dos propiedades molestas: **contagia** a las operaciones y **no se
    puede buscar con `==`**. Además, algunas operaciones de NumPy devuelven una
    **vista** (comparte memoria con el original) y no una copia, así que
    modificarla altera los datos de partida. Aquí tienes `X_nan` (visitas y
    valoración) e `y_nan`; a dos productos les falta la valoración.

    **Se pide:**

    1. Muestra la media de `valoraciones_nan` con `mean()` y con `np.nanmean`;
       cuántos `NaN` hay (con `np.isnan`) y el resultado de
       `(valoraciones_nan == np.nan).sum()`.
    2. **Opción A, eliminar.** Crea `X_sin_nan` e `y_sin_nan` quitando las
       observaciones con valoración faltante, **manteniéndolas alineadas**.
       Muestra sus `shape` y comprueba con `assert` que no queda ningún `NaN` y
       que `X_sin_nan` e `y_sin_nan` tienen el mismo número de filas.
    3. **Opción B, imputar.** En una **copia** de `X_nan`, sustituye los `NaN` de
       la valoración por la **mediana** (`np.nanmedian`) de esa columna. Muestra
       la mediana usada, cuántos `NaN` quedan en la copia y cuántos en el
       original.
    4. La función `imputar_con_media` la ha escrito un compañero. Llámala con una
       **copia** de `valoraciones_nan` y comprueba cuántos `NaN` tiene esa copia
       **después** de la llamada. Escribe después `imputar_con_media_segura`, que
       haga lo mismo pero **no modifique** el array que recibe, y demuestra con
       una copia que el argumento conserva sus `NaN` y que el resultado no
       comparte memoria con él (`np.shares_memory`).
    5. Sobre una copia de trabajo de `valoraciones_nan`, crea `vista_cinco =
       copia[:5]` y `seleccion = copia[copia > 4]`. Muestra si cada una tiene
       como `.base` la copia (`.base is copia`). Después pon `vista_cinco[0] =
       0.0` y muestra `copia[0]`.

    En «Tu respuesta»: ¿eliminar o imputar? Justifica tu decisión para este caso
    (2 de 10 observaciones) y di qué riesgo tiene cada opción. Explica por qué la
    función del compañero es peligrosa.
    """)
    return


@app.cell
def _(np):
    # Datos del ejercicio (no los modifiques)
    visitas_nan = np.array([120, 250, 80, 300, 170, 210, 95, 140, 60, 330])
    valoraciones_nan = np.array([4.2, np.nan, 3.1, 4.8, 2.5, np.nan, 3.9, 4.4, 3.6, 4.9])
    unidades_nan = np.array([90, 150, 40, 210, 100, 130, 55, 85, 30, 220])
    X_nan = np.column_stack([visitas_nan, valoraciones_nan])
    y_nan = unidades_nan


    def imputar_con_media(columna):
        """Versión del compañero: rellena los NaN con la media de la columna."""
        columna[np.isnan(columna)] = np.nanmean(columna)
        return columna


    # 1. El contagio de NaN
    # Escribe aquí tu código

    # 2. Opción A: eliminar, manteniendo X e y alineadas
    # Escribe aquí tu código

    # 3. Opción B: imputar la mediana en una copia
    # Escribe aquí tu código

    # 4. La función del compañero y la versión segura
    # Escribe aquí tu código

    # 5. Vista o copia
    # Escribe aquí tu código
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    *(Escribe aquí tu respuesta. Haz doble clic en esta celda para editarla.)*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    # Bloque 4 · Hacia el modelo

    ## Ejercicio 9 · *Broadcasting*: estandarizar y buscar el producto más parecido

    *Nivel: alto · Capítulo 1.4 · sección 11*

    El *broadcasting* permite operar arrays de formas distintas «estirando» el
    pequeño. Con él se estandariza `X` (una operación que verás en casi todos los
    modelos) y se calculan distancias entre observaciones. Es la base de una idea
    muy simple de ML: **para predecir un producto nuevo, mira cuál se le parece
    más**.

    **Se pide:**

    1. Calcula las medias y las desviaciones típicas **por columna** de `X_prod`
       (`axis=0`) y estandarízala con `(X_prod - medias) / desvios`. Muestra la
       `shape` de las medias, de los desvíos y del resultado, y comprueba con
       `np.allclose` que cada columna estandarizada tiene media 0 y desviación 1.
    2. `ventas_canal` guarda las ventas de cinco productos en tres canales (web,
       tienda y app). Calcula la **distribución porcentual por producto** (cada
       fila debe sumar 100) dividiendo cada fila entre su total con
       `keepdims=True`. Comprueba con `np.allclose` que todas las filas suman
       100. Después, **sin** `keepdims` y dentro de un `try … except
       ValueError`, intenta la misma división e imprime el mensaje del error.
    3. Ha llegado un producto nuevo, `nuevo` (visitas, valoración, precio).
       Calcula su **distancia euclídea** a los 12 productos de `X_prod` con
       broadcasting (`sqrt(suma de (X − nuevo)²)` por filas) y muestra el índice y
       la distancia de los **tres más parecidos**.
    4. Repite el apartado 3 **estandarizando también `nuevo`** con las medias y
       desvíos de `X_prod` (no con los suyos propios, que no tiene). Muestra de
       nuevo los tres más parecidos. Compara el más cercano en cada caso
       mostrando su fila de `X_prod`.

    En «Tu respuesta»: explica qué `shape` tienen los dos operandos de
    `(X_prod - medias)` y qué hace NumPy para restarlos; por qué falla el
    apartado 2 sin `keepdims`; y por qué el producto más parecido **cambia** al
    estandarizar y cuál de los dos resultados es más razonable.
    """)
    return


@app.cell
def _(np):
    # Datos del ejercicio (no los modifiques)
    _rng = np.random.default_rng(5)
    _visitas = _rng.integers(50, 500, size=12)
    _valoraciones = np.round(_rng.uniform(1, 5, size=12), 1)
    _precios = np.round(_rng.uniform(15, 350, size=12), 2)
    X_prod = np.column_stack([_visitas, _valoraciones, _precios])   # (12, 3)
    ventas_canal = np.array([
        [120, 300, 80],     # web, tienda, app
        [450, 150, 400],
        [ 60,  90, 30],
        [200, 600, 100],
        [310, 205, 485],
    ])
    nuevo = np.array([175, 4.7, 307.00])   # visitas, valoración, precio

    # 1. Estandarizar por columnas
    # Escribe aquí tu código

    # 2. Porcentajes por fila con keepdims
    # Escribe aquí tu código

    # 3. Producto más parecido con las unidades originales
    # Escribe aquí tu código

    # 4. Producto más parecido estandarizando
    # Escribe aquí tu código
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    *(Escribe aquí tu respuesta. Haz doble clic en esta celda para editarla.)*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Ejercicio 10 · Simular, repartir y predecir con `X @ w`

    *Nivel: integrador · Capítulo 1.4 · secciones 12 a 14*

    Para terminar, un mini-proyecto con todo lo anterior. Simularás ventas de
    TechShop con una semilla fija, separarás las observaciones en dos grupos y
    medirás si un modelo lineal hecho a mano **mejora** una referencia muy simple:
    predecir siempre la media.

    **Se pide:**

    1. Con `np.random.default_rng(semilla)` simula `n_productos` (200) productos: `visitas` (enteros de
       50 a 499), `valoracion` (uniforme de 1 a 5, con un decimal) y `unidades`
       = `0.3 · visitas + 15 · valoracion + ruido`, donde el ruido es normal de
       media 0 y desviación 12; redondea las unidades a enteros. Construye `X`
       `(200, 2)` e `y` `(200,)`, comprueba sus formas con `assert` y muestra
       las tres primeras filas de `X` y los tres primeros valores de `y`.
    2. Comprueba la **reproducibilidad**: crea un segundo generador con la misma
       semilla, repite la simulación de `visitas` y comprueba con
       `np.array_equal` que obtienes exactamente lo mismo.
    3. **Reparte** con `rng.permutation`: 160 observaciones para entrenar y 40 para
       evaluar. Crea `X_ent`, `X_prueba`, `y_ent`, `y_prueba`, muestra sus
       `shape` y comprueba con `np.isin` que ningún índice está en los dos
       grupos.
    4. Predice con `X_prueba @ w + b` usando `w = [0.25, 12.0]` y `b = 0.0`.
       Muestra la `shape` de la predicción, el **error medio absoluto** (MAE) del
       modelo y el MAE de la **referencia** (predecir siempre la media de
       `y_ent`), ambos en el grupo de prueba y con 2 decimales. Indica cuánto
       mejora (en %).
    5. **Ajusta los pesos a mano**: prueba al menos tres combinaciones de `w` y
       `b` más y quédate con la mejor (menor MAE en **entrenamiento**, no en
       prueba). Muestra una tabla sencilla con las combinaciones probadas y,
       para la elegida, su MAE en prueba.
    6. Muestra las `shape` de `X_ent.T`, de `X_ent.T @ X_ent` y de `X_ent * w`.
       ¿Qué diferencia hay entre `X_ent * w` y `X_ent @ w`?
    7. *Ampliación (opcional).* Ajusta los pesos «de verdad» con
       `np.linalg.lstsq`: añade una columna de unos a `X_ent` (para el sesgo) y
       compara el MAE en prueba con el de tu mejor combinación.

    En «Tu respuesta»: ¿por qué se evalúa en el grupo de prueba y no en el de
    entrenamiento? ¿Mejora tu modelo la referencia? Escribe también una frase
    sobre el límite de trabajar con datos simulados.
    """)
    return


@app.cell
def _():
    # Datos del ejercicio (no los modifiques)
    semilla = 2026
    n_productos = 200

    # 1. Simulación reproducible
    # Escribe aquí tu código

    # 2. Reproducibilidad
    # Escribe aquí tu código

    # 3. Reparto entrenamiento / prueba
    # Escribe aquí tu código

    # 4. Predicción y comparación con la referencia
    # Escribe aquí tu código

    # 5. Ajuste a mano (se elige con el entrenamiento)
    # Escribe aquí tu código

    # 6. Formas y diferencia entre * y @
    # Escribe aquí tu código

    # 7. Ampliación (opcional): mínimos cuadrados
    # Escribe aquí tu código
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Tu respuesta**

    *(Escribe aquí tu respuesta. Haz doble clic en esta celda para editarla.)*
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    ## Antes de entregar

    - [ ] He rellenado `alumno` al principio.
    - [ ] No queda ninguna celda con error.
    - [ ] He escrito la respuesta en todas las celdas «Tu respuesta».
    - [ ] He usado operaciones vectorizadas, sin bucles sobre los elementos.
    - [ ] He comprobado las `shape` de `X` e `y` y he usado la misma máscara en ambas.
    - [ ] No he modificado los datos de partida (he trabajado con `.copy()`).
    - [ ] Mi código tiene comentarios donde la lógica no es evidente.
    """)
    return


if __name__ == "__main__":
    app.run()

# GUÍA PARA PRINCIPIANTES: UNA APLICACIÓN DE VENTAS
# Para ejecutarla, abre una terminal en esta carpeta y escribe:
# *************Ojo :python -m streamlit run comparador.py ******************
# Si faltan las bibliotecas, puedes instalarlas en tu entorno con:
# python -m pip install streamlit pandas numpy
#
# Los comentarios empiezan por # y Python no los ejecuta.
# Las instrucciones se ejecutan de arriba abajo. En Streamlit, una interacción
# con un control normalmente vuelve a ejecutar todo el archivo.
# import carga una biblioteca; «as» le asigna un nombre corto o alias.
# Usaremos st para Streamlit (interfaz) y pd para pandas (tablas de datos).
import streamlit as st
import pandas as pd
# NumPy permite hacer cálculos numéricos, aunque este script no lo utiliza.
import numpy as np

# Demo de Streamlit: Análisis Rápido de Ventas
# El punto accede a una función de la biblioteca; title muestra el título.
# Los paréntesis contienen los argumentos, es decir, los datos de la llamada.
# El texto entre comillas es una cadena de caracteres (str).
st.title("Demo de Streamlit: Evaluación de Ventas y Márgenes")
# Las comillas triples permiten escribir un texto de varias líneas.
st.write("""
Esta app sencilla permite:
- Ingresar ingresos y costos de un producto o proyecto
- Calcular beneficio bruto y margen
- Simular el efecto de un descuento sobre los ingresos
- Visualizar comparaciones en un gráfico de barras
""")

# 1) Ingresar ingresos y costos
st.header("1. Ingresar Datos de Ventas")
# Una variable guarda un valor. = asigna el resultado de la derecha al nombre
# de la izquierda. number_input muestra una casilla y devuelve su número.
# min_value es el mínimo; value el valor inicial; step el paso de los botones.
# Son argumentos con nombre: indican qué opción estamos configurando.
# 1000.0 es un float (número con decimales); Python utiliza el punto decimal.
ingresos = st.number_input("Ingresos (€)", min_value=0.0, value=1000.0, step=100.0)
costos = st.number_input("Costos (€)", min_value=0.0, value=600.0, step=50.0)

# 2) Cálculo de beneficio y margen
st.header("2. Cálculo de Beneficio y Margen")
# button devuelve True cuando se pulsa en esta ejecución y False si no.
# if significa «si»: ejecuta su bloque cuando la condición es verdadera.
# Los dos puntos abren el bloque; la sangría (espacios iniciales) lo delimita.
if st.button("Calcular Beneficio"):
    # Restamos los costos a los ingresos para calcular el beneficio.
    beneficio = ingresos - costos
    # Expresión condicional: calcula el porcentaje si ingresos > 0; si no, usa 0.
    # Evita dividir entre cero. Ese 0 es una convención de esta aplicación:
    # matemáticamente el margen no está definido cuando los ingresos son cero.
    # Ejemplo: (1000 - 600) / 1000 * 100 = 40 %.
    margen = (beneficio / ingresos * 100) if ingresos > 0 else 0
    # metric muestra una etiqueta y un valor. Una f-string inserta datos
    # mediante {...}: :.2f muestra dos decimales y :.1f muestra uno.
    # Este formato afecta al texto mostrado, no al valor numérico guardado.
    st.metric(label="Beneficio (€)", value=f"{beneficio:.2f}")
    st.metric(label="Margen (%)", value=f"{margen:.1f}")

# 3) Simulación de descuento
st.header("3. Simulación de Descuento")
# slider permite elegir un entero (int) entre 0 y 50; empieza en 10.
descuento = st.slider("% de descuento aplicado a ingresos", min_value=0, max_value=50, value=10)
# / divide y * multiplica. Los paréntesis se calculan primero.
# Con un 10 % de descuento, 1 - 10/100 = 0.9: conservamos el 90 % del ingreso.
# Ejemplo: 1000 euros pasan a ser 900. Suponemos que la cantidad vendida
# y los costos se mantienen constantes.
ingresos_desc = ingresos * (1 - descuento/100)
if st.button("Simular Descuento"):
    # Repetimos los cálculos con los ingresos reducidos por el descuento.
    beneficio_desc = ingresos_desc - costos
    margen_desc = (beneficio_desc / ingresos_desc * 100) if ingresos_desc > 0 else 0
    # write muestra texto en la página; las f-strings incluyen los resultados.
    st.write(f"Ingresos tras descuento: €{ingresos_desc:.2f}")
    st.write(f"Beneficio tras descuento: €{beneficio_desc:.2f}")
    st.write(f"Margen tras descuento: {margen_desc:.1f}%")

# 4) Gráfico de comparación
st.header("4. Gráfico Comparativo")
# checkbox devuelve True si la casilla está marcada; en ese caso se dibuja.
if st.checkbox("Mostrar gráfico de barras"):
    # Un DataFrame es una tabla con filas y columnas.
    # El diccionario {...} asocia cada nombre de columna con una lista [...].
    # Las listas agrupan valores ordenados y separados por comas.
    # Cada lista tiene tres elementos: nuestra tabla tendrá tres filas.
    data = pd.DataFrame({
        "Categoría": ["Ingresos", "Costos", "Beneficio"],
        "Valor (€)": [ingresos, costos, ingresos - costos]
    })
    # set_index usa las categorías como etiquetas de las filas.
    # bar_chart dibuja sus valores con barras. Aquí usamos los ingresos
    # originales, anteriores al descuento.
    st.bar_chart(data.set_index("Categoría"))

# Pie de página
# Sin sangría, volvemos fuera del if: este pie se muestra en cada ejecución.
# Streamlit interpreta --- como una línea horizontal en Markdown.
st.write("---")
st.write("Ejecuta: `streamlit run comparador.py` desde tu terminal para probar.")

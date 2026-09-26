# Pandas I–III — Guía del enriquecimiento Codex

## Nota Codex — Cómo recorrer los materiales

Estudia cada notebook del curso junto con su complemento, practica sus ejercicios
originales y, al terminar Pandas III, resuelve la práctica común. Se conservan el
contenido y la secuencia del curso; las explicaciones añadidas se identifican como
**Nota Codex**. Los complementos son cuadernos autónomos con ejemplos pequeños,
para evitar duplicar todo el curso.

1. [01 Pandas Base I EstructurasDeDatos Complemento Codex](../../12_PANDAS_I_ESTRUCTURA%20DE%20DATOS/01_Notebooks/01_Pandas_Base_I_EstructurasDeDatos_Complemento_Codex.ipynb)
2. [04 Pandas Base II Indexacion Complemento Codex](../../13_PANDAS_II_INDEXACION/01_Notebooks/04_Pandas_Base_II_Indexacion_Complemento_Codex.ipynb)
3. [07 Pandas Base III Importacion De Datos Complemento Codex](07_Pandas_Base_III_Importacion_De_Datos_Complemento_Codex.ipynb)
4. [08 Pandas I III Ejercicios Complemento Codex](08_Pandas_I_III_Ejercicios_Complemento_Codex.ipynb)
5. [09 Pandas I III Ejercicios Complemento Codex Soluciones](09_Pandas_I_III_Ejercicios_Complemento_Codex_Soluciones.ipynb)

## Nota Codex — Análisis previo y delimitación

Se revisaron los nueve notebooks de Pandas I, II y III, incluidos sus enunciados
y soluciones, antes de modificar el material. Se consultaron los cursos de Pandas
IV, V y VI y los tres notebooks de Visualización con Pandas (curso, ejercicios y
soluciones) de `18_VISUALIZACION/02_PANDAS/01_Notebooks`.

Los modelos de presentación fueron los cuadernos de Estadística descriptiva,
inferencial y conceptos avanzados, sus Complemento Codex, el complemento de tamaño
de muestra y los ejercicios complementarios con soluciones: títulos jerárquicos,
notas identificadas, preparación, ejemplos comentados y explicación del resultado.

| Tema observado | Decisión pedagógica | Ubicación |
|---|---|---|
| Series y DataFrame ya se presentan; falta anticipar el resultado de cada selección | Comparar dimensiones, escalar, Series, tabla y pérdida de etiquetas al pasar a NumPy | Complemento I, 1–2 |
| El índice se explica, pero no su efecto sobre cálculos y constructores | Mostrar alineación, operación con escalar y Series parcialmente coincidentes | Complemento I, 3–4 |
| Algunas afirmaciones sobre tipos y faltantes eran incorrectas | Corregir datetime64, category, object, arrays de extensión y la inferencia numérica | Notas del curso I y complemento I, 5 |
| loc e iloc se trabajan mucho, pero el índice automático disimula sus diferencias | Etiquetas no consecutivas, límites, selección vacía y errores controlados | Complemento II, 1–2 |
| Filtros ya presentes; falta explicar pertenencia, negación y alineación | isin, between, máscaras de Series y precauciones de asignación | Complemento II, 3–4 |
| MultiIndex, stack, unstack y xs ya están en el curso II | Precisar su comportamiento; reforzar solo selección por niveles, sin un curso nuevo de remodelado | Notas II y complemento II, 5 |
| read_csv ya cubre separadores y nulos especiales | Completar header/names, dtype, encoding, usecols, comillas y contrato de lectura | Complemento III, 1–4 |
| Se exportan archivos, pero falta comprobar la relectura | Verificar códigos, índice, tipos, faltantes y fechas tras exportar | Complemento III, 5 |
| Excel y SQL ya se introducen | Añadir selección de hojas, diccionario de hojas y conexión SQLite autónoma | Complemento III, 6–7 |
| shape, dtypes e info aparecen en el diagnóstico posterior | Solo usarlos aquí para explicar estructuras y verificar imports; no repetir diagnóstico | Pandas IV |
| Nulos, duplicados, estadísticos, frecuencias, muestreo y select_dtypes | No tratarlos como lagunas de I–III | Pandas IV |
| Conversión de tipos, imputación, eliminación, reemplazo, map y limpieza de texto | Remitir al módulo posterior; solo enseñar cómo seleccionar el destino de una asignación | Pandas V |
| Concatenación e integración de tablas por claves | No desarrollar concat, merge ni joins | Pandas VI |
| plot, histogramas, barras, líneas, densidad, boxplot, scatter, hexbin, subplots y estilos | No reproducir gráficos ni su preparación con groupby/crosstab | Visualización con Pandas |

## Nota Codex — Correcciones del material existente

- Rutas: se elimina la ruta G: del autor y se corrigen las rutas de los ejercicios
  de Pandas III. Los datos se localizan desde el notebook o la raíz del proyecto.
- Pandas I: se corrigen los tipos que admiten faltantes, el texto sobre inferencia
  numérica y la notación decimal de las temperaturas del enunciado.
- Pandas II: se corrige el título I → II, se evita ocultar `dict`, se precisa
  `future_stack=True` y se retira una letra `d` que provocaba NameError.
- Soluciones II: `2:6` incluye time, las etiquetas `9:19` representan los registros
  décimo a vigésimo y `1:5` incluye smoker después de reset_index. Se actualizan
  las salidas de referencia de los enunciados sin introducir código resuelto en
  las celdas para completar.
- Pandas III: `skiprows=3, header=None` expresa correctamente los metadatos y la
  ausencia de cabecera; la lista de nombres incluye id. Se corrige la explicación
  de fechas y zonas horarias, usando una copia para Excel. La vista previa lee
  solo las líneas necesarias. ArtistId se asigna como índice y se guarda.
- El ejemplo de portapapeles mantiene la llamada manual comentada y usa una
  muestra tabulada reproducible al ejecutar todo.

## Nota Codex — Archivos y datos

Se modificaron **9 notebooks originales** y se crearon **5 notebooks**:
tres complementos y dos cuadernos comunes de ejercicios. La práctica contiene
**15 ejercicios**: 4 de Pandas I, 4 de Pandas II, 6 de Pandas III y una síntesis.

También se incluyen `00_Datasets/tips.csv` y `tips_Fuente_Codex.md`, que documenta
la copia del dataset público de Seaborn. Los demás datos originales ya estaban
en 00_Datasets. Los ejemplos nuevos crean sus datos en memoria o en una carpeta
temporal; no requieren descargas ni variables de otro notebook.

## Nota Codex — Verificación

Verificación realizada el 26 de septiembre de 2026 con Python 3.12 y Pandas 2.3.1,
además de NumPy, IPython, openpyxl y SQLAlchemy instalados en el entorno.

- Los **14 notebooks** se ejecutaron de principio a fin en procesos Python
  independientes, con captura de salidas IPython y copias aisladas de los datos.
- Se revisaron **378 celdas de código** (incluidas las celdas vacías y de
  comentarios reservadas para respuestas). Las celdas que contienen instrucciones
  se ejecutaron en su orden; no se ejecutan respuestas aún no escritas.
- No hubo excepciones sin capturar ni advertencias en esa ejecución. Los errores
  intencionales de los complementos se capturan y explican.
- Se verificaron resultados concretos: selección de etiquetas, límites de rangos,
  independencia de copias, códigos con ceros iniciales, fecha 2 de abril, ausencia
  documentada, primera fila id=84 y exportación de ArtistId.
- Las relecturas CSV y Excel se comprobaron con aserciones. Se validó el formato
  de los notebooks y se conservaron las imágenes adjuntas del curso.
- Las salidas de las celdas ejecutables se actualizaron. Las salidas «No tocar»
  se sincronizaron con los corregidos; pueden borrarse si ejecutas esas celdas
  sin código, por lo que el cuaderno de soluciones sigue siendo la referencia.

Para reproducir en Jupyter: reinicia el kernel y ejecuta todas las celdas desde
arriba. Se requiere Pandas 2.1 o posterior por `future_stack=True`; la versión
validada es 2.3.1, sin afirmar una ejecución con otras versiones. La interacción
manual con el portapapeles queda fuera de la verificación automática. Las
exportaciones del curso III se guardan en `salidas_codex`; los complementos y
ejercicios nuevos usan una carpeta temporal y la eliminan en su celda de cierre.

## Nota Codex — Referencias técnicas

- [Lectura CSV](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html)
- [Indexación y selección](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [Representación de faltantes](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [stack](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html)

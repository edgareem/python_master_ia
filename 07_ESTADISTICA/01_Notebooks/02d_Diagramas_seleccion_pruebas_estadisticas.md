# Diagramas para seleccionar una prueba estadística

#### Complemento Codex — Estadística inferencial y planes experimentales

Estos diagramas amplían el esquema utilizado en Psicología. Incluyen las ramas marcadas con una cruz en el documento original, ya que las cruces indicaban únicamente que esos contenidos ya habían sido evaluados en L2.

El conjunto cubre los principales tests estudiados en estadística inferencial, Psicología y Data Science. Se ha dividido en varios diagramas para que las decisiones sigan siendo legibles.

> Para importarlos en draw.io: copia solamente el contenido de un bloque `mermaid` y utiliza **Insertar → Avanzado → Mermaid**.

---

## 1. Puerta de entrada: ¿qué quieres analizar?

```mermaid
flowchart TD
    A["Pregunta de investigación"] --> B{"Objetivo"}
    B --> C["Comparar grupos o condiciones"]
    B --> D["Estudiar una asociación"]
    B --> E["Comparar con un valor"]
    B --> F["Explicar o predecir"]
    C --> G{"Tipo de variable dependiente"}
    G --> H["Cuantitativa"]
    G --> I["Ordinal"]
    G --> J["Binaria o categórica"]
    D --> K["Diagrama 5"]
    E --> L["Diagrama 2"]
    F --> M["Diagrama 6"]
    H --> N["Diagrama 3"]
    I --> O["Diagrama 4"]
    J --> P["Diagrama 4"]
```

---

## 2. Una muestra comparada con un valor de referencia

```mermaid
flowchart TD
    A["Una muestra frente a un valor"] --> B{"Tipo de variable"}
    B --> C["Cuantitativa"]
    B --> D["Ordinal o cuantitativa muy asimétrica"]
    B --> E["Binaria"]
    C --> F["t de una muestra"]
    D --> G["Wilcoxon de una muestra"]
    E --> H{"Tamaño y frecuencias suficientes"}
    H -->|Sí| I["z de una proporción"]
    H -->|No| J["Binomial exacta"]
```

Hipótesis típicas para una media:

- bilateral: $H_0:\mu=\mu_0$ frente a $H_1:\mu\neq\mu_0$;
- unilateral superior: $H_0:\mu\leq\mu_0$ frente a $H_1:\mu>\mu_0$;
- unilateral inferior: $H_0:\mu\geq\mu_0$ frente a $H_1:\mu<\mu_0$.

---

## 3. VD cuantitativa: comparación de grupos o condiciones

Este es el desarrollo completo del diagrama de planes experimentales de Psicología.

```mermaid
flowchart TD
    A["VD cuantitativa"] --> B{"Número de variables independientes"}
    B -->|Una| C{"Relación entre medidas"}
    B -->|Varias| D{"Plan factorial"}
    C -->|Independientes| E{"Número de modalidades"}
    C -->|Repetidas| F{"Número de modalidades"}
    E -->|Dos| G["t de Welch independiente"]
    E -->|Más de dos| H["ANOVA de un factor"]
    F -->|Dos| I["t pareada"]
    F -->|Más de dos| J["ANOVA de medidas repetidas"]
    D -->|Todas intersujetos| K["ANOVA factorial independiente"]
    D -->|Todas intrasujetos| L["ANOVA factorial repetida"]
    D -->|Inter e intra| M["ANOVA mixta"]
```

### Alternativas y extensiones para la VD cuantitativa

```mermaid
flowchart TD
    A["Prueba cuantitativa prevista"] --> B{"Problema principal"}
    B --> C["Dos grupos independientes no paramétricos"]
    B --> D["Más de dos grupos independientes"]
    B --> E["Dos medidas relacionadas no paramétricas"]
    B --> F["Más de dos medidas relacionadas"]
    C --> G["Mann–Whitney"]
    D --> H["Welch si varianzas desiguales"]
    D --> I["Kruskal–Wallis si rangos"]
    E --> J["Wilcoxon de rangos con signo"]
    F --> K["Friedman si rangos"]
```

### Casos adicionales

```mermaid
flowchart TD
    A["Diseño cuantitativo ampliado"] --> B{"Elemento adicional"}
    B --> C["Una covariable cuantitativa"]
    B --> D["Varios predictores"]
    B --> E["Varias VD cuantitativas"]
    B --> F["Datos agrupados o incompletos"]
    C --> G["ANCOVA"]
    D --> H["Regresión lineal"]
    E --> I["MANOVA"]
    F --> J["Modelo lineal mixto"]
```

#### Notas de selección

- Se recomienda **Welch** para dos grupos independientes porque no exige igualdad de varianzas.
- Para más de dos grupos independientes, una ANOVA de Welch sustituye a la ANOVA clásica cuando las varianzas son claramente diferentes.
- Mann–Whitney, Wilcoxon, Kruskal–Wallis y Friedman trabajan con rangos; no son simplemente tests de igualdad de medias.
- Un modelo lineal mixto es especialmente útil con medidas repetidas desiguales, datos faltantes o participantes agrupados en aulas, centros u hospitales.

---

## 4. VD ordinal, binaria o categórica

### 4.1. Variable ordinal

```mermaid
flowchart TD
    A["VD ordinal"] --> B{"Relación entre observaciones"}
    B -->|Independientes| C{"Número de grupos"}
    B -->|Relacionadas| D{"Número de momentos"}
    C -->|Dos| E["Mann–Whitney"]
    C -->|Más de dos| F["Kruskal–Wallis"]
    D -->|Dos| G["Wilcoxon"]
    D -->|Más de dos| H["Friedman"]
    A --> I["Modelo ordinal si hay varios predictores"]
```

### 4.2. Variable binaria o categórica

```mermaid
flowchart TD
    A["VD binaria o categórica"] --> B{"Relación entre observaciones"}
    B -->|Independientes| C{"Estructura"}
    B -->|Relacionadas| D{"Número de momentos"}
    C -->|Dos proporciones| E["z de dos proporciones"]
    C -->|Tabla de contingencia| F["Chi-cuadrado de independencia"]
    C -->|Frecuencias pequeñas| G["Fisher exacta"]
    D -->|Dos medidas binarias| H["McNemar"]
    D -->|Más de dos medidas binarias| I["Q de Cochran"]
```

### Modelos para varias variables explicativas

```mermaid
flowchart TD
    A["Varias variables explicativas"] --> B{"Tipo de resultado"}
    B --> C["Binario"]
    B --> D["Nominal con más de dos categorías"]
    B --> E["Ordinal"]
    B --> F["Recuento"]
    C --> G["Regresión logística binaria"]
    D --> H["Regresión logística multinomial"]
    E --> I["Regresión logística ordinal"]
    F --> J["Poisson o binomial negativa"]
```

#### Nota sobre chi-cuadrado y Fisher

La elección no depende únicamente de que la muestra total sea mayor que 30. Hay que examinar las **frecuencias esperadas dentro de las celdas**. Fisher es especialmente útil en tablas 2 × 2 con frecuencias pequeñas.

---

## 5. Asociación entre variables

```mermaid
flowchart TD
    A["Estudiar una asociación"] --> B{"Tipos de variables"}
    B --> C["Dos cuantitativas"]
    B --> D["Ordinales o relación monótona"]
    B --> E["Dos categóricas"]
    B --> F["Una binaria y una cuantitativa"]
    C --> G{"Relación aproximadamente lineal"}
    G -->|Sí| H["Correlación de Pearson"]
    G -->|No| I["Spearman o modelo no lineal"]
    D --> J["Spearman o Kendall"]
    E --> K["Chi-cuadrado y V de Cramér"]
    F --> L["Correlación punto-biserial"]
```

#### Punto de vigilancia

La correlación no demuestra causalidad. Antes de calcularla hay que observar un gráfico de dispersión, la forma de la relación y los valores extremos.

---

## 6. Explicar o predecir

```mermaid
flowchart TD
    A["Explicar o predecir una VD"] --> B{"Tipo de VD"}
    B --> C["Cuantitativa"]
    B --> D["Binaria"]
    B --> E["Categórica u ordinal"]
    B --> F["Recuento"]
    C --> G["Regresión lineal"]
    D --> H["Regresión logística binaria"]
    E --> I["Logística multinomial u ordinal"]
    F --> J["Poisson o binomial negativa"]
```

Si hay observaciones agrupadas o repetidas, se utilizan versiones mixtas o multinivel de estos modelos.

---

## 7. Verificación de las condiciones

La verificación no sustituye la selección según el plan experimental. Se realiza después de identificar la familia correcta de pruebas.

```mermaid
flowchart TD
    A["Prueba seleccionada según el diseño"] --> B{"Comprobaciones"}
    B --> C["Independencia según la recogida"]
    B --> D["Residuos o diferencias"]
    B --> E["Varianzas y valores extremos"]
    C --> F["Cambiar a método pareado, repetido o mixto si procede"]
    D --> G["Histograma, Q–Q y Shapiro como apoyo"]
    E --> H["Levene, Welch o método robusto"]
```

### Lo que debe comprobarse

1. **Independencia:** viene determinada por la recogida de datos.
2. **Normalidad:** se estudia principalmente en los residuos; para la t pareada, en las diferencias.
3. **Varianzas:** si son desiguales entre grupos independientes, se prefiere Welch.
4. **Valores extremos:** se investigan; no se eliminan solo para obtener significación.
5. **Tamaño y frecuencias:** en proporciones y tablas categóricas importan los recuentos esperados.

---

## 8. Después de una prueba global significativa

```mermaid
flowchart TD
    A["Prueba global significativa"] --> B{"Prueba realizada"}
    B --> C["ANOVA clásica"]
    B --> D["ANOVA de Welch"]
    B --> E["Kruskal–Wallis"]
    B --> F["Medidas repetidas"]
    C --> G["Post hoc de Tukey"]
    D --> H["Post hoc de Games–Howell"]
    E --> I["Dunn con corrección"]
    F --> J["Comparaciones pareadas corregidas"]
```

Una ANOVA significativa indica que existe al menos una diferencia, pero no identifica por sí sola qué grupos difieren. Las comparaciones múltiples deben corregirse, por ejemplo mediante Holm o Bonferroni.

---

## 9. Tabla maestra de selección

| VD | Objetivo y diseño | Prueba principal | Alternativa o extensión |
|---|---|---|---|
| Cuantitativa | una muestra frente a un valor | t de una muestra | Wilcoxon de una muestra |
| Cuantitativa | dos grupos independientes | t de Welch | Mann–Whitney |
| Cuantitativa | dos medidas relacionadas | t pareada | Wilcoxon |
| Cuantitativa | más de dos grupos independientes | ANOVA o ANOVA de Welch | Kruskal–Wallis |
| Cuantitativa | más de dos medidas relacionadas | ANOVA de medidas repetidas | Friedman |
| Cuantitativa | varias VI intersujetos | ANOVA factorial independiente | modelo lineal |
| Cuantitativa | varias VI intrasujetos | ANOVA factorial repetida | modelo lineal mixto |
| Cuantitativa | factores inter e intra | ANOVA mixta | modelo lineal mixto |
| Cuantitativa | covariable adicional | ANCOVA | regresión lineal |
| Varias VD cuantitativas | comparación simultánea | MANOVA | modelos separados corregidos |
| Binaria | una proporción frente a un valor | z de una proporción | binomial exacta |
| Binaria | dos proporciones independientes | z de dos proporciones o chi-cuadrado | Fisher exacta |
| Binaria | dos medidas relacionadas | McNemar | modelo logístico mixto |
| Binaria | más de dos medidas relacionadas | Q de Cochran | modelo logístico mixto |
| Categórica | asociación entre dos variables | chi-cuadrado | Fisher según la tabla |
| Ordinal | dos grupos independientes | Mann–Whitney | modelo ordinal |
| Ordinal | dos medidas relacionadas | Wilcoxon | modelo ordinal mixto |
| Ordinal | más de dos grupos independientes | Kruskal–Wallis | modelo ordinal |
| Ordinal | más de dos medidas relacionadas | Friedman | modelo ordinal mixto |
| Dos cuantitativas | asociación lineal | Pearson | regresión lineal |
| Ordinales o relación monótona | asociación | Spearman o Kendall | modelo ordinal |
| Recuento | explicación o predicción | regresión de Poisson | binomial negativa si hay sobredispersión |

---

## 10. Secuencia final que debe memorizarse

```mermaid
flowchart TD
    A["1. Formular la pregunta"] --> B["2. Identificar la VD"]
    B --> C["3. Contar VI y modalidades"]
    C --> D["4. Decidir si las medidas son independientes o relacionadas"]
    D --> E["5. Seleccionar la familia de pruebas"]
    E --> F["6. Verificar condiciones"]
    F --> G["7. Ejecutar y calcular tamaño del efecto"]
    G --> H["8. Interpretar p-valor, intervalo y relevancia práctica"]
```

> La prueba correcta es la que corresponde a la pregunta, al tipo de variable y al plan de recogida; no la que produce el p-valor más pequeño.

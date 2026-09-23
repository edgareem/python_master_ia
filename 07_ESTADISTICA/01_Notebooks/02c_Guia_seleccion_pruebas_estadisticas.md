# Guía para seleccionar una prueba estadística

#### Complemento Codex — Estadística inferencial

Esta guía completa el contenido del cuaderno de Estadística II y adapta el diagrama de planes experimentales utilizado en Psicología. Las cruces del diagrama original solo indicaban contenidos no evaluados en L3; aquí se incluyen todas las ramas porque siguen siendo necesarias para elegir correctamente una prueba.

El objetivo no es memorizar una lista de nombres, sino seguir siempre el mismo razonamiento.

---

## 1. La regla fundamental

La prueba estadística no se elige únicamente por el número de grupos. Se elige combinando cinco preguntas:

1. **¿Cuál es la pregunta de investigación?** Estimar, comparar, estudiar una asociación o predecir.
2. **¿Qué tipo de variable es la variable dependiente?** Cuantitativa, binaria, categórica u ordinal.
3. **¿Cuántos grupos, condiciones o momentos se comparan?** Uno, dos o más de dos.
4. **¿Las observaciones son independientes o están relacionadas?**
5. **¿Se cumplen razonablemente las condiciones de la prueba?** Independencia, forma de la distribución, valores extremos y, cuando corresponda, igualdad de varianzas.

> **Idea clave:** el plan de investigación determina qué observaciones están relacionadas. La distribución de los datos, por sí sola, no permite decidir si una prueba debe ser independiente o pareada.

---

## 2. Vocabulario mínimo

- **Variable dependiente (VD):** resultado que se mide. Ejemplos: puntuación de ansiedad, tiempo de reacción, éxito o fracaso.
- **Variable independiente (VI) o factor:** variable que define los grupos o condiciones. Ejemplos: tratamiento, grupo de edad, momento de medición.
- **Modalidades o niveles:** valores posibles de un factor. Por ejemplo, el factor tratamiento puede tener tres niveles: control, terapia A y terapia B.
- **Medidas independientes o intersujetos:** cada persona pertenece a un solo grupo.
- **Medidas repetidas o intrasujetos:** las mismas personas participan en varias condiciones o momentos.
- **Plan mixto:** combina al menos un factor intersujetos y otro intrasujetos.
- **Plan factorial:** contiene dos o más variables independientes y permite estudiar sus efectos principales y sus interacciones.

---

## 3. Primer paso: identificar el tipo de variable dependiente

| Tipo de VD | Ejemplos | Familia habitual de análisis |
|---|---|---|
| Cuantitativa continua | edad, peso, tiempo, puntuación | t, ANOVA, correlación, regresión lineal |
| Binaria | sí/no, éxito/fracaso, recaída/no recaída | proporciones, binomial, chi-cuadrado, Fisher, McNemar, regresión logística |
| Categórica nominal | tipo de diagnóstico, categoría profesional | chi-cuadrado, Fisher, regresión multinomial |
| Ordinal | ítem Likert, nivel bajo/medio/alto | Mann–Whitney, Wilcoxon, Kruskal–Wallis, Friedman, Spearman o modelos ordinales |
| Recuento | número de incidentes o consultas | modelos de Poisson o binomial negativa |

#### Punto de vigilancia sobre las escalas Likert

Un **ítem Likert aislado** es ordinal. Una puntuación compuesta por varios ítems puede tratarse a veces como aproximadamente cuantitativa si su construcción y sus propiedades psicométricas lo justifican. No existe una regla automática válida para todas las escalas.

---

## 4. Selección principal cuando la VD es cuantitativa

### 4.1. Una muestra comparada con un valor de referencia

Ejemplo: comprobar si la puntuación media de una población es diferente de 100.

| Situación | Prueba principal | Alternativa si las condiciones son inadecuadas |
|---|---|---|
| Una media frente a un valor teórico | t de una muestra | Wilcoxon de una muestra o método de remuestreo adecuado |

La hipótesis nula es:

$$H_0:\mu=\mu_0$$

Para una prueba bilateral:

$$H_1:\mu\neq\mu_0$$

Para una prueba unilateral superior:

$$H_1:\mu>\mu_0$$

---

### 4.2. Una VI con dos modalidades

| Plan | Ejemplo | Prueba paramétrica | Alternativa habitual |
|---|---|---|---|
| Dos grupos independientes | terapia A frente a terapia B, con personas distintas | **t de Welch para muestras independientes** | Mann–Whitney |
| Dos medidas relacionadas | ansiedad antes y después en las mismas personas | **t para muestras pareadas** | Wilcoxon de rangos con signo |

#### ¿Por qué recomendar Welch?

El t de Student clásico para grupos independientes supone varianzas iguales. El **t de Welch** no necesita esa igualdad y funciona también correctamente cuando las varianzas son parecidas. Por eso suele ser una opción más segura por defecto.

#### Matiz sobre Mann–Whitney y Wilcoxon

Estas pruebas trabajan con rangos. No deben presentarse simplemente como pruebas que comparan medias. Su interpretación exacta depende de la forma de las distribuciones y de las hipótesis utilizadas.

---

### 4.3. Una VI con más de dos modalidades

| Plan | Ejemplo | Prueba principal | Alternativa habitual |
|---|---|---|---|
| Grupos independientes | control, terapia A y terapia B | ANOVA de un factor; ANOVA de Welch si las varianzas difieren | Kruskal–Wallis |
| Medidas repetidas | medida antes, durante y después | ANOVA de un factor a medidas repetidas | Friedman |

Una ANOVA significativa indica que **al menos una diferencia existe**, pero no identifica automáticamente entre qué grupos. Después se realizan comparaciones post hoc adecuadas:

- **Tukey** después de una ANOVA clásica;
- **Games–Howell** después de una ANOVA de Welch;
- **Dunn con corrección** después de Kruskal–Wallis;
- comparaciones pareadas corregidas después de una ANOVA de medidas repetidas o Friedman.

---

## 5. Planes factoriales: varias variables independientes

Cuando existen dos o más VI, no conviene realizar una serie de pruebas separadas. Una ANOVA factorial permite estudiar:

- el **efecto principal** de cada factor;
- la **interacción** entre los factores.

Una interacción significa que el efecto de una VI cambia según el nivel de otra VI.

| Estatuto de las VI | Plan | Prueba habitual |
|---|---|---|
| Todas intersujetos | factorial a medidas independientes | ANOVA factorial entre sujetos |
| Todas intrasujetos | factorial a medidas repetidas | ANOVA factorial de medidas repetidas |
| Algunas inter y otras intra | plan mixto | ANOVA mixta |

### Ejemplo de interacción

Se estudia el efecto de una terapia según el grupo de edad:

- VI 1: tratamiento, con los niveles control y terapia;
- VI 2: edad, con los niveles jóvenes y adultos;
- VD: puntuación de ansiedad.

Una interacción tratamiento × edad indicaría que la terapia no produce el mismo efecto en ambos grupos de edad.

> En un plan factorial, se interpreta primero la interacción. Si es importante, los efectos principales aislados pueden ocultar diferencias entre condiciones.

### Cuando existe una covariable

Si se añade una variable cuantitativa que se desea controlar, como la puntuación inicial o la edad, puede utilizarse una **ANCOVA** o una **regresión lineal**. No se debe elegir una covariable únicamente porque produzca un resultado más significativo.

---

## 6. Selección cuando la VD es binaria o categórica

### 6.1. Una proporción

Ejemplo: comprobar si la proporción de fumadores es diferente del 30 %.

| Situación | Prueba |
|---|---|
| Una proporción, muestra pequeña o pocos éxitos | prueba binomial exacta |
| Una proporción, aproximación válida con muestra suficiente | prueba z de una proporción |

### 6.2. Dos o más grupos independientes

| Situación | Prueba |
|---|---|
| Dos proporciones independientes | prueba z de dos proporciones o chi-cuadrado en tabla 2 × 2 |
| Dos variables categóricas | chi-cuadrado de independencia |
| Frecuencias esperadas demasiado pequeñas | prueba exacta de Fisher, especialmente en tabla 2 × 2 |
| Efecto de varias variables sobre un resultado sí/no | regresión logística |

La regla de «muestra superior a 30» es demasiado simplificada. Para las aproximaciones basadas en z o chi-cuadrado importan sobre todo los **recuentos esperados** de las categorías, no solamente el tamaño total.

### 6.3. Medidas binarias relacionadas

| Situación | Prueba |
|---|---|
| Sí/no medido antes y después en las mismas personas | McNemar |
| Sí/no medido en más de dos momentos relacionados | Q de Cochran |

Un chi-cuadrado de independencia no es apropiado para datos pareados porque supone observaciones independientes.

---

## 7. Estudiar una asociación entre dos variables

| Variables | Objetivo | Prueba o medida principal |
|---|---|---|
| Dos cuantitativas, relación aproximadamente lineal | asociación lineal | correlación de Pearson |
| Dos cuantitativas u ordinales, relación monótona | asociación por rangos | Spearman |
| Variables ordinales, muestra pequeña o muchos empates | concordancia ordinal | Kendall |
| Dos categóricas | asociación | chi-cuadrado de independencia y tamaño del efecto |

#### Correlación no significa causalidad

Una correlación indica asociación, pero no demuestra que una variable provoque la otra. También deben examinarse el gráfico, los valores extremos y la forma de la relación. Pearson puede ser próximo a cero aunque exista una relación no lineal fuerte.

---

## 8. Árbol de decisión resumido

### Si quieres comparar valores cuantitativos

1. **¿Comparas una muestra con un valor?**
   - Sí → t de una muestra.
2. **¿Comparas dos condiciones?**
   - Personas distintas → t de Welch.
   - Las mismas personas o pares relacionados → t pareada.
3. **¿Comparas más de dos condiciones con una sola VI?**
   - Grupos distintos → ANOVA de un factor o ANOVA de Welch.
   - Mismas personas → ANOVA de medidas repetidas.
4. **¿Tienes varias VI?**
   - Todas intersujetos → ANOVA factorial independiente.
   - Todas intrasujetos → ANOVA factorial repetida.
   - Factores inter e intra → ANOVA mixta.

### Si quieres comparar proporciones o categorías

1. Una proporción frente a un valor → binomial exacta o z de una proporción.
2. Dos proporciones independientes → z de dos proporciones, chi-cuadrado o Fisher.
3. Dos medidas binarias relacionadas → McNemar.
4. Dos variables categóricas → chi-cuadrado de independencia.
5. Varios predictores y una VD binaria → regresión logística.

### Si quieres estudiar una relación

1. Dos variables cuantitativas con relación lineal → Pearson.
2. Variables ordinales o relación monótona → Spearman o Kendall.
3. Dos variables categóricas → chi-cuadrado.

---

## 9. Verificar las condiciones sin aplicar tests mecánicamente

### 9.1. Independencia

Es la condición más importante y depende del plan de recogida. No puede repararse aplicando una prueba de normalidad. Si las mismas personas aparecen varias veces, se necesita un método para medidas repetidas o datos dependientes.

### 9.2. Normalidad

En las pruebas t y ANOVA interesa principalmente la distribución de los **residuos**; en una t pareada interesa la distribución de las **diferencias**. No siempre se exige que cada variable bruta sea perfectamente normal.

Se puede examinar mediante:

- histograma;
- gráfico Q–Q;
- valores extremos;
- test de Shapiro–Wilk como información complementaria.

Con muestras grandes, Shapiro–Wilk puede detectar desviaciones pequeñas sin importancia práctica. Con muestras pequeñas, puede no detectar una desviación relevante. No debe utilizarse como un semáforo automático.

### 9.3. Igualdad de varianzas

Levene o Brown–Forsythe ayudan a estudiar la homogeneidad. Si existen dudas al comparar grupos independientes, se puede utilizar Welch. Decidir entre Student y Welch únicamente en función de un test previo de varianzas añade una decisión innecesaria.

### 9.4. Valores extremos

Un valor extremo puede cambiar una media, una desviación, una correlación o una prueba. Primero se comprueba si es un error; no se elimina solo porque dificulte obtener significación.

---

## 10. Prueba unilateral o bilateral

Una prueba bilateral pregunta si existe una diferencia en cualquier dirección:

$$H_1:\mu\neq\mu_0$$

Una prueba unilateral superior pregunta únicamente si el valor es mayor:

$$H_1:\mu>\mu_0$$

Con un nivel de confianza del 95 %:

$$\alpha=0{,}05$$

En una prueba bilateral, el riesgo se reparte entre las dos colas:

$$\frac{\alpha}{2}=0{,}025$$

En una prueba unilateral, todo el riesgo de 0,05 se coloca en la dirección definida antes de observar los datos.

> No se elige una prueba unilateral después de ver qué dirección siguen los resultados. Si un efecto contrario también sería científicamente importante, se utiliza una prueba bilateral.

---

## 11. Alpha, p-valor, intervalo y tamaño del efecto

- **Alpha** es el umbral fijado antes del análisis.
- El **p-valor** mide la compatibilidad de los datos con $H_0$ según el modelo utilizado.
- El **intervalo de confianza** muestra un rango de valores compatibles con los datos y el procedimiento.
- El **tamaño del efecto** cuantifica la importancia de la diferencia o asociación.

La regla de decisión es:

$$p\text{-valor}<\alpha \Rightarrow \text{rechazar }H_0$$

$$p\text{-valor}\geq\alpha \Rightarrow \text{no rechazar }H_0$$

No rechazar $H_0$ no demuestra que $H_0$ sea verdadera. Puede significar que el efecto es pequeño, que los datos son demasiado variables o que la potencia es insuficiente.

Una buena conclusión informa conjuntamente:

1. la estimación o diferencia observada;
2. su intervalo de confianza;
3. el tamaño del efecto;
4. el p-valor;
5. el tamaño de la muestra y el plan utilizado.

---

## 12. Comparaciones múltiples

Cada prueba adicional aumenta el riesgo de encontrar un resultado significativo por azar. Por ello:

- se define previamente una hipótesis principal;
- después de una ANOVA se usan comparaciones post hoc;
- se aplican correcciones como Holm o Bonferroni cuando corresponda;
- se distinguen análisis confirmatorios y exploratorios.

Realizar muchos tests t separados para sustituir una ANOVA aumenta el riesgo de falsos positivos.

---

## 13. Correspondencia rápida con Python

| Prueba | Función habitual |
|---|---|
| t de una muestra | `scipy.stats.ttest_1samp()` |
| t independiente de Welch | `scipy.stats.ttest_ind(equal_var=False)` |
| t pareada | `scipy.stats.ttest_rel()` |
| Mann–Whitney | `scipy.stats.mannwhitneyu()` |
| Wilcoxon pareada | `scipy.stats.wilcoxon()` |
| ANOVA de un factor | `scipy.stats.f_oneway()` |
| Kruskal–Wallis | `scipy.stats.kruskal()` |
| Friedman | `scipy.stats.friedmanchisquare()` |
| chi-cuadrado | `scipy.stats.chi2_contingency()` |
| Fisher exacta | `scipy.stats.fisher_exact()` |
| binomial exacta | `scipy.stats.binomtest()` |
| z de proporciones | `statsmodels.stats.proportion.proportions_ztest()` |
| McNemar | `statsmodels.stats.contingency_tables.mcnemar()` |
| Pearson | `scipy.stats.pearsonr()` |
| Spearman | `scipy.stats.spearmanr()` |
| Kendall | `scipy.stats.kendalltau()` |
| Shapiro–Wilk | `scipy.stats.shapiro()` |
| Levene | `scipy.stats.levene()` |

Las ANOVA factoriales, mixtas y los modelos de regresión se realizan habitualmente con `statsmodels`, `pingouin` u otras bibliotecas especializadas.

---

## 14. Ejemplos de selección

### Ejemplo 1 — Dos grupos de personas

Se compara la puntuación media de ansiedad entre un grupo control y un grupo que recibió una terapia. Cada persona pertenece a un solo grupo.

- VD: cuantitativa.
- Una VI con dos modalidades.
- Medidas independientes.
- **Elección:** t de Welch para muestras independientes.

### Ejemplo 2 — Antes y después

Se mide la ansiedad de las mismas personas antes y después de una terapia.

- VD: cuantitativa.
- Una VI con dos modalidades temporales.
- Medidas repetidas.
- **Elección:** t pareada; Wilcoxon si una prueba basada en rangos está mejor justificada.

### Ejemplo 3 — Tres terapias

Se comparan tres grupos independientes: control, terapia A y terapia B.

- VD: cuantitativa.
- Una VI con tres modalidades.
- Medidas independientes.
- **Elección:** ANOVA de un factor, ANOVA de Welch o Kruskal–Wallis según las condiciones.

### Ejemplo 4 — Evolución en tres momentos

Las mismas personas son evaluadas antes, durante y después de la intervención.

- VD: cuantitativa.
- Una VI con tres modalidades.
- Medidas repetidas.
- **Elección:** ANOVA de medidas repetidas o Friedman.

### Ejemplo 5 — Grupo y tiempo

Un grupo recibe una terapia y otro sirve de control. Ambos se evalúan antes y después.

- Factor grupo: intersujetos.
- Factor tiempo: intrasujetos.
- Plan mixto.
- **Elección:** ANOVA mixta.
- Pregunta central frecuente: interacción grupo × tiempo.

### Ejemplo 6 — Resultado sí/no

Se compara la proporción de mejoría entre dos grupos independientes.

- VD: binaria.
- Medidas independientes.
- **Elección:** z de dos proporciones o chi-cuadrado; Fisher si los recuentos son pequeños.

### Ejemplo 7 — Mejoría antes y después

Se registra sí/no en las mismas personas antes y después.

- VD: binaria.
- Medidas relacionadas.
- **Elección:** McNemar, no chi-cuadrado de independencia.

---

## 15. Checklist final

Antes de ejecutar una prueba, completa esta ficha:

1. **Pregunta principal:** ______________________________________
2. **Variable dependiente y tipo:** ______________________________
3. **Variables independientes y niveles:** _______________________
4. **Número de grupos o momentos:** ______________________________
5. **Observaciones independientes o relacionadas:** ______________
6. **Prueba seleccionada:** _____________________________________
7. **Hipótesis $H_0$ y $H_1$:** _________________________________
8. **Bilateral o unilateral, y por qué:** _________________________
9. **Condiciones examinadas:** __________________________________
10. **Tamaño del efecto e intervalo que se informarán:** __________
11. **Corrección por comparaciones múltiples:** ___________________
12. **Interpretación práctica esperada:** _________________________

---

## Conclusión

El diagrama de Psicología es correcto para seleccionar pruebas en diseños experimentales con una VD cuantitativa: una o varias VI, medidas independientes, repetidas o mixtas. Sin embargo, debe completarse con el tipo de variable dependiente, las pruebas para proporciones y categorías, las asociaciones, las condiciones de aplicación y el tamaño del efecto.

La secuencia correcta es siempre:

**pregunta → tipo de VD → número de factores y modalidades → independencia o repetición → condiciones → prueba → tamaño del efecto e interpretación.**

Elegir correctamente la prueba no consiste en buscar la que produzca el p-valor más pequeño, sino la que corresponde al diseño y a la pregunta definidos antes de analizar los datos.

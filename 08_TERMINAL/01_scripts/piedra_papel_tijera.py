
# GUÍA PARA PRINCIPIANTES: PIEDRA, PAPEL O TIJERA
# Abre una terminal en esta carpeta y ejecuta: python piedra_papel_tijera.py
# Se juegan 10 rondas. Cada victoria suma un punto y los empates no suman.
# Piedra gana a tijera; tijera gana a papel; papel gana a piedra.
#
# Los comentarios empiezan por # y Python no los ejecuta.
# import carga un módulo (un conjunto de herramientas). random viene incluido
# en Python y permite hacer elecciones al azar.
import random

# def define una función: un bloque de instrucciones con un nombre.
# Su contenido se ejecuta al llamarla con jugador(), no al definirla.
# Los dos puntos abren el bloque y la sangría indica qué líneas contiene.
def jugador():
    # input muestra la pregunta y espera una respuesta seguida de Enter.
    # Devuelve texto (str), incluso si escribimos un número.
    # \n introduce un salto de línea. = guarda el resultado en una variable.
    respuesta = input('\n ¿Qué jugada eliges (1: Piedra, 2: Papel, 3: Tijera)?: ')
    # int convierte un texto como '2' en el entero 2.
    # return termina la función y devuelve el valor a quien la llamó.
    # Aquí no hay validación: 'hola' provoca un ValueError y detiene el programa.
    # Para jugar correctamente, introduce 1, 2 o 3.
    return int(respuesta)

def ordenador():
    # Una lista [...] agrupa valores ordenados, separados por comas.
    # Las palabras entre comillas son cadenas de texto.
    opciones = ['piedra','papel','tijera']
    # El punto accede a choice, que elige un elemento de la lista al azar.
    opcion = random.choice(opciones)
    # Devolvemos texto; jugador() devuelve un entero. Son tipos diferentes.
    # return(opcion) equivale a return opcion: estos paréntesis son opcionales.
    return(opcion)

# Los parámetros entre paréntesis reciben los valores enviados en la llamada.
# Aquí jugador es un entero y ordenador un texto; son nombres locales,
# no las funciones definidas anteriormente.
def compara(jugador,ordenador):
    # None representa la ausencia de valor: todavía no tenemos un resultado.
    ganador = None
    # == compara valores; = asigna un valor. and exige que ambas condiciones
    # sean verdaderas. if comprueba la primera y elif significa «si no, si...».
    # Solo se ejecuta la primera rama verdadera. Aquí cada instrucción corta
    # está en la misma línea que su condición, después de los dos puntos.
    # Las tres primeras ramas cubren las posibilidades al elegir piedra (1).
    if (jugador == 1 and ordenador == 'tijera'): ganador = 'jugador'
    elif (jugador == 1 and ordenador == 'papel'): ganador = 'ordenador'
    elif (jugador == 1 and ordenador == 'piedra'): ganador = 'empate'
    # Papel (2) pierde contra tijera y gana contra piedra.
    elif (jugador == 2 and ordenador == 'tijera'): ganador = 'ordenador'
    elif (jugador == 2 and ordenador == 'papel'): ganador = 'empate'
    elif (jugador == 2 and ordenador == 'piedra'): ganador = 'jugador'
    # Tijera (3) gana contra papel y pierde contra piedra.
    elif (jugador == 3 and ordenador == 'tijera'): ganador = 'empate'
    elif (jugador == 3 and ordenador == 'papel'): ganador = 'jugador'
    elif (jugador == 3 and ordenador == 'piedra'): ganador = 'ordenador'
    # else se ejecuta si ninguna condición se cumple, por ejemplo, al elegir 4.
    # print muestra un mensaje en la terminal.
    else: print('Ha habido algún error')
    # Devolvemos 'jugador', 'ordenador' o 'empate'. Con un número inválido,
    # ganador sigue siendo None; esta función no vuelve a pedir una entrada.
    return(ganador)

# __name__ vale '__main__' cuando ejecutamos este archivo directamente.
# Este if inicia la partida en ese caso. Si importamos el archivo desde otro,
# podremos usar sus funciones sin que empiece automáticamente el juego.
if __name__ == "__main__":
    nombre = input('Cómo te llamas?: ')
    # %s es un marcador de texto: %nombre lo sustituye por el nombre escrito.
    print('Hola %s vamos a echar 10 jugadas. Y el que consiga más puntos gana!' %nombre)

    # Inicializamos a cero dos variables que cuentan los puntos.
    puntos_j = 0
    puntos_o = 0

    # for repite un bloque. range(10) produce 0, 1, ..., 9: diez iteraciones.
    # cada recibe el número de cada vuelta, aunque aquí no lo utilizamos.
    for cada in range(10):
        # Llamamos a ambas funciones y guardamos los valores que devuelven.
        tirada_jugador = jugador()
        tirada_ordenador = ordenador()
        # Enviamos las dos jugadas como argumentos, en el orden de los parámetros.
        ganador = compara(tirada_jugador,tirada_ordenador)
        # Consultamos el resultado para mostrar mensajes y actualizar puntos.
        if ganador == 'jugador':
            print('\n Yo he sacado %s'%tirada_ordenador)
            print('\n Así que esta la has ganado tú!!')
            # += 1 equivale a puntos_j = puntos_j + 1: suma un punto.
            puntos_j += 1
        elif ganador == 'ordenador':
            print('\n Yo he sacado %s'%tirada_ordenador)
            print('\n Así que esta la he ganado yo!!')
            # Si gana el ordenador, solo incrementamos su contador.
            puntos_o += 1
        # Un empate consume una de las diez rondas, pero no suma puntos.
        elif ganador == 'empate':
            print('\n Vaya, yo también he sacado %s'%tirada_ordenador)
            print('\n Así que hemos empatado, venga otra mano')
        # Una entrada numérica inválida también consume la ronda sin sumar.
        else: print('Ha habido algún problema')

    # Al reducir la sangría salimos del for: esto se ejecuta tras las 10 rondas.
    # > significa «mayor que» y < significa «menor que».
    if puntos_j > puntos_o:
        # Guardamos los puntos del ganador para incluirlos en el mensaje.
        puntos_finales = puntos_j
        print('\n HEMOS TERMINADO!!')
        # .format(...) sustituye {} por el valor recibido: es otra forma
        # de insertar datos en un texto, además de %s utilizado antes.
        print('\n El resultado final es que has ganado tú con {} puntos'.format(puntos_finales))
    elif puntos_j < puntos_o:
        puntos_finales = puntos_o
        print('\n El resultado final es que he ganado yo con {} puntos'.format(puntos_finales))
    # Si ningún contador es mayor que el otro, las puntuaciones son iguales.
    else:
        print('\n Pues parece que hemos empatado, así que todos ganamos!')

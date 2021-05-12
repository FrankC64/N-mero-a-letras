"""Este modulo define únicamente una función pública que tiene como proposito
convertir un número que esté entre 1 a 100000000 a una cadena de caracteres.
"""

__lista_de_numeros = [("uno", "ún", "un"), ("dos", "dós"), ("tres", "trés"), 
                    "cuatro", "cinco", ("seis", "séis"), "siete", "ocho", 
                    "nueve", "diez", "once", "doce", "trece", "catorce", 
                    "quince", "veinte", "treinta", "cuarenta", "cincuenta", 
                    "sesenta", "setenta", "ochenta", "noventa", 
                    ("cien", "ciento", "cientos"), "quinientos", "setecientos", 
                    "novecientos"]


__lista_de_conectores = ["dieci", "veinti", "treintai", "cuarentai", 
                        "cincuentai", "sesentai", "setentai", "ochentai", 
                        "noventai", "mil", ("millón", "millones")]



def __desde_mil(n1, conector1, conector2, numero):
    """Esta función es para crear la cadena de texto de un número que esté por
    encima de mil.

    n1: es el número minimo desde el cual se evalúa.
    conector1: se pasa como argumento el prefijo de cuando 'numero' sea menor
    que  n1*2 ya que desde ese rango el prefijo está en singular (a excepción
    de mil).
    conector2: se pasa como argumneto el prefijo de cuando 'numero' sea mayor
    o igual a n1*2 ya que desde ese rango el prefijo está en plural (a
    excepción de mil).
    numero: se pasa como argumento el valor que se utilizará para evaluar
    las diferentes condiciones.
    """
    salida = ""

    if (numero >= n1 and numero < n1*2): 
        salida = conector1
    elif (numero >= n1*2 and numero < n1*10):
        salida_aux = numero_a_letras(int(str(numero)[0]), True)
        salida = salida + " ".join([salida_aux, conector2])
    elif (numero >= n1*10 and numero < n1*100):
        salida_aux = numero_a_letras(int(str(numero)[0:2]), True)
        salida = salida + " ".join([salida_aux, conector2])
    elif (numero >= n1*100):
        salida_aux = numero_a_letras(int(str(numero)[0:3]), True)
        salida = salida + " ".join([salida_aux, conector2])

    return salida

def __es_una_tupla(salida1, salida2, evaluacion):
    """Solo para verificar si un objeto es una tupla"""

    if (type(evaluacion) != type(tuple())):
        return salida1
    else:
        return salida2

def numero_a_letras(numero, un=False):
    """Esta función sirve para la conversión del primer argumento a una
    cadena de texto.

    El segundo argumento siempre será 'False', cambiar su valor puede causar
    que el valor devuelto por esta función sea incorrecto.
    """

    salida = ""

    while (numero > 0):
        if (numero <= 15):

            salida = " ".join(
                        [salida, __es_una_tupla(
                                    __lista_de_numeros[numero-1], 
                                    __lista_de_numeros[numero-1][0], 
                                    __lista_de_numeros[numero-1])])

            numero = 0 # Cierre del bucle

        elif (numero > 15 and numero <= 99):
            """1 devuelve "ún" y 0 devuelve "un", esto es cuando se
            evalúa la condición de si es una tupla."""

            if (numero % 10 == 0):
                salida = " ".join(
                            [salida, __lista_de_numeros[(numero//10)+13]])
                """Esta condición se aplica cuando "numero" es 20, 30, 40, etc.
                13 es "catorce" pero al ser sumado por la divición que se ve,
                da como resultado un número entre 2 y 9, que será el
                desplazamiento para obtener la cadena de texto correcta."""
            elif (numero < 30):
                temp_n = 1 if (numero % 10 == 1 and un) else 0
                
                salida = " ".join(
                    [salida, __lista_de_conectores[(numero//10)-1] 
                    + __es_una_tupla(
                        __lista_de_numeros[(numero%10)-1],
                        __lista_de_numeros[(numero%10)-1][temp_n],
                        __lista_de_numeros[(numero%10)-1])])
            else:
                temp_n = 2 if (numero % 10 == 1 and un) else 0

                print(numero, temp_n)
                salida = " ".join(
                            [salida, 
                            __lista_de_numeros[(numero//10)+13], "y"])
                salida = " ".join(
                            [salida, __es_una_tupla(
                                    __lista_de_numeros[(numero%10)-1], 
                                    __lista_de_numeros[(numero%10)-1][temp_n], 
                                    __lista_de_numeros[(numero%10)-1])])

            numero = 0 # Cierre del bucle

        elif (numero > 99 and numero <= 999):
            if (numero == 100):
                salida = " ".join([salida, __lista_de_numeros[23][0]])
            else:
                if (numero > 100 and numero < 200):
                    salida = " ".join([salida, __lista_de_numeros[23][1]])
                    """Esta condicionar es para poner "ciento" ya que desde el
                    100 al 199 no se usa "cientos"."""
                elif (numero >= 500 and numero <= 599):
                    salida = " ".join([salida, __lista_de_numeros[24]])
                    # condición especial por ser incorrecto cincocientos
                elif (numero >= 700 and numero <= 799):
                    salida = " ".join([salida, __lista_de_numeros[25]])
                    # condición especial por ser incorrecto sietecientos
                elif (numero >= 900):
                    salida = " ".join([salida, __lista_de_numeros[26]])
                    # condición especial por ser incorrecto noventacientos
                else:
                    salida = " ".join(
                                [salida, __es_una_tupla(
                                        __lista_de_numeros[(numero//100)-1], 
                                        __lista_de_numeros[(numero//100)-1][0], 
                                        __lista_de_numeros[(numero//100)-1])])
                    salida = salida + __lista_de_numeros[23][2]
                    # Pega "cientos"

            numero = numero - (numero // 100 * 100)
         
        elif (numero > 999 and numero <= 999999):
            salida = " ".join([
                        salida, __desde_mil(
                                1000, 
                                __lista_de_conectores[9], 
                                __lista_de_conectores[9], 
                                numero)])
            numero = numero - (numero // 1000 * 1000)

        elif (numero > 999999 and numero <= 999999999):
            salida = " ".join(
                        [salida, __desde_mil(
                                1000000, 
                                " ".join(
                                    [__lista_de_numeros[0][2], # un millón
                                    __lista_de_conectores[10][0]]),
                                    __lista_de_conectores[10][1],
                                    numero)])
            numero = numero - (numero // 1000000 * 1000000)

        elif (numero > 100000000):
            return "Número fuera de rango"

    return salida.strip(' ').rstrip(' ')

if __name__ == '__main__':
    print(numero_a_letras(1221921))

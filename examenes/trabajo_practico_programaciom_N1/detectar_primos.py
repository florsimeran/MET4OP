# Falta ver si la podemos hacer más rápida

# Falta que quede todo metido en la función ¿Tengo que meter el diccionario en la función?

diccionario_primos = {1: 2}

def encontrar_primo(numero_ingresado):
    '''Se ingresa un número como parámetro y la función devuelve el numero primo ubicado en la posición que se ingresó'''

    numero_ingresado = int(numero_ingresado)

    if numero_ingresado < 1:
        raise ValueError("El número que ingresó es 0 o es negativo")

    if numero_ingresado in diccionario_primos.keys():
        print(F'El primo número {numero_ingresado} es el {diccionario_primos[numero_ingresado]}')
        return diccionario_primos[numero_ingresado]

    else:

        contador = len(diccionario_primos)

        ultimo_primo = diccionario_primos[contador]

        while contador != numero_ingresado:

            ultimo_primo += 1

            primo = True

            for valor in diccionario_primos.values():
                if ultimo_primo % valor == 0:
                    primo = False
                    break

            if primo == True:
                contador += 1
                diccionario_primos[contador] = ultimo_primo

    print(F'El primo número {numero_ingresado} es el {diccionario_primos[numero_ingresado]}')
    return diccionario_primos[numero_ingresado]

primo_numero_x = encontrar_primo(input("Por favor ingrese un numero entero positivo para saber el numero primo que se encuentra en esa posición: "))
print(primo_numero_x)
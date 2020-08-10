#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1
 
Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

def ej1():
    # Ejercicios de práctica con números

    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
        
    '''
    print("Ingrese numero 1:")
    numero_1 = int(input())
    print("ingrese numero 1:",numero_1)

    print("Ingrese numero 2:")
    numero_2 = int(input())
    print("ingrese numero1:",numero_2)

    if numero_1 > numero_2:
       print(numero_1,'es mayor que',numero_2)
    elif numero_1 < numero_2:
       print(numero_1,'es menor que',numero_2)
    else:
        print(numero_1,'es igual a',numero_2)


def ej2():
# Ejercicios de práctica con números

  '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    
  '''

  print("Ingrese numero1:")
  numero_1 = int(input())
  print("ingrese numero 1:",numero_1)

  print("Ingrese numero 2:")
  numero_2 = int(input())
  print("ingrese numero1:",numero_2)

  print("Ingrese numero 3:")
  numero_3 = int(input())
  print("ingrese numero 3:",numero_3)

  if (numero_1 % 2) == 0:
      print('"numero_1" es par')
  else:
      print('"numero_1" es impar')

  if (numero_2 % 2):
      print('"numero_1" es par')
  elif numero_2 == 0:
      print("El numero es cero")
  else:
      print('"numero_2" es impar')

  if (numero_3 % 3) == 0:
      print('"numero_1" es impar')
  else:
      print('"numero_1" es par')


def ej3():
    # Ejercicios de práctica con números

    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)

    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    

    '''
    print("Ingrese numero 4:")
    numero_4 = int(input())
    print("ingrese numero 4:",numero_4)

    print("Ingrese numero 5:")
    numero_5 = int(input())
    print("ingrese numero 5:",numero_5)

    if (numero_4 >= 0) or (numero_5 >= 0):
        suma = numero_4 + numero_5
        print('La suma entre {} y {} es {}'.format(numero_4, numero_5, suma))

    if (numero_4 >= 0) or (numero_5>= 0):
        resta = numero_4 - numero_5
        print('La resta entre {} y {} es {}'.format(numero_4, numero_5, resta))

    if (numero_4 >= 0) or (numero_5>= 0):
        multiplicacion = numero_4 * numero_5
        print('La multiplicacion entre {} y {} es {}'.format(numero_4, numero_5, multiplicacion))

    if (numero_4 >= 0) or (numero_5>= 0):
        division = numero_4 / numero_5
        print('La division entre {} y {} es {}'.format(numero_4, numero_5, division))

    if (numero_4 >= 0) or (numero_5>= 0):
        exponente = numero_4 ** numero_5
        print('El exponente entre {} y {} es {}'.format(numero_4, numero_5, exponente))
    

def ej4():
    # Ejercicios de práctica con cadenas
    
    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor

  '''
    print('Ingrese palabra 1: ')
    palabra_1 = str(input())
    print('palabra ingresada:', palabra_1)

    print('Ingrese palabra 2:')
    palabra_2 = str(input())
    print('palabra ingresada:', palabra_2)

    print('Ingrese palabra 3:')
    palabra_3 = str(input())
    print('palabra ingresada:', palabra_3)

    if palabra_1 > palabra_2  and palabra_3:
        print('{} es mayor que {}'.format(palabra_1, palabra_2, palabra_3))
    else:
        print('{} es mayor que {}'.format(palabra_2, palabra_1, palabra_3))
    
    
    print('palabra 1:', palabra_1)

    palabra_1_len = len(palabra_1)
    print(palabra_1, 'tiene', palabra_1_len, 'caracteres')

    palabras_=[palabra_1,palabra_2,palabra_3]
    palabras_.sort()
    print (palabras_)



def ej5():
    # Ejercicios de práctica con números
       
    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado  

    '''
    print('Ingrese temperatura 1:')
    temperatura_1 = float(input())
    print('temperatura ingresada:', temperatura_1)

    print('Ingrese temperatura 2:')
    temperatura_2 = float(input())
    print('temperatura ingresada:', temperatura_2)

    print('Ingrese temperatura 3:')
    temperatura_3 = float(input())
    print('temperatura ingresada:', temperatura_3)

    if temperatura_2 < temperatura_1 > temperatura_3:
       print('la temperatura maxima es', temperatura_1)
    elif temperatura_1 < temperatura_2 > temperatura_3:
       print('la temperatura mayor es', temperatura_2)
    elif temperatura_1 < temperatura_3 > temperatura_2:
        print('la temperatura mayor es', temperatura_3)

    if temperatura_1 <= temperatura_2 and temperatura_1 <= temperatura_3:
       print('la temperatura minima es', temperatura_1)
    elif temperatura_2 <= temperatura_1 and temperatura_2 <= temperatura_3:
       print('la temperatura minima es', temperatura_2)
    elif temperatura_3 <= temperatura_1 and temperatura_3 <= temperatura_2:
        print('la temperatura minima es', temperatura_3)

    promedio = (temperatura_1+temperatura_2+temperatura_3)/3
    print('el promedio de las tres temperaturas es:', promedio)

      


if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    ej5()

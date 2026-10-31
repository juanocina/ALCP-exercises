import random
import json
# Ejercicio personal
def suma_mult(lim: int):
    lista = [random.randint(0,lim) for i in range(100)]
    archivo = open('sec.txt', 'w')
    json.dump(lista, archivo)
    archivo.close()
    f1=open('sec.txt', 'rt')
    datos=json.load(f1)
    f1.close()
    n = len(datos)
    aux = 0
    for i in range(n):
        if datos[i] % 3 == 0 or datos[i] % 5 == 0:
             aux += datos[i]
    return aux

#--------------------------------------------------------
#Si escribimos todos los n´umeros naturales menores que 10 que son m´ultiplos de 3 o
#de 5, obtenemos 3, 5, 6 y 9. La suma de esos n´umeros es 23. Calcular la suma de todos los m´ultiplos
#de 3 o 5 menores que 1000.

def ejc_1(n: int):
    suma = 0
    i = 1
    while i < n:
         if i % 3 == 0 or i % 5 == 0:
              suma += i
              i += 1
         else:
              i += 1
    return suma

#--------------------------------------------------------
#Cada t´ermino de la sucesi´on de Fibonacci es la suma de los dos anteriores. Los dos
#primeros t´erminos son 0 y 1, as´ı que la sucesi´on empieza:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, . . .
#Calcular la suma de los n´umeros pares menores que cuatro millones que aparecen entre los t´erminos
#de la sucesi´on de Fibonacci.

def ejc_2(n):
    f1 = 0
    f2 = 1
    suma_pares = 0
    while f2 < n:
         if f2 % 2 == 0:
              suma_pares += f2
              next = f1 + f2
              f1 = f2
              f2 = next
         else:
              next = f1 + f2
              f1 = f2
              f2 = next
    return suma_pares

#--------------------------------------------------------
#Si se ordenan los primos en orden creciente se obtiene 2, 3, 5, 7, 11, 13, . . .. ¿Cu´al es
#el primo que ocupa el lugar 10001 de la sucesi´on?

def ejc_3(n : int):
    num_prim = [2]
    i = 3
    while len(num_prim) < n:
         if all(i % j != 0 for j in num_prim):
             num_prim.append(i)
             i+=1
         else:
             i+=1
    return num_prim[n-1]

#--------------------------------------------------------
#La conjetura de Collatz afirma que si empieza por cualquier n´umero entero n ≥ 1 y
#se lo va cambiando iterativamente de acuerdo con la regla:
#n par −→ n/2
#n impar −→ 3n + 1
#se llega siempre a 1. Verificar que la conjetura es cierta para todo n menor que 1000000 y determinar
#cu´al de esos valores de n produce la cadena m´as larga hasta llegar al 1.


d_cadenas = {1: [1]}
l_cadenas = {1: 0}

def crea_cad(n: int):
    cadena = []
    j = n
    while j not in d_cadenas:
        if j % 2 == 0:
            cadena.append(j)
            j = j//2
        else:
            cadena.append(j)
            j = 3*j + 1
    cadena.extend(d_cadenas[j])
    d_cadenas[n] = cadena
    l_cadenas[n] = len(cadena)


def ejc_4(n: int):
    c = True
    for i in range(1,n):
        crea_cad(i)
        if d_cadenas[i][-1] != 1:
            c = False
    maslargo = max(l_cadenas.items(), key = lambda x: x[1])
    return c, maslargo

#--------------------------------------------------------
#La constante de Champernowne es el n´umero irracional que se obtiene al concatenar
#todos los n´umeros naturales, del siguiente modo:
#0.1234567891011121314151617181920212223 . . .
#Se puede ver que el d´ıgito en la posici´on n´umero 12 despues del punto decimal es 1 (subrayado en la
#linea de arriba). Sea dn el d´ıgito que ocupa el lugar n-´esimo. Calcular
#d1 · d10 · d100 · d1000 · d10000 · d100000 · d1000000.

def ejc_5(n: int):# Usar simepre el 1000000
    k = 1
    i = 0
    cte = ''
    while i < n:
        cte = cte + str(k)
        k += 1
        i = len(cte)
    return int(cte[0])*int(cte[9])*int(cte[99])*int(cte[999])*int(cte[9999])*int(cte[99999])*int(cte[999999])

#--------------------------------------------------------
#Implementar la funci´on cambiar5por3(n) que tome un n´umero entero n y devuelva
#el entero que se obtiene al cambiar cada d´ıgito 5 que aparece en la representaci´on decimal de n por
#un 3. Por ejemplo, la llamada cambiar5por3(-5152) debe devolver -3132.

def ejc_6(n: int):
    num = str(n)
    l = len(num)
    list = [num[j] for j in range(l)]
    for i in range(l):
        if list[i] == '5':
            list[i] = str(3)
    cambio = ''
    for k in range(l):
        cambio = cambio + list[k]
    return int(cambio)

#--------------------------------------------------------
# Implementar la funci´on dia de la semana(d,m,a) que devuelva el d´ıa de la semana
#correspondiente a d´ıa d del mes m del a˜no a. Se puede asumir que la fecha con la que se invoca a
#la funci´on es v´alida y pertenece al calendario gregoriano. La funci´on deber´a devolver 0 para lunes, 1
#para martes, etc.

def ejc_7(d: int, m: int, a: int):#tupla de tres entradas: día/mes/año
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]

    # Enero y febrero se tratan como parte del año anterior,
    # para que el día bisiesto quede al final del "año"
    if m < 3:
        a -= 1

    # 0 = domingo, 1 = lunes, ..., 6 = sábado
    dom0 = (a + a // 4 - a // 100 + a // 400 + t[m - 1] + d) % 7

    # Reajuste para que 0 = lunes, 1 = martes, ..., 6 = domingo
    return (dom0 + 6) % 7
      
#-------Ejc 8--------------------------------------------
#(Atbash, Rot13, Caesar). El criptosistema atbash consiste en cifrar una cadena de
#caracteres, que solo contiene letras del alfabeto ingl´es, cambiando cada letra por la que est´a en la
#posici´on opuesta en el alfabeto, es decir, la "a" cambia por la "z", la "b" por la "y", etc. Implementar
#la funci´on atbash(w) que tome una cadena de caracteres w y la devuelva cifrada. Otra variante de
#este criptosistema, llamada rot13, cambia cada letra por la que est´a 13 posiciones mas adelante en el
#alfabeto (entendido c´ıclicamente). Implementarlo en la funci´on rot13(w). M´as generalmente, podr´ıa
#cambiarse el 13 por un n´umero 0 ≤ k ≤ 25 (la clave secreta) y as´ı tener un poco mas de seguridad
#(cifrado caesar). Implementar esta variaci´on en la funci´on caesar(w,k). ¿Cu´al es la funci´on de
#descifrado?

alf_ing = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
    'z': 26}
alf_ing_reverse = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e',
    6: 'f', 7: 'g', 8: 'h', 9: 'i', 10: 'j',
    11: 'k', 12: 'l', 13: 'm', 14: 'n', 15: 'o',
    16: 'p', 17: 'q', 18: 'r', 19: 's', 20: 't',
    21: 'u', 22: 'v', 23: 'w', 24: 'x', 25: 'y',
    26: 'z'}
def atbash(p: str):
    n = len(p)
    code = ''
    for i in range(n):
        code += alf_ing_reverse[26 + 1 - alf_ing[p[i]]]
    return code   
    
def caesar(p:str, k: int):
    n = len(p)
    code = ''
    for i in range(n):
        c = k + alf_ing[p[i]]
        if c <= 26: 
            code += alf_ing_reverse[c]
        else:
            code += alf_ing_reverse[c - 26]
    return code
    
#-------Ejc 10-------------------------------------------
#Si se ordenan todas la palabras de 4 o menos letras (elegidas del alfabeto ingl´es de
#26 letras) con el orden del diccionario, la primera ser´ıa la "a", la segunda la "aa", y la ´ultima, en la
#posici´on 26+262+263+264, la "zzzz". ¿Cu´al es la palabra en la posici´on 138096? M´as generalmente,
#implementar la funci´on number2word(p,n) que, dados 1 ≤ p ≤ 26 + 262 + · · · + 26n, determine la
#palabra en la posici´on p de entre todas la de n o menos letras. Implementar tambi´en la operaci´on
#inversa, es decir, la funci´on word2number(w,n) que tome una cadena de caracteres w de longitud entre
#1 y n formada solo por letras del alfabeto ingl´es y devuelva su posici´on entre todas las de hasta n
#letras.

alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def Sum(k: int):
    return (26**(k+1)-1)/25

def number2word(p:int,n:int):
    if p > Sum(n):
        return 'Datos incoherentes'
    word = ''
    for i in range(n-1, -1, -1):
        c = (p - 1) // Sum(i)
        word += alfabeto[int(c)]
        p -= c * Sum(i)
        if p == 1:
            break
        p -= 1
    return word

alf_ing = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
    'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
    'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
    'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
    'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
    'z': 25}

def word2number(w: str,n: int):
    if len(w) > n:
        return 'Datos incoherentes'
    num = 0
    for i, letra in enumerate(w):
        num += alf_ing[letra] * Sum(n - i -1) + 1
    return num

#--------------------------------------------------------
#Implementar la funci´on factorizar(n) que toma un n´umero entero positivo n y
#devuelve una lista de pares ordenados de los primos que aparecen en la factorizaci´on de n (en orden
#creciente) y sus correspondientes multiplicidades. Por ejemplo, el resultado de factorizar(1400)
#debe ser [(2,3),(5,2),(7,1)].

def factorizar(n:int):
    factorization = []
    if n <=1:
        return factorization
    else:
        i = 2
        while i*i <= n:
            exp = 0
            while n % i == 0:
                exp += 1
                n = n//i
            if exp != 0:
                factorization.append((i,exp))
            i += 1
        if n > 1:
            factorization.append((n, 1))
    return factorization  

#--------------------------------------------------------
#Un polinomio f = a0 + a1x + · · · + adxd ∈ C[x] puede ser representado en Python3
#por la lista de coeficientes [a 0,a 1,...,a d]. Implementar la funci´on evaluar polinomio(f,t) que
#tome una lista f representando a un polinomio y un n´umero complejo t y que devuelva f(t). Por
#ejemplo, evaluar polinomio([-1.0,1-2j,2.5],1j) deber´ıa devolver (aproximadamente) -1.5+1j.

def ejc_13(pol: list, numc):
    result = 0
    for i in range(len(pol)):
        result += pol[i] * (numc**i)
    return result 

#--------------------------------------------------------
#Hay ocho posibles monedas de euro: las de 1, 2, 5, 10, 20 y 50 c´entimos y las de 1
#y 2 euros. ¿Cu´antas posibilidades hay para la cantidad total de dinero que puede tener una persona
#con exactamente 12 monedas de euro? ¿Cu´al es la menor cantidad de c´entimos (a partir de 12) que
#no pueden pagarse con exactamente 12 monedas de euro?

import itertools

monedas = [1, 2, 5, 10, 20, 50, 100, 200]

def ejc_14(n: int):
    combinaciones = itertools.combinations_with_replacement(monedas, n)
    sum_posibles = set(sum(comb) for comb in combinaciones)
    l = len(sum_posibles)
    cantidad_menor = 12
    while cantidad_menor in sum_posibles:
        cantidad_menor += 1
    return l, cantidad_menor 

#--------------------------------------------------------
#Se tienen inicialmente 100 cajas (colocadas en c´ırculo) con una bola en cada una.
#En cada turno, se extraen todas las bolas de una caja y se las coloca, una a una, en las siguientes
#cajas avanzando en sentido horario. El siguiente turno comienza en la caja donde se coloc´o la ´ultima
#bola del paso anterior. ¿En qu´e turno se repite la configuraci´on inicial por primera vez?

def hacer_mov(l: list[list], pos: int):
    cant = l[pos][1]
    l[pos][1] = 0
    ind_inic = pos
    for i in range(1, cant + 1):
        l[pos + i][1] += 1
        ind_inic = (ind_inic + 1) % 100
    return l, ind_inic

def ejc_15(n: int): #Solo introducir el valor n = 100
    p0 = [[i, 1] for i in range(1, n+1)]
    cont = 0
    paux = p0
    pos = 0
    while True: 
        paux, pos = hacer_mov(paux, pos)
        cont += 1
        if p0 == paux:
            return cont
        
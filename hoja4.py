# HOJA 4

import modular

#Ejercicio 1---------------------------------
"""
Demostrar que la sucesi´on de Fibonacci satistace
[fn, fn+1] = [[0,1],[1,1]]^n * [0,1]
y utilizar esa identidad para implementar un algoritmo que calcule eficientemente fk mod N dados
k ≥ 0 y N ≥ 1. ¿Cu´al es la complejidad binaria del algoritmo?
"""
def multiplicar_2x2_mod_N(A, B, N):
    return [
        [
            (A[0][0] * B[0][0] + A[0][1] * B[1][0])%N, # Fila 1 x Columna 1
            (A[0][0] * B[0][1] + A[0][1] * B[1][1])%N  # Fila 1 x Columna 2
        ],
        [
            (A[1][0] * B[0][0] + A[1][1] * B[1][0])%N, # Fila 2 x Columna 1
            (A[1][0] * B[0][1] + A[1][1] * B[1][1])%N  # Fila 2 x Columna 2
        ]
    ]

def pow_mat_2x2_mod_N(A,n,N):
    if n==0:
        return [[1,0],[0,1]]
    if n%2 == 0:
        R = pow_mat_2x2_mod_N(A,n//2,N)
        R = multiplicar_2x2_mod_N(R,R,N)
    else:
        R = pow_mat_2x2_mod_N(A,n-1,N)
        R = multiplicar_2x2_mod_N(A,R,N)
    return R
    
def mat_x_vect(A,v):
    return [(A[0][0]*v[0]+A[0][1]*v[1]), (A[1][0]*v[0]+A[1][1]*v[1])]

A = [[0,1],[1,1]]
def fibo_mod(k:int,N:int):
    P = pow_mat_2x2_mod_N(A,k,N)
    [fk,fk1] = mat_x_vect(P,[0,1])
    return fk

#Ejercicio 2---------------------------------
"""
Sean N1, . . . ,Nk ≥ 1 coprimos y sea N = Qk i=1 Ni. Demostrar que el sistema de
congruencias simult´aneas x ≡ ai (mod Ni) para a1, . . . , ak dados es equivalente a una ´unica congruencia
x ≡ a (mod N) para alg´un a. Implementar este resultado en Python3 como la funci´on
reducir congruencias(l) que toma una lista l = [(a1,N1),(a2,N2),...,(ak,Nk)] de pares ordenados
(tuplas) y devuelve el par (a,N).
"""
def reducir_congruencias(l):
    n = len(l)
    y = [l[0][0],l[1][0]]
    M1,M2 = l[0][1],l[1][1]
    x = modular.gamma_inversa_eficiente(y,M1,M2)
    N = M1*M2
    print(x,N)
    for i in range(2,n):
        y = [x,l[i][0]]
        P = l[i][1]
        x = modular.gamma_inversa_eficiente(y,N,P)
        N = N * P
        print(x,N)
    return x,N   

#Ejercicio 3---------------------------------
import gcds
import modular
#Ejercicio 4--------------------
"""
Mostrar que φ(100) = 40. De acuerdo con el teorema de Euler-Fermat se tiene que
a40 ≡ 1 (mod 100) para cualquier a coprimo con 100. Escribir un programa en Python3 que verifique
esa afirmaci´on. Calcular la estructura del grupo (Z/100Z)∗ determinando manualmente la estructura
de (Z/4Z)∗ y (Z/25Z)∗. Demostrar que a20 ≡ 1 (mod 100) para todo a coprimo con 100 y modificar
el programa anterior para verficar esta nueva afirmaci´on.
"""
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

def phi_euler(n:int):
    fact = factorizar(n)
    a = len(fact)
    if n == 1:
        return 1
    result = 1
    for i in range(a):
        p = fact[i][0]
        exp = fact[i][1]
        phi_i = (p**exp) - (p**(exp-1))
        result = result * phi_i
    return result
    
def ejc_4():
    print(phi_euler(100) == 40)
    unidades = []
    for i in range(100):
        if (gcds.gcd_binario_tail_rec(i,100))==1:
            unidades.append(i)
    print((unidades, len(unidades)))
    for i in range(len(unidades)):
        resp = True
        pot_mod = modular.potencia_mod(unidades[i], 40, 100)
        if pot_mod != 1:
            resp = False
    for i in range(len(unidades)):
        pot_mod = modular.potencia_mod(unidades[i], 20, 100)
        if pot_mod != 1:
            resp = False
    print(resp)
    
#Ejercicio 5--------------------
"""
Calcular (a mano) el resto de dividir 1010000000 por 2 · 3 · 5 · 7 · 11 · 13 y luego
verificarlo haciendo (10 ** 10000000) % (2*3*5*7*11*13) en Python3. Comparar la velocidad de
esta instrucci´on con potencia mod(10, 10000000, 2*3*5*7*11*13).
"""
import time
def ejc_5():   
    inicio = time.perf_counter()
    r1 = (10*10000000)%(2*3*5*7*11*13)
    t1 = time.perf_counter() - inicio
    
    inicio = time.perf_counter()
    r2 = modular.potencia_mod(10, 10000000, 2*3*5*7*11*13)
    t2 = time.perf_counter() - inicio
    
    print("Método 1:", r1, f"-> {t1:.8f} s")
    print("Método 2:", r2, f"-> {t2:.8f} s")
    print(f"El método 2 es ~{t1 / t2:,.0f} veces más rápido")
    
#Ejercicio 6--------------------
"""
Un entero N ≥ 2 se dice pseudoprimo de Fermat en base a, para a ∈ Z coprimo
con N, si aN−1 ≡ 1 (mod N). Se dice que N es pseudoprimo de Fermat fuerte si es pseudoprimo en
cualquier base a coprimo con N. El teorema de Euler-Fermat muestra que todo primo es pseudoprimo
de Fermat fuerte, pero lamentablemente la rec´ıproca no es cierta. Los n´umeros compuestos N ≥ 2
que son pseudoprimos de Fermat fuertes se llaman n´umeros de Carmichael. Escribir un programa en
Python3 que determine los 10 primeros n´umeros de Carmichael.
"""
def es_primo(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def es_carmichael(n):
    if n < 2 or es_primo(n):
        return False
    return all(modular.potencia_mod(a, n - 1, n) == 1 for a in range(1, n) if gcds.gcd_binario_tail_rec(a,n) == 1)

def carmichael_10_primeros():
    carmichael = []
    n = 2
    while len(carmichael) < 10:
        if es_carmichael(n):
            carmichael.append(n)
        n += 1

    print(carmichael)

#Ejercicio 7--------------------     
"""
Implementar la funci´on menor raiz primitiva(p) que obtenga la menor ra´ız primitiva
1 ≤ a ≤ p − 1 para un primo p dado.
"""
def divisores(n):
    div = []
    for i in range(2,(n//2+1)):
        if n % i == 0:
            div.append(i)
    return div

def menor_raiz_primitiva(p):
    unidades = [i for i in range(1,p)]
    div = divisores(p-1)
    print(div)
    for i in range(2,p):
        if all((modular.potencia_mod(i,j,p) != 1) for j in div):
            return i

#Ejercicio 12--------------------   
"""
Mostrar, con la ayuda de Python3, que N = 3 · 2189 + 1 es primo utilizando el test
de primalidad de Lucas. Para cada p ∈ {2, 3}, determinar la cantidad de enteros 1 ≤ a < N tales
que a(N−1)/p ̸≡ 1 (mod N). ¿Es posible encontrar a tal que a(N−1)/2 ̸≡ 1 (mod N) y a(N−1)/3 ̸≡ 1
(mod N)?
"""
"""
A continuación las líneas de código para el ejc 12

>>> N = 3*(2**189) + 1
>>> import random
>>> a = random.randint(1, N)
>>> a
1634492502257618333535594645624424087891571885518548732296
>>> modular.potencia_mod(a,N-1,N)
1
>>> modular.potencia_mod(a,N-1//2,N)
1634492502257618333535594645624424087891571885518548732296
>>> modular.potencia_mod(a,N-1//3,N)
1634492502257618333535594645624424087891571885518548732296

# Vemos que cunple las hipótesis del Test de primalidad de Lucas => N es primo # 
"""
#Ejercicio 14--------------------
"""
¿Cu´antas soluciones (x, y) ∈ Z/pZ tiene la ecuaci´on y2 ≡ x3 + 7 (mod p) para un
primo p ≡ 2 (mod 3)? Modificar el programa curva eliptica mod13.py del tema #1 para comprobarlo
para los primeros 100 primos.
"""
# este programa obtiene la lista de puntos (x,y)
# que satisfacen 0<=x,y <13 y 13|y^2-x^3 -7.
def soluciones_mod_p(p):
    if (p-2)%3 != 0:
        return "Entrada no válida, p-2 debe ser multiplo de 3"
    puntos = [] # empezamos con la lista vac´ıa
    x = 0 # bucle con x=0 ,1 ,... ,12
    while x < p:
        y = 0 # bucle con y=0 ,1 ,... ,12
        while y < p:
            if (y**2 -x **3 -7)%p == 0: # si el punto cumple la condici ´on
                puntos += [(x,y)] # lo agregamos a la lista
            y += 1
        x += 1
    return puntos
    
#Ejercicio 15--------------------
"""
Utilizar el criterio de Korselt para probar que si 6k+1, 12k+1 y 18k+1 son primos
(para un cierto entero k ≥ 1), entonces N = (6k + 1)(12k + 1)(18k + 1) es un n´umero de Carmichael.
Escribir un programa en Python3 para encontrar los primeros 5 n´umeros de Carmichael de esta forma.
"""
import sympy
from sympy import isprime
def carmichael_5():
    carmichael = []
    k = 1
    while len(carmichael) < 5:
        if isprime(6*k + 1) and isprime(12*k + 1) and isprime(18*k + 1):
            N = (6*k + 1)*(12*k + 1)*(18*k + 1)
            carmichael.append(N)
        k += 1
    return carmichael

#Ejercicio 16--------------------   
"""
Utilizar el m´etodo p − 1 de Pollard para factorizar
N = 1533639298078728959641946066766007559698078324136928757330809029848359733271767
utilizando B = 50. ¿C´omo se puede calcular gcd(aβ − 1,N) de forma eficiente?
9
"""
from math import gcd, isqrt, factorial
import random

N = 1533639298078728959641946066766007559698078324136928757330809029848359733271767
B = 50
a = random.randint(1,N)
"""
def primes_upto(n):
    primos = []
    for p in range(2, n + 1):
        es_primo = True
        for d in range(2, isqrt(p) + 1):
            if p % d == 0:
                es_primo = False
                break          # ya sabemos que no es primo, paramos
        if es_primo:
            primos.append(p)
    return primos

def log_sup(p, N):# Calcula el logaritmo (base p) de N redondeado hacia arriba.
    log, t = 0, 1
    while t < N:
        t *= p; log += 1
    return log

beta = 1
for p in primes_upto(B):
    beta *= p ** log_sup(p, N)

def pollard(N, beta, a):
    x = gcd(a, N)
    if x != 1:                    # caso x != 1: ya tenemos un factor
        return x
    return gcd(pow(a, beta, N) - 1, N)   # y = gcd(a^beta - 1, N)
"""


def pollard(N,B):
    x = random.randint(1,B)
    if gcds.gcd_binario_tail_rec(x,N) != 1:
        return x
    for k in range(2, B + 1):
        x = pow(x, k, N)
        d = gcd(x - 1, N) 
        if 1<d<N:
            return d, N//d
            

#-------tortu
import math
n = 1473
def f(x):
    return (x**2+1) % n

def tortu_liebre(n):
    x1 = random.randint(1,n)
    tortu = x1
    liebre = x1
    while True:
        tortu = f(tortu)
        liebre = f(f(liebre))
        x = math.gcd(tortu - liebre, n)
        if x != 1:
            return x
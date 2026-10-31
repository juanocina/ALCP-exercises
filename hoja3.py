#---------- HOJA 3 ---------------------------------
import natural
#Ejercicio 1----------------------------------------
"""
Implementar la funci´on div2(a) que calcule los d´ıgitos de ⌊a/2⌋, es decir, que se
comporte como la operaci´on a//2 de Python3 pero utilizando la representaci´on de listas de d´ıgitos
“reducidas”. Utilizar esa funci´on para implementar la funci´on decimal a base2(a) que devuelve la
representaci´on binaria de a (una lista de ceros y unos). Calcular la complejidad binaria de ambas
funciones.
"""
def div2(a:list):
    if a == []:
        return ([],0)
    n = len(a)
    cociente = [0] * n
    acarreo = 0
    for i in range(n-1,-1,-1):
        y = a[i] + acarreo*10
        cociente[i] = y//2
        acarreo = y%2
    natural.remover_ceros(cociente)
    return (cociente,acarreo)
    
#La complejidad binaria de div2(a) es O(n)

def binario(a:list):
    if a == [1]:
        return a
    n = len(a)
    bin = []
    (coci,acarreo) = div2(a)
    while coci != [1]:
        bin.append(acarreo)
        (coci,acarreo) = div2(coci)
    bin.append(acarreo)
    bin.append(1)
    return bin
      
#La complejidad binaria de binario(a) es O(n^2)

#Ejercicio 2---------------------------------------- 
"""
Implementar la funci´on base2 a decimal(b) que obtenga la lista de d´ıgitos decimales
de un n´umero a partir de la lista de sus bits. Calcular la complejidad binaria de esta funci´on.
"""
def hacer_decimal(n:int):
    num = []
    while n != 0:
        r = n%10
        num.append(r)
        n = n // 10 
    return num

def base2_a_decimal(b:list):
    n = len(b)
    suma = []
    for i in range(n):
        c = 2**(i) * b[i]
        num = hacer_decimal(c)
        suma = natural.sumar(suma,num)
    return suma

# base2_a_decimal es de una complejidad binaria de O(n^3) 

#Ejercicios (3-7)----------------------------------------   
#No son de programar, menos el 6,7 pero no tienen mucha gracia.

#Ejercicio 8----------------------------------------
"""
Implementar la funci´on raiz cuadrada(x) que dado un entero (no negativo) calcule
su ra´ız cuadrada ⌊
√
x⌋, utilizando una b´usqueda binaria o bien obteniendo d´ıgito por d´ıgito del resultado.
Tanto la entrada como la salida del algoritmo ser´an listas de d´ıgitos. ¿Cu´al es la complejidad
binaria del m´etodo? Generalizar a la funci´on raiz k esima(x,k) que calcula ⌊ k
√
x⌋, donde x es una
lista de d´ıgitos y k ≥ 1 un entero.
"""
def raiz_cuadrada(a:list):
    iz = []
    dr = natural.sumar(a,[1])
    while natural.comparar(iz,natural.restar(dr,[1])) == (-1):
        med = div2(natural.sumar(iz,dr))[0]
        if natural.comparar(natural.multiplicar_karatsuba(med,med),a) == 1:
            dr = med
        else:
            iz = med
    return iz
    
#Ejercicio 9----------------------------------------
"""
Incorporar las mejoras indicadas arriba a la funci´on division y resto(a,b). Comparar
los tiempos reales de ejecuci´on de ambas versiones.
"""
def divf(a:list,f:int):
    if a == []:
        return ([],0)
    n = len(a)
    cociente = [0] * n
    acarreo = 0
    for i in range(n-1,-1,-1):
        y = a[i] + acarreo*10
        cociente[i] = y//f
        acarreo = y%f
    natural.remover_ceros(cociente)
    return cociente

def division_normalizada(a,b):
    m = len(b)
    f = 10//(b[m-1]+1)
    a1 = natural.multiplicar(a,[f])
    b1 = natural.multiplicar(b,[f])
    q,r = natural.division_y_resto(a1,b1)
    return q,divf(r,f)

#Ejercicio 12---------------------------------------
"""
Calcular los primeros mil d´ıgitos de √2 despu´es del punto decimal, utilizando la
iteraci´on de Newton con la funci´on f(x) = x2 − 2.
"""
def calcular_raiz_2_newton(digitos):
    N = 2 * (10 ** (2 * digitos))
    
    # CORRECCIÓN: Empezar con un número garantizadamente mayor a la raíz (2.0 en vez de 1.0)
    x = 2 * (10 ** digitos)
    
    while True:
        x_siguiente = (x + N // x) // 2
        
        # Ahora la sucesión siempre decrecerá hasta estabilizarse en la raíz
        if x_siguiente >= x:
            break
            
        x = x_siguiente
    num = str(x)
    cifras_decimales = num[1:]
    return cifras_decimales
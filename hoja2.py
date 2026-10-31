#Ejercicio 1-----------------------------------------
"""
Demostrar que para cualquier par de enteros (x, y) ̸= (0, 0), existen a, b ∈ Z tales
que ax + by = gcd(x, y). Implementar una funci´on gcd extendido binario(x,y), basado en la idea
de gcd binario, que no solo devuelva el m´aximo com´un divisor, sino que tambi´en devuelva a y b.
"""
def gcd_extendido_binario(x, y):
    """Devuelve (g, a, b) con g = gcd(x,y) y a*x + b*y = g.  (x,y) != (0,0)"""
    sx = -1 if x < 0 else 1
    sy = -1 if y < 0 else 1
    g, a, b = _gcd_ext_bin(abs(x), abs(y))
    return g, sx * a, sy * b


def _gcd_ext_bin(x, y):          # x, y >= 0, no ambos nulos
    xespar = x % 2 == 0
    yespar = y % 2 == 0

    if x == 0:                   # caso base: gcd(0,y) = y
        return y, 0, 1
    elif y == 0:                 # caso base: gcd(x,0) = x
        return x, 1, 0

    elif xespar and yespar:      # caso 1
        g, a, b = _gcd_ext_bin(x // 2, y // 2)
        return 2 * g, a, b

    elif xespar:                 # caso 2
        g, a, b = _gcd_ext_bin(x // 2, y)
        if a % 2 == 0:
            return g, a // 2, b
        return g, (a + y) // 2, b - x // 2

    elif yespar:                 # caso 3
        g, a, b = _gcd_ext_bin(x, y // 2)
        if b % 2 == 0:
            return g, a, b // 2
        return g, a - y // 2, (b + x) // 2

    elif x > y:                  # caso 4: gcd(y, (x-y)/2) = a'*y + b'*(x-y)/2
        g, a, b = _gcd_ext_bin(y, (x - y) // 2)
        if b % 2 == 0:
            return g, b // 2, a - b // 2
        u, v = b, 2 * a - b
        return g, (u + y) // 2, (v - x) // 2

    else:                        # caso 5: gcd(x, (y-x)/2) = a'*x + b'*(y-x)/2
        g, a, b = _gcd_ext_bin(x, (y - x) // 2)
        if b % 2 == 0:
            return g, a - b // 2, b // 2
        u, v = 2 * a - b, b
        return g, (u + y) // 2, (v - x) // 2
    
#Ejercicio 2-----------------------------------------
"""
El m´etodo cl´asico para calcular el m´aximo com´un divisor se llama algoritmo de
Euclides y est´a basado en la identidad gcd(x, y) = gcd(y, x mod y), donde x mod y es el resto de dividir
x por y. Demostrar que la identidad es correcta, e implementar el correspondiente algoritmo recursivo
gcd euclides(x,y) identificando cu´ales son los casos base. Comparar la complejidad aritm´etica de
este algoritmo con gcd binario(x,y). Por ´ultimo, extender el algoritmo a uno que obtenga tambi´en
a y b como en el problema 2.1
"""
def gcd_euclides(x:int, y:int):
    x = abs( x )
    y = abs( y )
    if y > x:
        aux = x
        x = y
        y = aux
    if y == 0:
        return x
    if y == 1:
        return y
    return gcd_euclides(y, x % y)

def gcd_euclides_2(x:int,y:int):
    cambio = False
    if y > x:
        aux = x
        x = y
        y = aux
        cambio = True
    if y == 0:
        return x,1,0
    m,a1,b1 = gcd_euclides_2(y,x%y)
    a = b1
    b = a1 - (x//y)*b1
    if cambio:
        aux=a
        a=b
        b=aux
    return m,a,b

#Ejercicio 3-----------------------------------------
"""
Implementar una funci´on es suma de k potencias n(x,k,n) que decida si un entero
x ≥ 0 se puede escribir como xn1 + xn2 + · · · + xnk para ciertos enteros x1, . . . , xk ≥ 0. La funci´on debe
devolver un valor booleano.
"""
def es_suma_de_k_potencias_n(x:int,k:int,n:int):
    if k == 0:
        return x==0
    if x < 0:
        return False
    i = 0
    while i**n <= x:
        i += 1
    limite = i - 1
    for base in range(limite,-1,-1):
        pot = base**n
        if es_suma_de_k_potencias_n(x-pot, k-1,n):
            return True
    return False

#Ejercicio 4-----------------------------------------
"""
Considerar el siguiente juego de dos jugadores: partiendo de una pila de n piedras,
los jugadores van (uno tras otro) quitando 1, 2, 6 o 98 piedras de la pila a su elecci´on, hasta que el
que quita la ´ultima pierde. Implementar un algoritmo recursivo hay estrategia ganadora(n) que
determine si, partiendo de una pila de n piedras, el jugador que empieza tiene estrategia ganadora.
"""
memoria = {}

def ganar_juego_piedras(n:int):
    if n in memoria:
        resp = memoria[n]
    if n == 1:
        resp = False
    elif n == 2:
        resp = True
    elif n>=3 and n<=5:
        resp = not(ganar_juego_piedras(n-1) and ganar_juego_piedras(n-2))
    elif n == 6:
        resp = True
    elif n>=7 and n<=98:
        resp = not(ganar_juego_piedras(n-1) and ganar_juego_piedras(n-2) and ganar_juego_piedras(n-6))
    #elif n == 98:
        #resp = 
    memoria[n] = resp
    return resp
 
#Ejercicio 5-----------------------------------------
"""
Implementar una funci´on contar palabras(n) que calcule cu´antas palabras hay de
longitud n ≥ 1 que utilizan solamente las letras a y b y que no tienen tres a consecutivas.
"""
memc0 = {}
memc1 = {}
memc2 = {}

def c0(n:int):
    if n in memc0:
        return memc0[n]
    if n == 1:
        return 1
    memc0[n] = c0(n-1)+c1(n-1)+c2(n-1)
    return c0(n-1)+c1(n-1)+c2(n-1)

def c1(n:int):
    if n in memc1:
        return memc1[n]
    if n == 1:
        return 1
    memc1[n] = c0(n-1)
    return c0(n-1)

def c2(n:int):
    if n in memc2:
        return memc2[n]
    if n == 1:
        return 0
    memc2[n] = c1(n-1)
    return c1(n-1)
    
def contar_palabras_sin_tres_aes_seguidas(n:int):
    return c0(n)+c1(n)+c2(n)
    
#Ejercicio 6-----------------------------------------
"""
(Egg dropping problem). Consideremos un edificio de n ≥ 1 plantas y k ≥ 1 huevos
ideales con la siguiente propiedad: si se deja caer uno de estos huevos desde la planta m o superior,
el huevo se rompe, pero si se lo deja caer desde una planta inferior a la m, el huevo queda intacto. El
valor de m ∈ [1, n + 1] es el mismo para todos los huevos. Se pretende determinar el valor exacto de
m utilizando los k huevos. Si se utiliza la estrategia ´optima, ¿cu´al es la m´ınima cantidad de veces que
debe lanzar el huevo para conseguir esto? Implementar la funci´on egg drop(n,k) que lo determine.
Por ejemplo, si solo disponemos de k = 1 huevo, la ´unica opci´on es lanzarlo desde todos los pisos,
empezando desde mas abajo. La primer planta desde la que se rompa, ser´a el valor de m buscado. Si
no se rompe desde ninguna planta, ser´a m = n + 1. En el peor caso, necesitariamos n lanzamientos,
y por lo tanto egg drop(n,1) devolver´a n.
"""
def egg_drop(n, k): #No lo he entendido, la solución por lo tanto es de Gemini.
    # Crear una tabla 2D DP donde dp[i][j] representará 
    # el mínimo número de lanzamientos para i huevos y j plantas.
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    
    # Caso base 1: Si tenemos 1 planta o 0 plantas
    for i in range(1, k + 1):
        dp[i][0] = 0
        dp[i][1] = 1
        
    # Caso base 2: Si solo tenemos 1 huevo, necesitamos j lanzamientos
    for j in range(1, n + 1):
        dp[1][j] = j
        
    # Rellenar el resto de la tabla usando la relación de recurrencia
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            dp[i][j] = float('inf')
            
            # Probar lanzando el huevo desde cada planta x entre 1 y j
            for x in range(1, j + 1):
                # 1 + max(se rompe, no se rompe)
                res = 1 + max(dp[i - 1][x - 1], dp[i][j - x])
                
                # Minimizar el peor de los casos
                if res < dp[i][j]:
                    dp[i][j] = res
                    
    return dp[k][n]
    
#Ejercicio 7-----------------------------------------
"""
La forma m´as simple de multiplicar dos matrices A de m × n y B de n × k requiere
hacer m · n · k multiplicaciones de n´umeros y una cantidad similar de sumas. Si se tienen varias
matrices A1,A2, . . . ,Ak de tama˜nos n0 × n1, n1 × n2, . . . , nk−1 × nk, el producto A1 · A2 · · ·Ak puede
calcularse de varios modos (por la propiedad asociativa del producto de matrices), pero no siempre con
el mismo coste computacional. Implementar la funci´on optimal mat mul(tam) que tome una tupla de
enteros positivos tam=(n0, n1, ..., nk) y determine cuantas operaciones de multiplicaci´on requiere
la estrategia ´optima para multiplicar las matrices.
Caso particular de prueba: optimal mat mul((a,b,c,d)) dar´a el m´ınimo entre abc + acd y
bcd+abd. El primer valor corresponde con el coste de hacer (A0 ·A1) ·A2 y el otro el de A0 · (A1 ·A2).
"""
def optimal_mat_mult(tam:tuple):
    k = len(tam) - 1
    dp = [[0 for p in range(k+1)]for p in range(k+1)]
    for l in range(2,k+1):
        for i in range(1, k-l+2):
            j = i + l - 1
            dp[i][j] = float('inf')
            for m in range(i,j):
                q = dp[i][m] + dp[m+1][j] + (tam[i-1]*tam[m]*tam[j])
                if q < dp[i][j]:
                    dp[i][j] = q
    return dp[1][k]
                
#Ejercicio 8-----------------------------------------  
"""
(Pots of Gold). En este famoso juego, dos jugadores van alternadamente llevandose
pilas de oro, con el objetivo de obtener al final la mayor cantidad de oro posible. Las pilas de oro
est´an dispuestas en una fila horizontal, y los jugadores en su turno solo pueden elegir de entre las dos
pilas que est´an en los extremos de la fila. Digamos que hay k ≥ 1 pilas de oro y que las cantidades en
gramos de oro de cada pila est´an en una lista l = [l1, l2, ..., lk] de enteros. Escribir una funci´on
max gold(l) que devuelva la m´axima cantidad de oro que puede llevarse el jugador que empieza si
este utiliza la estrategia ´optima.
"""
def ganar_partida():
    a1 = open('max_gold.txt','rt') #Cambiar para leer la partida que se quiera jugar.
    partida = a1.readlines()
    a1.close()
    partida = [linea.strip() for linea in partida]
    partida = [int(x) for x in partida]
    return max_gold(partida)

memoria = {}
def max_gold_v2(l:list, i:int, j:int, memoria:dict):
    if (i,j) in memoria:
        return memoria[(i,j)]
    n = j - i + 1
    if n == 1:
        resp = l[i]
    else:
        suma = 0
        for k in range(i,j+1):
            suma += l[k]
        opc1 = suma - max_gold_v2(l,i+1,j,memoria)
        opc2 = suma - max_gold_v2(l,i,j-1,memoria)
        resp = max(opc1,opc2)
    memoria[(i,j)] = resp
    return resp

def max_gold(l:list):
    memoria = {}
    return max_gold_v2(l,0,len(l)-1,memoria)
    
#Ejercicio 9-----------------------------------------
"""
Se tiene un tablero de n × m con un n´umero entero en cada casilla. Una ficha se
encuentra inicialmente en la casilla de arriba a la izquierda del tablero. En cada movimiento se puede
desplazar a esta ficha una casilla hacia abajo o una hacia la derecha. El objetivo es llegar a la casilla
de abajo a la derecha de modo que la suma de los n´umeros de las casillas visitadas sea m´ınimo.
Implementar una funci´on min suma casillas(n,m,a) que tome una matriz a (una lista de n listas de
m enteros) y que devuelva la suma m´ınima de los n´umeros visitados en el camino ´optimo.
"""
def min_suma_casillas(n:int,m:int,a:list[list]):
    if n == 0 and m == 0:
        return 0
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = a[0][0]
    for j in range(1,m):#Definir movimiento lateral
        dp[0][j] = dp[0][j-1] + a[0][j]
    for i in range(1,n):#Definir movimiento vertical
        dp[i][0] = dp[i-1][0] + a[i][0]
    for i in range(1,n):
        for j in range(1,m):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + a[i][j] #Decidir bajar o ir dcha
    return dp[n-1][m-1]
# Álgebra Computacional · Hojas de ejercicios

Resoluciones en **Python 3** de las hojas de ejercicios de la asignatura de **Álgebra Computacional**. Cada hoja es un único archivo `.py` donde cada ejercicio va precedido de su enunciado (como comentario o docstring) y de su implementación.

Los temas cubiertos van desde el cálculo elemental (sucesiones, primos, criptografía clásica) hasta aritmética de enteros grandes, aritmética modular y algoritmos de factorización y primalidad.

## Contenido

```
.
├── hoja1.py   # Programación básica y problemas tipo Project Euler
├── hoja2.py   # Recursión, MCD y programación dinámica
├── hoja3.py   # Aritmética de números grandes (listas de dígitos)
├── hoja4.py   # Aritmética modular, Carmichael, factorización
└── README.md
```

---

## Hoja 1 · Programación básica

| Ejercicio | Función | Descripción |
|---|---|---|
| Personal | `suma_mult(lim)` | Genera 100 enteros aleatorios, los guarda/lee con `json` y suma los múltiplos de 3 o 5 |
| 1 | `ejc_1(n)` | Suma de los múltiplos de 3 o 5 menores que `n` |
| 2 | `ejc_2(n)` | Suma de los términos pares de Fibonacci menores que `n` |
| 3 | `ejc_3(n)` | El `n`-ésimo número primo |
| 4 | `ejc_4(n)` | Conjetura de Collatz con memoización: verificación y cadena más larga |
| 5 | `ejc_5(n)` | Constante de Champernowne: producto `d1·d10·…·d1000000` |
| 6 | `ejc_6(n)` | `cambiar5por3`: sustituye cada dígito 5 por un 3 |
| 7 | `ejc_7(d, m, a)` | Día de la semana de una fecha (0 = lunes … 6 = domingo) |
| 8 | `atbash(p)`, `caesar(p, k)` | Criptosistemas Atbash y César (Rot13 con `k = 13`) |
| 10 | `number2word(p, n)`, `word2number(w, n)` | Biyección entre palabras de hasta `n` letras y su posición en orden de diccionario |
| 11 | `factorizar(n)` | Factorización en primos: lista de pares `(primo, multiplicidad)` |
| 13 | `ejc_13(pol, numc)` | Evaluación de un polinomio dado por su lista de coeficientes |
| 14 | `ejc_14(n)` | Cantidades posibles con `n` monedas de euro |
| 15 | `ejc_15(n)` | Problema de las 100 cajas con bolas: turno en el que se repite la configuración inicial |

## Hoja 2 · Recursión y programación dinámica

| Ejercicio | Función | Descripción |
|---|---|---|
| 1 | `gcd_extendido_binario(x, y)` | MCD binario extendido: devuelve `(g, a, b)` con `ax + by = g` |
| 2 | `gcd_euclides(x, y)`, `gcd_euclides_2(x, y)` | Algoritmo de Euclides y su versión extendida |
| 3 | `es_suma_de_k_potencias_n(x, k, n)` | ¿Se puede escribir `x` como suma de `k` potencias `n`-ésimas? |
| 4 | `ganar_juego_piedras(n)` | Juego de piedras (quitar 1, 2, 6 o 98), con memoización |
| 5 | `contar_palabras_sin_tres_aes_seguidas(n)` | Palabras en `{a, b}` sin tres `a` consecutivas (recurrencia con memoización) |
| 6 | `egg_drop(n, k)` | Problema de los huevos (DP) |
| 7 | `optimal_mat_mult(tam)` | Coste mínimo del producto encadenado de matrices |
| 8 | `max_gold(l)` | *Pots of Gold*: máximo oro del jugador que empieza |
| 9 | `min_suma_casillas(n, m, a)` | Camino de suma mínima en un tablero (abajo / derecha) |

## Hoja 3 · Aritmética de enteros grandes

Los números se representan como **listas de dígitos** (el menos significativo primero) y se apoyan en el módulo propio `natural`.

| Ejercicio | Función | Descripción | Complejidad binaria |
|---|---|---|---|
| 1 | `div2(a)` | Cociente y resto de dividir por 2 | `O(n)` |
| 1 | `binario(a)` | Decimal → binario | `O(n²)` |
| 2 | `base2_a_decimal(b)` | Binario → decimal | `O(n³)` |
| 8 | `raiz_cuadrada(a)` | ⌊√a⌋ por búsqueda binaria | — |
| 9 | `division_normalizada(a, b)` | División con normalización previa del divisor | — |
| 12 | `calcular_raiz_2_newton(digitos)` | Dígitos de √2 mediante iteración de Newton sobre enteros | — |

## Hoja 4 · Aritmética modular

| Ejercicio | Función | Descripción |
|---|---|---|
| 1 | `fibo_mod(k, N)` | `F_k mod N` por exponenciación rápida de la matriz `[[0,1],[1,1]]` |
| 2 | `reducir_congruencias(l)` | Teorema chino del resto: reduce un sistema de congruencias a una sola |
| 4 | `phi_euler(n)`, `ejc_4()` | Función φ de Euler y verificación de `a⁴⁰ ≡ a²⁰ ≡ 1 (mod 100)` |
| 5 | `ejc_5()` | Comparativa de tiempos: `pow` de Python vs. `potencia_mod` |
| 6 | `es_carmichael(n)`, `carmichael_10_primeros()` | Los 10 primeros números de Carmichael |
| 7 | `menor_raiz_primitiva(p)` | Menor raíz primitiva módulo un primo `p` |
| 12 | *(sesión de consola en comentario)* | Test de primalidad de Lucas para `N = 3·2¹⁸⁹ + 1` |
| 14 | `soluciones_mod_p(p)` | Puntos de la curva `y² ≡ x³ + 7 (mod p)` |
| 15 | `carmichael_5()` | Carmichael de la forma `(6k+1)(12k+1)(18k+1)` (criterio de Korselt) |
| 16 | `pollard(N, B)`, `tortu_liebre(n)` | Método `p − 1` de Pollard y método ρ de Pollard (tortuga y liebre) |

---

## Requisitos

- Python 3.9 o superior
- [`sympy`](https://pypi.org/project/sympy/) (solo para `isprime` en `hoja4.py`)

```bash
pip install sympy
```

### Módulos propios de la asignatura

Algunas hojas importan módulos desarrollados a lo largo del curso que **no están incluidos en este repositorio**:

| Módulo | Usado en | Para qué |
|---|---|---|
| `natural` | `hoja3.py` | Operaciones sobre números naturales como listas de dígitos (`sumar`, `restar`, `multiplicar`, `comparar`, `division_y_resto`, …) |
| `modular` | `hoja4.py` | `potencia_mod`, `gamma_inversa_eficiente`, … |
| `gcds` | `hoja4.py` | `gcd_binario_tail_rec` |

Para ejecutar `hoja3.py` y `hoja4.py`, colócalos en la misma carpeta.

## Uso

Cada archivo se puede importar o ejecutar desde un intérprete interactivo:

```python
>>> from hoja1 import ejc_1, ejc_2, ejc_3, factorizar
>>> ejc_1(1000)
233168
>>> ejc_2(4_000_000)
4613732
>>> ejc_3(10001)
104743
>>> factorizar(1400)
[(2, 3), (5, 2), (7, 1)]

>>> from hoja2 import gcd_extendido_binario, min_suma_casillas
>>> g, a, b = gcd_extendido_binario(240, 46)
>>> a * 240 + b * 46 == g
True

>>> from hoja4 import fibo_mod
>>> fibo_mod(10, 1000)
55
```

## Notas

- Los enunciados se conservan tal cual en los comentarios de cada archivo, de modo que cada ejercicio es autocontenido.
- Los ejercicios puramente teóricos (demostraciones) no aparecen: solo se incluye el código y, cuando se pedía, el análisis de complejidad en comentarios.
- Las numeraciones saltan en algunos puntos (p. ej. hoja 3: 3–7, 10, 11) porque esos ejercicios eran teóricos o no requerían programación.

## Aviso

Este repositorio es un registro personal de estudio. Si estás cursando la asignatura, úsalo como referencia.

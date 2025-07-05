# U. Internacional de Aguascalientes
# Doctorado en Tecnologías de la Transformación Digital
# Materia:  Ingeniería para el procesamiento masivo de datos
# Tutor:    Dr. Jonás Velasco Álvarez
# Alumno:   Luis Alejandro Santana Valadez
# Trabajo:  2.1 Ejercicios de Programación Avanzada con Python
# Objetivo: Programación y ejecución de instrucciones que aplican Compresores
#           y Generadores para comprobar los conceptos teóricos
# Archivo fuente: [2.1. Compresores generadores python.pdf]
# --------------------------------------------------------------------------

# ---------------------------------------------------------------
# Descripción de instrucciones basadas Compresores y Generadores
# ---------------------------------------------------------------

# ----------------------
# Ejercicio sobre map()
# ----------------------
# Prog. 1
squared = list(map(lambda x: x**2, range(5)))
print(squared)           

# Prog. 2
combined = list(map(lambda *args: sum(args), range(3), [10, 20, 30]))
print(combined)       


# ----------------------
# Ejercicio sobre zip()
# ----------------------
# Prog. 1
nums = [1, 2, 3]
chars = ['a', 'b', 'c']
result = list(zip(nums, chars))
print(result)

# Prog. 2
data = list(zip(range(3), 'abc', [10.1, 20.2, 30.3]))
print(data)


# -------------------------
# Ejercicio sobre filter()
# -------------------------
# Prog. 1
nums = [2, 5, 8, 1]
res = list(filter(lambda x: x > 4, nums))
print(res)                  

# Prog. 2
items = [1, 'a', 4, None, 8]
clean = list(filter(lambda x: isinstance(x, int) and x % 2 == 0, items))
print(clean)               


# -------------------------------------
# Ejercicio sobre List Comprehensions
# -------------------------------------
# Prog. 1
print([x**2 for x in range(5)])

# Prog. 2
print([x*y for x in range(1, 4) for y in range(1, x+1)])


# --------------------------------------
# Ejercicio sobre Nested Comprehensions
# --------------------------------------
# Prog. 1
mat = [[i for i in range(3)] for j in range(3)]
print(mat)

# Prog. 2
print([[i*j for j in range(1, 4)] for i in range(1, 4)])


# ---------------------------------------------
# Ejercicio sobre Filtering a Comprehension
# ---------------------------------------------
# Prog. 1
print([x**2 for x in range(10) if x % 2 == 0])

# Prog. 2
print([x*y for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 != 0])


# -------------------------------------------
# Ejercicio sobre Dictionary Comprehensions
# -------------------------------------------
# Prog. 1
print({c: ord(c) for c in 'abc'})

# Prog. 2
from string import ascii_lowercase

print({c: k for k, c in enumerate (ascii_lowercase, 1) if c not in 'aeiou'})


# ------------------------------------
# Ejercicio sobre Set Comprehensions
# ------------------------------------
# Prog. 1
print({x % 3 for x in range(10)})

# Prog. 2
print({(x+y) % 5 for x in range(4) for y in range(3)})


# --------------------------------------
# Ejercicio sobre Generator Functions
# --------------------------------------
def infinite_count(start=0):
    while True:
        yield start
        start += 1

gen = infinite_count(5)
for _ in range(3):
    print(next(gen))


# ---------------------------
# Ejercicio sobre yield from
# ---------------------------
def squares():
    yield from (x**2 for x in range(3))

def combining():
    yield from squares()
    yield from [100, 200]

print(list(combining()))


# ----------------------------------------
# Ejercicio sobre Generator Expressions
# ----------------------------------------
# Prog. 1
gen = (x**2 for x in range(5))
print(next(gen))                  

# Prog. 2
gen = ((x, x**2) 
          for x in range(10) if x % 2 == 0)
print(dict(gen))


# ------------------------------------------------------
# Ejercicio sobre Name Localization in Comprehensions
# ------------------------------------------------------
# Prog. 1
x = 10
print([x for x in range(3)])  
# x sigue siendo 10

# Prog. 2
var = 'externo'
resultado = [var for var in 'abc']
print(var)  
# 'externo'



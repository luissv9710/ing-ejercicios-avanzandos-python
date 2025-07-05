# U. Internacional de Aguascalientes
# Doctorado en Tecnologías de la Transformación Digital
# Materia:  Ingeniería para el procesamiento masivo de datos
# Tutor:    Dr. Jonás Velasco Álvarez
# Alumno:   Luis Alejandro Santana Valadez
# Trabajo:  2.2 Ejercicios de Programación Avanzada con Python
# Objetivo: Programación y ejecución de instrucciones que aplican la P.O.O.,
#           Decoradores e Iteradores para comprobar los conceptos teóricos
# Archivo fuente: [2.2. OOP python.pdf]
# --------------------------------------------------------------------------

# --------------------------------------------------
# Descripción de instrucciones basadas en la P.O.O.
# --------------------------------------------------


# -----------------------------------------------------
# Ejercicio sobre class, objects, __dict__, attributes
# -----------------------------------------------------
class Persona:
    especie = 'Humano'
    nombre = ''

print(Persona.especie)

juan = Persona()
print(juan.especie)      # Hereda atributo

juan.nombre = "Juan"
print(juan.nombre)


print(juan.__dict__) 


# ----------------------
# Ejercicio sobre self
# ----------------------
class Precio:
    def __init__(self):
        self.neto = 0  # definido en el constructor
            
    def final(self, iva, descuento=0):
        return (self.neto * (100 + iva) / 100) - descuento

p = Precio()
p.neto = 100
print(p.final(21, 10))     



# ----------------------
# Ejercicio sobre __init__
# ----------------------
class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def saludo(self):
        return f"Hola, soy {self.nombre}"

u = Usuario("Ana", "ana@mail.com")
print(u.saludo())

# --------------------------------------------
# Ejercicio sobre clases padre y clases hijas
# --------------------------------------------
class Motor:
    def encender(self):
        print("Motor encendido")

class Auto:
    def __init__(self):
        self.motor = Motor()  # composición

    def arrancar(self):
        self.motor.encender()

carro = Auto()
carro.arrancar()

# ------------------------
# Ejercicio sobre super()
# ------------------------
class Base:
    def __init__(self):
        print("Base init")

class Mezcla(Base):
    def __init__(self):
        super().__init__()
        print("Mezcla init")

obj = Mezcla()

# ---------------------------------
# Ejercicio sobre @staticmethod
# ---------------------------------
class StringUtil:
    
    @staticmethod
    def es_palindromo(s):
        s = ''.join(c for c in s if c.isalnum()).lower()
        return s == s[::-1]

print(StringUtil.es_palindromo("Anita lava la tina"))


# ---------------------------------
# Ejercicio sobre @classmethod
# ---------------------------------
class Usuaria:
    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod
    def crear_desde_dict(cls, dd):
        return cls(dd["nombre"])

u = Usuaria.crear_desde_dict({"nombre": "Alex"})


# ---------------------------------
# Ejercicio sobre @property
# ---------------------------------
class Personas:
    def __init__(self, edad):
        self._edad = edad

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, valor):
        if 0 <= valor <= 120:
            self._edad = valor
        else:
            raise ValueError("Edad inválida")


# ---------------------------------
# Ejercicio sobre @cached_property
# ---------------------------------
from functools import cached_property

class DB:
    def __init__(self):
        print("Conectando DB")

class Gestor:
    @cached_property
    def db(self):
        return DB()

g = Gestor()
_ = g.db            # 1era. conexión (se imprime)
del g.db            # Se elimina la caché
_ = g.db            # Nva conn (imprime de nuevo)


# ---------------------------------
# Ejercicio sobre __atributo
# ---------------------------------
class Bases:
    def __init__(self):
        self.__secreto = "oculto"

class Derivada(Bases):
    def __init__(self):
        super().__init__()
        self.__secreto = "visible"

d = Derivada()
print(d.__dict__)  
# {'_Base__secreto': 'oculto', '_Derivada__secreto': 'visible'}


# -------------------------------------------
# Ejercicio sobre __add__, __len__, __bool__
# -------------------------------------------
class Weird:
    def __init__(self, s):
        self.s = s

    def __bool__(self):
        return "42" in self.s

w = Weird("tengo 42 años")
print(bool(w)) 


# -------------------------------------------------
# Ejercicio sobre Método común en múltiples clases
# -------------------------------------------------
class Motors:
    def encender(self):
        print("Motor base")

class MotorV8(Motors):
    def encender(self):
        print("Motor V8")

def test_motor(m):
    m.encender()

test_motor(Motors())
test_motor(MotorV8())




# -----------------------------------------------------------------
# Descripción de instrucciones basadas en Decoradores e Iteradores
# -----------------------------------------------------------------

# --------------------------------------
# Ejercicio 1. sobre @decorador, @wraps
# --------------------------------------
from functools import wraps

def max_result(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(f'Result {result} exceeds {threshold}')
            return result
        return wrapper
    return decorator

@max_result(75)
def cube(n):
    return n**3

print(cube(5))


# --------------------------------------
# Ejercicio 2 sobre @decorador, @wraps
# --------------------------------------
def max_pow(threshold):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result > threshold:
                print(f'Resultado demasiado grande ({result})')
            return result
        return wrapper
    return decorator

@max_pow(100)
def potencia(n):
    return n**3

print(potencia(5))


# --------------------------------------
# Ejercicio sobre __iter__, __next__
# --------------------------------------
class OddEven:
    def __init__(self, data):
        self._data = data
        self.indexes = (
            list(range(0, len(data), 2)) +
            list(range(1, len(data), 2))
        )

    def __iter__(self):
        return self

    def __next__(self):
        if self.indexes:
            return self._data[self.indexes.pop(0)]
        raise StopIteration

texto = OddEven("Python")
print(''.join(c for c in texto))


# Diccionario:
# Cabe recalcar que todos esos términos pertenecen al ecosistema de Python. parte de la biblioteca estándar de Python y otros provienen de bibliotecas adicionales como Pandas y NumPy que sirven para el análisis de datos y operaciones numéricas.
#J_J
'''

Estructura del diccionario.
diccionario = {
"A":{"terminos,": {"categoría": "categoria en español", "traducción": "definicion en español"}},
}
'''
diccionario = {
    "a": {
        "abs": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve el valor absoluto de un número.",
            "traduccion": "Returns the absolute value of a number."},
        "all": {
            "categoria": ("Funciones de lista",),
            "definicion": "Devuelve True si todos los elementos en un iterable son verdaderos.",
            "traduccion": "Returns True if all elements in an iterable are true."},
        "any": {
            "categoria": ("Funciones de lista",),
            "definicion": "Devuelve True si algún elemento en un iterable es verdadero.",
            "traduccion": "Returns True if any element in an iterable is true."},
        "ascii": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Devuelve la versión ASCII de un objeto, eliminando caracteres especiales.",
            "traduccion": "Returns the ASCII version of an object, escaping non-ASCII characters."},
        "append": {
            "categoria": ("Listas",),
            "definicion": "Agrega un elemento al final de una lista.",
            "traduccion": "Adds an element to the end of a list."},
        "argmax": {
            "categoria": ("Funciones NumPy",),
            "definicion": "Devuelve el índice del elemento máximo en una lista o array.",
            "traduccion": "Returns the index of the maximum element in a list or array."},
        "argmin": {
            "categoria": ("Funciones NumPy",),
            "definicion": "Devuelve el índice del elemento mínimo en una lista o array.",
            "traduccion": "Returns the index of the minimum element in a list or array."},
        "array": {
            "categoria": ("Estructura de datos",),
            "definicion": "Estructura de datos que puede almacenar múltiples valores del mismo tipo.",
            "traduccion": "Data structure that can store multiple values of the same type."},
        "as": {
            "categoria": ("Sintaxis de lenguaje",),
            "definicion": "Usado para crear un alias en una importación.",
            "traduccion": "Used to create an alias in an import."},
        "assert": {
            "categoria": ("Depuración",),
            "definicion": "Usado para declarar una condición que debe ser verdadera en el programa.",
            "traduccion": "Used to declare a condition that must be true in the program."},
        "async": {
            "categoria": ("Programación asincrónica",),
            "definicion": "Declara una función como asincrónica.",
            "traduccion": "Declares a function as asynchronous."},
        "await": {
            "categoria": ("Programación asincrónica",),
            "definicion": "Usado para esperar una coroutine en un entorno asincrónico.",
            "traduccion": "Used to wait for a coroutine in an asynchronous context."},
        "attribute": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Una propiedad o método de un objeto.",
            "traduccion": "A property or method of an object."},
        "at": {
            "categoria": ("Indexación",),
            "definicion": "Usado para acceder a un índice específico en una lista o array.",
            "traduccion": "Used to access a specific index in a list or array."},
        "args": {
            "categoria": ("Funciones",),
            "definicion": "Argumentos posicionales pasados a una función.",
            "traduccion": "Positional arguments passed to a function."},
        "kwargs": {
            "categoria": ("Funciones",),
            "definicion": "Argumentos con nombre pasados a una función.",
            "traduccion": "Keyword arguments passed to a function."},
        "apply": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Usado para aplicar una función a un iterable.",
            "traduccion": "Used to apply a function to an iterable."},
        "assertEqual": {
            "categoria": ("Pruebas unitarias",),
            "definicion": "Verifica que dos valores son iguales.",
            "traduccion": "Checks that two values are equal."},
        "assertIsNone": {
            "categoria": ("Pruebas unitarias",),
            "definicion": "Verifica que el valor sea None.",
            "traduccion": "Checks that the value is None."},
        "attributeError": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Excepción lanzada cuando un atributo de un objeto no se encuentra.",
            "traduccion": "Exception raised when an attribute of an object is not found."},
        "add": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve la suma de dos números.",
            "traduccion": "Returns the sum of two numbers."},
        "allclose": {
            "categoria": ("Funciones NumPy",),
            "definicion": "Verifica si dos arrays son iguales dentro de una tolerancia específica.",
            "traduccion": "Checks if two arrays are equal within a specific tolerance."},
        "average": {
            "categoria": ("Estadística",),
            "definicion": "Calcula el promedio de una lista de números.",
            "traduccion": "Calculates the average of a list of numbers."},
        "assertAlmostEqual": {
            "categoria": ("Pruebas unitarias",),
            "definicion": "Verifica que dos números son aproximadamente iguales.",
            "traduccion": "Checks that two numbers are approximately equal."},
        "absolute_import": {
            "categoria": ("Importación de módulos",),
            "definicion": "Importación que se refiere a un módulo desde la raíz del paquete.",
            "traduccion": "Import that refers to a module from the root of the package."},
        "allexcept": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Usado para capturar todas las excepciones excepto una específica.",
            "traduccion": "Used to catch all exceptions except for a specific one."},
        "as_tuple": {
            "categoria": ("Estructura de datos",),
            "definicion": "Devuelve los resultados como una tupla.",
            "traduccion": "Returns the results as a tuple."},
        "atleast_1d": {
            "categoria": ("Funciones NumPy",),
            "definicion": "Convierte una entrada en un array de al menos una dimensión.",
            "traduccion": "Converts input to an array of at least one dimension."},
        "atleast_2d": {
            "categoria": ("Funciones NumPy",),
            "definicion": "Convierte una entrada en un array de al menos dos dimensiones.",
            "traduccion": "Converts input to an array of at least two dimensions."},
        "arange": {
            "categoria": ("Funciones NumPy",),
            "definicion": "Crea un array con valores espaciados uniformemente en un rango específico.",
            "traduccion": "Creates an array with evenly spaced values within a specified range."},
        "arccos": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve el arco coseno de un número.",
            "traduccion": "Returns the arc cosine of a number."},
        "arcsin": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve el arco seno de un número.",
            "traduccion": "Returns the arc sine of a number."},
        "arctan": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve el arco tangente de un número.",
            "traduccion": "Returns the arc tangent of a number."},
        "argparse": {
            "categoria": ("Análisis de argumentos",),
            "definicion": "Módulo para analizar argumentos de línea de comandos.",
            "traduccion": "Module for parsing command-line arguments."},
        "array_like": {
            "categoria": ("Estructura de datos",),
            "definicion": "Cualquier objeto que pueda ser convertido a un array.",
            "traduccion": "Any object that can be converted to an array."}},
    
    "b": {
        "bin": {
            "categoria": ("Conversión de datos",),
            "definicion": "Convierte un número en su representación binaria.",
            "traduccion": "Converts a number to its binary representation."},
        "bool": {
            "categoria": ("Tipos de datos",),
            "definicion": "Convierte un valor en su equivalente booleano (True o False).",
            "traduccion": "Converts a value to its boolean equivalent (True or False)."},
        "break": {
            "categoria": ("Control de flujo",),
            "definicion": "Termina el ciclo en el que se encuentra.",
            "traduccion": "Terminates the loop it is in."},
        "bytes": {
            "categoria": ("Tipos de datos",),
            "definicion": "Convierte a una secuencia inmutable de bytes.",
            "traduccion": "Converts to an immutable sequence of bytes."},
        "bytearray": {
            "categoria": ("Tipos de datos",),
            "definicion": "Crea una secuencia mutable de bytes.",
            "traduccion": "Creates a mutable sequence of bytes."},
        "byteswap": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Invierte el orden de los bytes en una estructura de datos.",
            "traduccion": "Swaps the byte order in a data structure."},
        "buffer": {
            "categoria": ("Memoria",),
            "definicion": "Interfaz para acceder a los datos sin copiarlos.",
            "traduccion": "Interface to access data without copying it."},
        "base64": {
            "categoria": ("Codificación y decodificación",),
            "definicion": "Codifica y decodifica datos en el formato base64.",
            "traduccion": "Encodes and decodes data in base64 format."},
        "bitwise_and": {
            "categoria": ("Operadores bit a bit",),
            "definicion": "Operador AND bit a bit entre dos números.",
            "traduccion": "Performs a bitwise AND operation between two numbers."},
        "bitwise_or": {
            "categoria": ("Operadores bit a bit",),
            "definicion": "Operador OR bit a bit entre dos números.",
            "traduccion": "Performs a bitwise OR operation between two numbers."},
        "bitwise_xor": {
            "categoria": ("Operadores bit a bit",),
            "definicion": "Operador XOR bit a bit entre dos números.",
            "traduccion": "Performs a bitwise XOR operation between two numbers."},
        "bitwise_not": {
            "categoria": ("Operadores bit a bit",),
            "definicion": "Operador NOT bit a bit que invierte los bits de un número.",
            "traduccion": "Performs a bitwise NOT operation, inverting bits of a number."},
        "binomial": {
            "categoria": ("Estadística",),
            "definicion": "Distribución binomial en estadística.",
            "traduccion": "Binomial distribution in statistics."},
        "binascii": {
            "categoria": ("Conversión de datos",),
            "definicion": "Módulo para conversiones entre datos binarios y representaciones ASCII.",
            "traduccion": "Module for conversions between binary data and ASCII representations."},
        "byteorder": {
            "categoria": ("Memoria",),
            "definicion": "Propiedad que determina el orden de los bytes en un sistema ('big' o 'little').",
            "traduccion": "Property determining byte order in a system ('big' or 'little')."},
        "bit_length": {
            "categoria": ("Operaciones numéricas",),
            "definicion": "Devuelve el número de bits necesarios para representar un número en binario.",
            "traduccion": "Returns the number of bits required to represent a number in binary."},
        "breakpoint": {
            "categoria": ("Depuración",),
            "definicion": "Punto de interrupción para depurar el código.",
            "traduccion": "Breakpoint for debugging code."},
        "binhex": {
            "categoria": ("Conversión de datos",),
            "definicion": "Convierte datos binarios en formato hexadecimal.",
            "traduccion": "Converts binary data to hexadecimal format."},
        "bitset": {
            "categoria": ("Estructura de datos",),
            "definicion": "Conjunto de bits para operaciones bit a bit.",
            "traduccion": "Set of bits for bitwise operations."},
        "broadcast": {
            "categoria": ("Manipulación de arrays",),
            "definicion": "Extiende dimensiones para operaciones en arrays.",
            "traduccion": "Extends dimensions for operations on arrays."},
        "bitarray": {
            "categoria": ("Estructura de datos",),
            "definicion": "Estructura de datos que representa una secuencia de bits.",
            "traduccion": "Data structure representing a sequence of bits."},
        "buffer": {
            "categoria": ("Memoria",),
            "definicion": "Interfaz para manejar objetos de memoria sin copiarlos.",
            "traduccion": "Interface for handling memory objects without copying them."},
        "bitwise_left_shift": {
            "categoria": ("Operadores bit a bit",),
            "definicion": "Desplaza los bits de un número a la izquierda, equivalente a multiplicación por potencias de dos.",
            "traduccion": "Shifts the bits of a number to the left, equivalent to multiplication by powers of two."},
        "bitwise_right_shift": {
            "categoria": ("Operadores bit a bit",),
            "definicion": "Desplaza los bits de un número a la derecha, equivalente a división por potencias de dos.",
            "traduccion": "Shifts the bits of a number to the right, equivalent to division by powers of two."},
        "bz2": {
            "categoria": ("Compresión de datos",),
            "definicion": "Módulo para compresión y descompresión de archivos en formato bzip2.",
            "traduccion": "Module for compressing and decompressing files in bzip2 format."},
        "bool_": {
            "categoria": ("Tipos de datos",),
            "definicion": "Tipo de dato booleano en bibliotecas como NumPy.",
            "traduccion": "Boolea"}},
    
    "c": {
        "callable": {
            "categoria": ("Funciones",),
            "definicion": "Devuelve True si el objeto es llamable (función, método, etc.).",
            "traduccion": "Returns True if the object is callable (function, method, etc.)."},
        "chr": {
            "categoria": ("Conversión de datos",),
            "definicion": "Convierte un código ASCII en su carácter correspondiente.",
            "traduccion": "Converts an ASCII code to its corresponding character."},
        "class": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Define una nueva clase para crear objetos personalizados.",
            "traduccion": "Defines a new class to create custom objects."},
        "classmethod": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Convierte un método en un método de clase, accesible desde la clase sin instanciarla.",
            "traduccion": "Converts a method to a class method, accessible from the class without instantiating it."},
        "compile": {
            "categoria": ("Compilación",),
            "definicion": "Compila una cadena de texto en código ejecutable de Python.",
            "traduccion": "Compiles a text string into executable Python code."},
        "complex": {
            "categoria": ("Tipos de datos",),
            "definicion": "Crea un número complejo a partir de dos valores (real e imaginario).",
            "traduccion": "Creates a complex number from two values (real and imaginary)."},
        "continue": {
            "categoria": ("Control de flujo",),
            "definicion": "Salta la iteración actual de un bucle y pasa a la siguiente.",
            "traduccion": "Skips the current iteration of a loop and moves to the next one."},
        "copy": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Crea una copia superficial de una lista, diccionario u otro objeto mutable.",
            "traduccion": "Creates a shallow copy of a list, dictionary, or other mutable object."},
        "coroutine": {
            "categoria": ("Programación asincrónica",),
            "definicion": "Define una función especial que puede pausarse y reanudarse (asincrónica).",
            "traduccion": "Defines a special function that can be paused and resumed (asynchronous)."},
        "count": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Cuenta la cantidad de ocurrencias de un valor en una lista o cadena.",
            "traduccion": "Counts the occurrences of a value in a list or string."},
        "clear": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Elimina todos los elementos de una lista o diccionario.",
            "traduccion": "Removes all elements from a list or dictionary."},
        "cmath": {
            "categoria": ("Matemáticas complejas",),
            "definicion": "Módulo para operaciones matemáticas complejas.",
            "traduccion": "Module for complex mathematical operations."},
        "chain": {
            "categoria": ("Manipulación de iterables",),
            "definicion": "Función del módulo itertools que concatena múltiples iterables.",
            "traduccion": "Function from itertools module that concatenates multiple iterables."},
        "csv": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Módulo para manipular archivos CSV (valores separados por comas).",
            "traduccion": "Module for handling CSV (comma-separated values) files."},
        "copyreg": {
            "categoria": ("Serialización",),
            "definicion": "Módulo que registra funciones para serialización de objetos.",
            "traduccion": "Module that registers functions for object serialization."},
        "counter": {
            "categoria": ("Estructura de datos",),
            "definicion": "Clase de collections para contar elementos en un iterable.",
            "traduccion": "Class from collections to count elements in an iterable."},
        "cProfile": {
            "categoria": ("Depuración y optimización",),
            "definicion": "Herramienta para realizar un perfil de rendimiento de código Python.",
            "traduccion": "Tool for profiling Python code performance."},
        "capitalize": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Devuelve una copia de la cadena con la primera letra en mayúscula.",
            "traduccion": "Returns a copy of the string with the first letter capitalized."},
        "center": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Devuelve una cadena centrada, con ancho especificado y relleno opcional.",
            "traduccion": "Returns a centered string with specified width and optional fill character."},
        "ceil": {
            "categoria": ("Matemáticas",),
            "definicion": "Redondea un número al entero más próximo hacia arriba.",
            "traduccion": "Rounds a number up to the nearest integer."},
        "call": {
            "categoria": ("Funciones",),
            "definicion": "Ejecuta una función o método específico en un objeto.",
            "traduccion": "Executes a specific function or method on an object."},
        "clamp": {
            "categoria": ("Matemáticas",),
            "definicion": "Restringe un valor dentro de un rango especificado (no en la biblioteca estándar).",
            "traduccion": "Restricts a value within a specified range (not in standard library)."},
        "choice": {
            "categoria": ("Generación de datos aleatorios",),
            "definicion": "Selecciona un elemento aleatorio de una secuencia.",
            "traduccion": "Selects a random element from a sequence."},
        "collections": {
            "categoria": ("Estructura de datos",),
            "definicion": "Módulo que proporciona estructuras de datos especializadas.",
            "traduccion": "Module providing specialized data structures."},
        "compress": {
            "categoria": ("Manipulación de iterables",),
            "definicion": "Filtra elementos de un iterable según un selector booleano.",
            "traduccion": "Filters elements in an iterable according to a boolean selector."},
        "complex_conjugate": {
            "categoria": ("Matemáticas complejas",),
            "definicion": "Devuelve el conjugado de un número complejo.",
            "traduccion": "Returns the conjugate of a complex number."},
        "ctypes": {
            "categoria": ("Interoperabilidad",),
            "definicion": "Módulo para manipular datos en bibliotecas compartidas en C.",
            "traduccion": "Module for handling data in C shared libraries."},
        "clear_screen": { 
            "categoria": ("Interacción con el sistema",),
            "definicion": "Limpia la pantalla en algunos entornos de terminal (no es una función estándar).",
            "traduccion": "Clears the screen in some terminal environments (not a standard function)."},
        "call_later": {
            "categoria": ("Programación asincrónica",),
            "definicion": "Programa la ejecución de una función después de un tiempo en asyncio.",
            "traduccion": "Schedules the execution of a function after a delay in asyncio."},
        "chunk": {
            "categoria": ("Manipulación de iterables",),
            "definicion": "Divide un iterable en partes de tamaño fijo (disponible en itertools y otras bibliotecas).",
            "traduccion": "Splits an iterable into fixed-size chunks (available in itertools and other libraries)."},
        "cycle": {
            "categoria": ("Manipulación de iterables",),
            "definicion": "Itertools: Cicla infinitamente a través de un iterable.",
            "traduccion": "Itertools: Cycles infinitely through an iterable."},
        "coerce": {
            "categoria": ("Conversión de datos",),
            "definicion": "Convierte parámetros a un tipo común (obsoleto en Python 3).",
            "traduccion": "Converts parameters to a common type (obsolete in Python 3)."},
        "current_thread": {
            "categoria": ("Hilos",),
            "definicion": "Obtiene el hilo actual de ejecución en threading.",
            "traduccion": "Gets the current thread in threading."},
        "configparser": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Módulo para manipular archivos de configuración estilo INI.",
            "traduccion": "Module for handling INI-style configuration files."},
        "compileall": {
            "categoria": ("Compilación",),
            "definicion": "Compila recursivamente archivos .py en bytecode.",
            "traduccion": "Recursively compiles .py files to bytecode."},
        "copytree": {
            "categoria": ("Manipulación de archivos",),
            "definicion": "Copia recursivamente un directorio completo.",
            "traduccion": "Recursively copies an entire directory."}},
    
    "d": {
        "def": {
            "categoria": ("Función",),
            "definicion": "Declara una función o método.",
            "traduccion": "Declares a function or method."},
        "delattr": {
            "categoria": ("Función",),
            "definicion": "Elimina un atributo de un objeto.",
            "traduccion": "Deletes an attribute from an object."},
        "dataframe": {
            "categoria": ("Estructura de datos",),
            "definicion": "Estructura de datos de Pandas para manipulación de datos tabulares.",
            "traduccion": "Pandas data structure for manipulating tabular data."},
        "decode": {
            "categoria": ("Método",),
            "definicion": "Convierte bytes en una cadena utilizando una codificación.",
            "traduccion": "Converts bytes into a string using an encoding."},
        "decimal": {
            "categoria": ("Módulo",),
            "definicion": "Módulo para operaciones aritméticas con decimales de precisión exacta.",
            "traduccion": "Module for arithmetic operations with exact decimal precision."},
        "device": {
            "categoria": ("Atributo",),
            "definicion": "Atributo en PyTorch para definir el dispositivo (CPU o GPU) donde se almacenan los tensores.",
            "traduccion": "Attribute in PyTorch to define the device (CPU or GPU) for tensor storage."},
        "dict.get": {
            "categoria": ("Método",),
            "definicion": "Obtiene el valor de una clave en un diccionario o un valor predeterminado si la clave no existe.",
            "traduccion": "Gets the value of a dictionary key or a default if the key doesn't exist."},
        "dropna": {
            "categoria": ("Método",),
            "definicion": "Elimina filas o columnas con valores nulos en un DataFrame de Pandas.",
            "traduccion": "Removes rows or columns with null values in a Pandas DataFrame."},
        "dtype": {
            "categoria": ("Atributo",),
            "definicion": "Especifica el tipo de datos de un array en NumPy.",
            "traduccion": "Specifies the data type of a NumPy array."},
        "deque.appendleft": {
            "categoria": ("Método",),
            "definicion": "Agrega un elemento al inicio de una deque.",
            "traduccion": "Adds an element to the beginning of a deque."},
        "dict.update": {
            "categoria": ("Método",),
            "definicion": "Actualiza un diccionario con pares clave-valor de otro diccionario.",
            "traduccion": "Updates a dictionary with key-value pairs from another dictionary."},
        "del": {
            "categoria": ("Operador",),
            "definicion": "Elimina una variable, elemento o atributo.",
            "traduccion": "Deletes a variable, element, or attribute."},
        "dict": {
            "categoria": ("Tipo de dato",),
            "definicion": "Tipo de dato de diccionario que almacena pares clave-valor.",
            "traduccion": "Dictionary data type that stores key-value pairs."},
        "dir": {
            "categoria": ("Función",),
            "definicion": "Devuelve una lista de atributos y métodos disponibles para un objeto.",
            "traduccion": "Returns a list of attributes and methods available for an object."},
        "divmod": {
            "categoria": ("Función",),
            "definicion": "Devuelve el cociente y el residuo de una división.",
            "traduccion": "Returns the quotient and remainder of a division."},
        "deque": {
            "categoria": ("Clase",),
            "definicion": "Clase de collections para una cola de doble extremo.",
            "traduccion": "Class from collections for a double-ended queue."},
        "defaultdict": {
            "categoria": "Tipo de dato",
            "definicion": "Diccionario que asigna un valor predeterminado a claves no existentes.",
            "traduccion": "Dictionary that assigns a default value to nonexistent keys."},
        "decode": {
            "categoria": ("Método",),
            "definicion": "Convierte bytes a una cadena usando una codificación específica.",
            "traduccion": "Converts bytes to a string using a specific encoding."},
        "deflate": {
            "categoria": ("Método",),
            "definicion": "Método de compresión para reducir el tamaño de archivos.",
            "traduccion": "Compression method to reduce file sizes."},
        "deepcopy": {
            "categoria": ("Método",),
            "definicion": "Copia un objeto y todos sus objetos anidados.",
            "traduccion": "Copies an object and all its nested objects."},
        "detach": {
            "categoria": ("Método",),
            "definicion": "Desconecta un buffer de un flujo (usado en IO).",
            "traduccion": "Disconnects a buffer from a stream (used in IO)."},
        "dump": {
            "categoria": ("Método",),
            "definicion": "Serializa un objeto a un archivo en formato binario o JSON.",
            "traduccion": "Serializes an object to a file in binary or JSON format."},
        "dumps": {
            "categoria": ("Método",),
            "definicion": "Serializa un objeto a una cadena en formato JSON.",
            "traduccion": "Serializes an object to a string in JSON format."},
        "difference": {
            "categoria": ("Método",),
            "definicion": "Devuelve la diferencia entre conjuntos.",
            "traduccion": "Returns the difference between sets."},
        "difference_update": {
            "categoria": ("Método",),
            "definicion": "Actualiza un conjunto, eliminando elementos encontrados en otro conjunto.",
            "traduccion": "Updates a set by removing elements found in another set."},
        "decode_header": {
            "categoria": ("Método",),
            "definicion": "Decodifica un encabezado de correo electrónico.",
            "traduccion": "Decodes an email header."},
        "disk_usage": {
            "categoria": ("Función",),
            "definicion": "Devuelve el uso de espacio en disco de un directorio o disco (en shutil).",
            "traduccion": "Returns disk space usage of a directory or disk (in shutil)."},
       "datetime": {
           "categoria": ("Fecha",),
           "traduccion": "Class for manipulating dates and times.",
           "definicion": "Proporciona funciones y objetos para trabajar con fechas y horas en Python."},
        "difference": {
            "categoria": ("Método",),
            "definicion": "Devuelve la diferencia entre dos o más conjuntos.",
            "traduccion": "Returns the difference between two or more sets."},
        "disk_cache": {
            "categoria": ("Caché",),
            "definicion": "Caché que almacena temporalmente datos en el disco.",
            "traduccion": "Cache that temporarily stores data on disk."}},
    "e":{
        "enumerate": {
            "categoria": ("Manipulación de iterables",),
            "definicion": "Agrega un contador a un iterable y lo devuelve como un objeto enumerado.",
            "traduccion": "Adds a counter to an iterable and returns it as an enumerated object."},
        "eval": {
            "categoria": ("Evaluación de expresiones",),
            "definicion": "Ejecuta una expresión Python desde una cadena dada.",
            "traduccion": "Executes a Python expression from a given string."},
        "exec": {
            "categoria": ("Ejecución de código",),
            "definicion": "Ejecuta un código Python dinámico en el entorno actual.",
            "traduccion": "Executes dynamic Python code in the current environment."},
        "except": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Bloque que captura excepciones en el manejo de errores.",
            "traduccion": "Block that catches exceptions in error handling."},
        "else": {
            "categoria": ("Control de flujo",),
            "definicion": "Bloque que se ejecuta cuando no se cumple una condición if.",
            "traduccion": "Block that runs when an if condition is not met."},
        "elif": {
            "categoria": ("Control de flujo",),
            "definicion": "Condición alternativa en una declaración if.",
            "traduccion": "Alternative condition in an if statement."},
        "exit": {
            "categoria": ("Control de programa",),
            "definicion": "Finaliza el programa actual.",
            "traduccion": "Terminates the current program."},
        "end": {
            "categoria": ("Impresión",),
            "definicion": "Argumento en print() que especifica el carácter final en la salida.",
            "traduccion": "Argument in print() specifying the end character in output."},
        "expandtabs": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Convierte tabulaciones en espacios en una cadena.",
            "traduccion": "Converts tabs to spaces in a string."},
        "encode": {
            "categoria": ("Codificación",),
            "definicion": "Convierte una cadena en bytes usando una codificación específica.",
            "traduccion": "Converts a string to bytes using a specified encoding."},
        "element": {
            "categoria": ("Estructura de datos",),
            "definicion": "Un item en una colección como listas o conjuntos.",
            "traduccion": "An item in a collection such as lists or sets."},
        "error": {
            "categoria": ("Manejo de errores",),
            "definicion": "Indica que ha ocurrido un problema en el programa.",
            "traduccion": "Indicates that an issue has occurred in the program."},
        "exception": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Un error que ocurre durante la ejecución del programa.",
            "traduccion": "An error that occurs during program execution."},
        "evaluate": {
            "categoria": ("Evaluación de expresiones",),
            "definicion": "Determina el valor de una expresión o variable.",
            "traduccion": "Determines the value of an expression or variable."},
        "elements": {
            "categoria": ("Estructura de datos",),
            "definicion": "Conjunto de items en una colección.",
            "traduccion": "Set of items in a collection."},
        "exponential": {
            "categoria": ("Matemáticas",),
            "definicion": "Función que calcula la potencia de un número.",
            "traduccion": "Function that calculates the power of a number."},
        "enumerations": {
            "categoria": ("Estructura de datos",),
            "definicion": "Tipo de dato que permite definir conjuntos de constantes.",
            "traduccion": "Data type that allows defining sets of constants."},
        "encode_utf8": {
            "categoria": ("Codificación",),
            "definicion": "Convierte una cadena a bytes usando la codificación UTF-8.",
            "traduccion": "Converts a string to bytes using UTF-8 encoding."},
        "execfile": {
            "categoria": ("Ejecución de código",),
            "definicion": "Ejecuta un archivo Python como si fuera un script.",
            "traduccion": "Executes a Python file as if it were a script."},
        "edit_distance": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Número mínimo de operaciones necesarias para transformar una cadena en otra.",
            "traduccion": "Minimum number of operations needed to transform one string into another."},
        "eval_input": {
            "categoria": ("Evaluación de expresiones",),
            "definicion": "Evalúa una expresión ingresada por el usuario.",
            "traduccion": "Evaluates an expression entered by the user."},
        "exceed": {
            "categoria": ("Comparación",),
            "definicion": "Sobrepasar un límite o cantidad.",
            "traduccion": "To go beyond a limit or amount."},
        "expected": {
            "categoria": ("Comparación",),
            "definicion": "El resultado que se prevé en una operación.",
            "traduccion": "The outcome that is anticipated in an operation."},
        "encode_base64": {
            "categoria": ("Codificación",),
            "definicion": "Convierte datos en una representación Base64.",
            "traduccion": "Converts data into a Base64 representation."},
        "execute": {
            "categoria": ("Ejecución de código",),
            "definicion": "Llevar a cabo un comando o instrucción.",
            "traduccion": "Carry out a command or instruction."},
        "exit_code": {
            "categoria": ("Control de programa",),
            "definicion": "Valor devuelto al finalizar un programa.",
            "traduccion": "Value returned when a program finishes."},
        "evaluate_expression": {
            "categoria": ("Evaluación de expresiones",),
            "definicion": "Evalúa una expresión para determinar su valor.",
            "traduccion": "Evaluates an expression to determine its value."},
        "environment": {
            "categoria": ("Configuración",),
            "definicion": "Conjunto de variables que afectan la ejecución de un programa.",
            "traduccion": "Set of variables that affect the execution of a program."},
        "environment_variable": {
            "categoria": ("Configuración",),
            "definicion": "Variable que define el comportamiento de procesos en el sistema.",
            "traduccion": "Variable that defines the behavior of processes in the system."},
        "exp": {
            "categoria": ("Matemáticas",),
            "definicion": "Función que devuelve el valor de e elevado a la potencia especificada.",
            "traduccion": "Function that returns the value of e raised to the specified power."},
        "exception_handling": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Mecanismo para manejar errores y excepciones en el código.",
            "traduccion": "Mechanism to handle errors and exceptions in code."},
        "expand": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Desarrolla variables o estructuras de datos.",
            "traduccion": "Expands variables or data structures."},
        "environment_config": {
            "categoria": ("Configuración",),
            "definicion": "Configuraciones que definen el entorno de ejecución.",
            "traduccion": "Configurations that define the runtime environment."},
        "equal": {
            "categoria": ("Comparación",),
            "definicion": "Operador que verifica la igualdad entre dos valores.",
            "traduccion": "Operator that checks equality between two values."},
        "error_handling": {
            "categoria": ("Manejo de errores",),
            "definicion": "Proceso de gestionar errores en el código.",
            "traduccion": "Process of managing errors in code."},
        "event": {
            "categoria": ("Eventos",),
            "definicion": "Acción que ocurre en un programa, como un clic de ratón.",
            "traduccion": "An action that occurs in a program, such as a mouse click."},
        "event_loop": {
            "categoria": ("Programación asincrónica",),
            "definicion": "Ciclo que espera y despacha eventos o mensajes.",
            "traduccion": "Loop that waits for and dispatches events or messages."},
        "exception_type": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Tipo de error que se puede manejar en Python.",
            "traduccion": "Type of error that can be handled in Python."},
        "error_message": {
            "categoria": ("Manejo de errores",),
            "definicion": "Mensaje que describe el error ocurrido.",
            "traduccion": "Message describing the error that occurred."},
        "extract": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Obtiene un valor específico de una colección.",
            "traduccion": "Retrieves a specific value from a collection."},
        "exit_status": {
            "categoria": ("Control de programa",),
            "definicion": "Estado de salida que indica si un programa finalizó con éxito.",
            "traduccion": "Exit status indicating whether a program finished successfully."}},
    
    "f": {
        "filemode": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Modo en el que se abre un archivo, como lectura o escritura.",
            "traduccion": "Mode in which a file is opened, such as read or write."},
        "frozen_set": {
            "categoria": ("Estructura de datos",),
            "definicion": "Colección inmutable de elementos únicos.",
            "traduccion": "Immutable collection of unique elements."},
        "format_map": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Devuelve una cadena formateada usando un diccionario.",
            "traduccion": "Returns a formatted string using a dictionary."},
        "find": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Busca una subcadena dentro de una cadena y devuelve su índice.",
            "traduccion": "Searches for a substring within a string and returns its index."},
        "float32": {
            "categoria": ("Tipos de datos",),
            "definicion": "Tipo de dato que representa un número en punto flotante de 32 bits.",
            "traduccion": "Data type representing a 32-bit floating-point number."},
        "float64": {
            "categoria": ("Tipos de datos",),
            "definicion": "Tipo de dato que representa un número en punto flotante de 64 bits.",
            "traduccion": "Data type representing a 64-bit floating-point number."},
        "formatting": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Proceso de dar formato a la salida de texto.",
            "traduccion": "Process of formatting the output of text."},
        "flush_output": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Forza la escritura de datos en la salida estándar.",
            "traduccion": "Forces the writing of data to standard output."},
        "function_definition": {
            "categoria": ("Funciones",),
            "definicion": "La forma en que se define una función en Python.",
            "traduccion": "The way a function is defined in Python."},
        "filepath": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Ruta que especifica la ubicación de un archivo en el sistema de archivos.",
            "traduccion": "Path that specifies the location of a file in the file system."},
        "flask": {
            "categoria": ("Frameworks",),
            "definicion": "Microframework para desarrollar aplicaciones web en Python.",
            "traduccion": "Microframework for developing web applications in Python."},
        "filtering": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Proceso de eliminar elementos no deseados de una colección.",
            "traduccion": "Process of removing unwanted elements from a collection."},
        "futures": {
            "categoria": ("Programación asincrónica",),
            "definicion": "Una forma de trabajar con programación asíncrona en Python.",
            "traduccion": "A way to work with asynchronous programming in Python."},
        "fold": {
            "categoria": ("Funciones",),
            "definicion": "Función que aplica una operación acumulativa sobre un iterable.",
            "traduccion": "Function that applies an accumulating operation over an iterable."},
        "fromkeys": {
            "categoria": ("Estructura de datos",),
            "definicion": "Método de diccionario que crea un nuevo diccionario con claves y un valor por defecto.",
            "traduccion": "Dictionary method that creates a new dictionary with keys and a default value."},
        "flask_restful": {
            "categoria": ("Frameworks",),
            "definicion": "Extensión de Flask para construir APIs RESTful de manera sencilla.",
            "traduccion": "Flask extension for building RESTful APIs easily."},
        "fix": {
            "categoria": ("Depuración",),
            "definicion": "Corregir o ajustar errores en el código.",
            "traduccion": "To correct or adjust bugs in code."},
        "float_conversion": {
            "categoria": ("Conversión de datos",),
            "definicion": "Proceso de convertir un número a su representación en punto flotante.",
            "traduccion": "Process of converting a number to its floating-point representation."},
        "full_path": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Ruta completa a un archivo, incluyendo el nombre del archivo y su directorio.",
            "traduccion": "Complete path to a file, including the filename and its directory."},
        "filter": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Crea una lista de elementos para los cuales una función devuelve True.",
            "traduccion": "Creates a list of elements for which a function returns True."},
        "float": {
            "categoria": ("Tipos de datos",),
            "definicion": "Tipo de dato que representa un número en punto flotante.",
            "traduccion": "Data type that represents a floating-point number."},
        "for": {
            "categoria": ("Control de flujo",),
            "definicion": "Crea un bucle que itera sobre un iterable.",
            "traduccion": "Creates a loop that iterates over an iterable."},
        "format": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Devuelve una cadena formateada.",
            "traduccion": "Returns a formatted string."},
        "from": {
            "categoria": ("Importación de módulos",),
            "definicion": "Utilizado para importar módulos o partes de un módulo.",
            "traduccion": "Used to import modules or parts of a module."},
        "function": {
            "categoria": ("Funciones",),
            "definicion": "Bloque de código reutilizable que realiza una tarea específica.",
            "traduccion": "Reusable block of code that performs a specific task."},
        "fibonacci": {
            "categoria": ("Matemáticas",),
            "definicion": "Secuencia de números donde cada número es la suma de los dos anteriores.",
            "traduccion": "Sequence of numbers where each number is the sum of the two preceding ones."},
        "file": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Objeto que representa un archivo en el sistema de archivos.",
            "traduccion": "Object that represents a file in the file system."},
        "fwrite": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Escribe datos en un archivo abierto.",
            "traduccion": "Writes data to an open file."},
        "fread": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Lee datos de un archivo abierto.",
            "traduccion": "Reads data from an open file."},
        "finally": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Bloque que se ejecuta después de un try/except, sin importar si se produjo un error.",
            "traduccion": "Block that executes after a try/except, regardless of whether an error occurred."},
        "freeze": {
            "categoria": ("Estructura de datos",),
            "definicion": "Convierte un objeto en un formato inmutable.",
            "traduccion": "Converts an object into an immutable format."},
        "flush": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Vacía el búfer de un archivo para asegurar que todos los datos se escriban.",
            "traduccion": "Flushes the file buffer to ensure all data is written."},
        "fstring": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Cadena formateada literal, que permite incrustar expresiones.",
            "traduccion": "Formatted string literal, allowing embedded expressions."},
        "factorial": {
            "categoria": ("Matemáticas",),
            "definicion": "Producto de todos los números enteros positivos hasta un número dado.",
            "traduccion": "Product of all positive integers up to a given number."},
        "frozen": {
            "categoria": ("Estructura de datos",),
            "definicion": "Un tipo de conjunto inmutable.",
            "traduccion": "An immutable set type."},
        "filterfalse": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Devuelve un iterador que filtra elementos de una secuencia para los cuales la función es False.",
            "traduccion": "Returns an iterator filtering elements from a sequence for which the function is False."},
        "fuzzy": {
            "categoria": ("Manejo de datos",),
            "definicion": "Método que permite trabajar con datos inexactos o imprecisos.",
            "traduccion": "Method that allows working with inaccurate or imprecise data."},
        "fibonacci_sequence": {
            "categoria": ("Matemáticas",),
            "definicion": "Genera la secuencia de Fibonacci hasta un número específico.",
            "traduccion": "Generates the Fibonacci sequence up to a specific number."},
        "format_spec": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Especificación que define cómo se debe formatear un valor.",
            "traduccion": "Specification that defines how a value should be formatted."},
        "fork": {
            "categoria": ("Procesos del sistema",),
            "definicion": "Crea un nuevo proceso en sistemas operativos basados en Unix.",
            "traduccion": "Creates a new process in Unix-based operating systems."},
        "forking": {
            "categoria": ("Procesos del sistema",),
            "definicion": "Proceso de dividir un programa en varios procesos para ejecutar tareas en paralelo.",
            "traduccion": "Process of dividing a program into multiple processes to run tasks in parallel."},
        "first": {
            "categoria": ("Manipulación de iterables",),
            "definicion": "Método para obtener el primer elemento de una secuencia.",
            "traduccion": "Method to get the first element of a sequence."},
        "float_format": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Especificación de formato para representar números en punto flotante.",
            "traduccion": "Format specification for representing floating-point numbers."},
        "filter_none": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Devuelve un iterador que filtra elementos que no son None.",
            "traduccion": "Returns an iterator filtering elements that are not None."},
        "func_code": {
            "categoria": ("Funciones",),
            "definicion": "Código byte que representa el cuerpo de una función.",
            "traduccion": "Bytecode representing the body of a function."},
        "float_power": {
            "categoria": ("Matemáticas",),
            "definicion": "Función que eleva un número a la potencia de otro número en punto flotante.",
            "traduccion": "Function that raises a number to the power of another floating-point number."},
        "format_string": {
            "categoria": ("Manipulación de texto",),
            "definicion": "Cadena que especifica cómo se deben formatear los valores en Python.",
            "traduccion": "String that specifies how values should be formatted in Python."},
        "filename": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Nombre de un archivo, que puede incluir su extensión.",
            "traduccion": "Name of a file, which may include its extension."},
        "file_object": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Objeto que permite interactuar con un archivo abierto en Python.",
            "traduccion": "Object that allows interaction with an open file in Python."},
        "finally_clause": {
            "categoria": ("Manejo de excepciones",),
            "definicion": "Parte de una estructura try/except que se ejecuta siempre, independientemente de los errores.",
            "traduccion": "Part of a try/except structure that always executes, regardless of errors."},
        "file_read": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Operación que lee el contenido de un archivo.",
            "traduccion": "Operation that reads the content of a file."},
        "form": {
            "categoria": ("Web",),
            "definicion": "Representación de datos en un formato estructurado, a menudo utilizado en aplicaciones web.",
            "traduccion": "Representation of data in a structured format, often used in web applications."},
        "function_call": {
            "categoria": ("Funciones",),
            "definicion": "Invocación de una función para ejecutar su código.",
            "traduccion": "Invocation of a function to execute its code."},
        "force": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Método para forzar la ejecución de un proceso o función.",
            "traduccion": "Method to force the execution of a process or function."},
        "function_pointer": {
            "categoria": ("Funciones",),
            "definicion": "Referencia a una función que puede ser pasada como argumento.",
            "traduccion": "Reference to a function that can be passed as an argument."},
        "float_precision": {
            "categoria": ("Tipos de datos",),
            "definicion": "Precisión de un número en punto flotante, que afecta la exactitud de los cálculos.",
            "traduccion": "Precision of a floating-point number, affecting the accuracy of calculations."},
        "format_error": {
            "categoria": ("Manejo de errores",),
            "definicion": "Error que ocurre al formatear datos de manera incorrecta.",
            "traduccion": "Error that occurs when formatting data incorrectly."},
        "file_write": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Operación que escribe datos en un archivo.",
            "traduccion": "Operation that writes data to a file."},
        "fibonacci_search": {
            "categoria": ("Algoritmos de búsqueda",),
            "definicion": "Algoritmo de búsqueda que utiliza la secuencia de Fibonacci para encontrar elementos.",
            "traduccion": "Search algorithm that uses the Fibonacci sequence to find elements."},
        "filter_map": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Combinación de la funcionalidad de filter y map en una operación.",
            "traduccion": "Combination of the functionality of filter and map in a single operation."}},
    
    "g": {
        "getattr": {
            "categoria": ("Manejo de objetos",),
            "definicion": "Devuelve el valor de un atributo de un objeto.",
            "traduccion": "Returns the value of an object's attribute."},
        "globals": {
            "categoria": ("Espacios de nombres",),
            "definicion": "Devuelve un diccionario con todas las variables globales del programa.",
            "traduccion": "Returns a dictionary of all global variables in the program."},
        "groupby": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Agrupa datos basándose en una clave específica.",
            "traduccion": "Groups data based on a specific key."},
        "gc": {
            "categoria": ("Gestión de memoria",),
            "definicion": "Módulo que proporciona control sobre el recolector de basura.",
            "traduccion": "Module that provides control over garbage collection."},
        "ge": {
            "categoria": ("Operadores",),
            "definicion": "Devuelve True si el primer valor es mayor o igual que el segundo.",
            "traduccion": "Returns True if the first value is greater than or equal to the second."},
        "gzip": {
            "categoria": ("Compresión de datos",),
            "definicion": "Módulo para comprimir y descomprimir archivos en formato gzip.",
            "traduccion": "Module for compressing and decompressing files in gzip format."},
        "getpass": {
            "categoria": ("Seguridad",),
            "definicion": "Permite la entrada de contraseñas de manera segura.",
            "traduccion": "Allows for secure password input."},
        "getsizeof": {
            "categoria": ("Gestión de memoria",),
            "definicion": "Devuelve el tamaño en bytes de un objeto.",
            "traduccion": "Returns the size in bytes of an object."},
        "genericpath": {
            "categoria": ("Manejo de archivos",),
            "definicion": "Módulo que proporciona funciones comunes para la manipulación de rutas.",
            "traduccion": "Module that provides common functions for path manipulation."},
        "get": {
            "categoria": ("Diccionarios",),
            "definicion": "Obtiene el valor de una clave en un diccionario.",
            "traduccion": "Gets the value of a key in a dictionary."},
        "get_ipython": {
            "categoria": ("Entornos interactivos",),
            "definicion": "Devuelve la instancia actual de IPython activa.",
            "traduccion": "Returns the current active IPython instance."},
        "gettext": {
            "categoria": ("Internacionalización",),
            "definicion": "Módulo que facilita la traducción de textos en aplicaciones.",
            "traduccion": "Module that facilitates text translation in applications."},
        "get_event_loop": {
            "categoria": ("Programación asíncrona",),
            "definicion": "Devuelve el bucle de eventos actualmente en ejecución.",
            "traduccion": "Returns the currently running event loop."},
        "getcwd": {
            "categoria": ("Sistema operativo",),
            "definicion": "Devuelve el directorio de trabajo actual.",
            "traduccion": "Returns the current working directory."},
        "genfromtxt": {
            "categoria": ("Procesamiento de datos",),
            "definicion": "Carga datos desde un archivo de texto, con opciones avanzadas de control.",
            "traduccion": "Loads data from a text file with advanced control options."},
        "google_auth": {
            "categoria": ("Autenticación",),
            "definicion": "Biblioteca para manejar la autenticación de Google en aplicaciones.",
            "traduccion": "Library for handling Google authentication in applications."},
        "grayscale": {
            "categoria": ("Procesamiento de imágenes",),
            "definicion": "Convierte una imagen a escala de grises.",
            "traduccion": "Converts an image to grayscale."},
        "grid_search": {
            "categoria": ("Optimización",),
            "definicion": "Método para encontrar los mejores hiperparámetros de un modelo.",
            "traduccion": "Method for finding the best hyperparameters for a model."},
        "graphlib": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Módulo que proporciona herramientas para manipular grafos.",
            "traduccion": "Module that provides tools for manipulating graphs."},
        "greatest_common_divisor": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve el máximo común divisor de dos números.",
            "traduccion": "Returns the greatest common divisor of two numbers."},
        "generate_token": {
            "categoria": ("Seguridad",),
            "definicion": "Genera un token de autenticación único.",
            "traduccion": "Generates a unique authentication token."},
        "gradient": {
            "categoria": ("Matemáticas",),
            "definicion": "Calcula el gradiente de una función.",
            "traduccion": "Calculates the gradient of a function."},
        "gzip_file": {
            "categoria": ("Compresión de datos",),
            "definicion": "Crea o lee un archivo comprimido en formato gzip.",
            "traduccion": "Creates or reads a file compressed in gzip format."},
        "gui_toolkit": {
            "categoria": ("Interfaces gráficas",),
            "definicion": "Conjunto de herramientas para crear interfaces gráficas.",
            "traduccion": "Toolkit for creating graphical user interfaces."},
        "gaussian_filter": {
            "categoria": ("Procesamiento de imágenes",),
            "definicion": "Aplica un filtro gaussiano para suavizar una imagen.",
            "traduccion": "Applies a Gaussian filter to smooth an image."},
        "get_config": {
            "categoria": ("Configuraciones",),
            "definicion": "Obtiene configuraciones del entorno o de una aplicación.",
            "traduccion": "Gets environment or application configurations."},
        "group_indices": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Devuelve los índices de elementos agrupados por una clave.",
            "traduccion": "Returns the indices of elements grouped by a key."},
        "generate_password": {
            "categoria": ("Seguridad",),
            "definicion": "Crea una contraseña aleatoria según criterios definidos.",
            "traduccion": "Generates a random password based on defined criteria."},
        "genetic_algorithm": {
            "categoria": ("Inteligencia artificial",),
            "definicion": "Algoritmo basado en la selección y evolución genética.",
            "traduccion": "Algorithm based on genetic selection and evolution."},
        "get_frame": {
            "categoria": ("Depuración",),
            "definicion": "Obtiene el marco actual de ejecución en una pila de llamadas.",
            "traduccion": "Gets the current execution frame in a call stack."},
        "get_headers": {
            "categoria": ("Redes",),
            "definicion": "Obtiene los encabezados de una solicitud HTTP.",
            "traduccion": "Gets the headers of an HTTP request."},
        "get_nodes": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Devuelve los nodos de un grafo.",
            "traduccion": "Returns the nodes of a graph."},
        "global_average": {
            "categoria": ("Estadísticas",),
            "definicion": "Calcula el promedio global de un conjunto de datos.",
            "traduccion": "Calculates the global average of a dataset."},
        "gradient_descent": {
            "categoria": ("Aprendizaje automático",),
            "definicion": "Método para minimizar funciones mediante gradientes.",
            "traduccion": "Method for minimizing functions using gradients."},
        "get_meta_data": {
            "categoria": ("Bases de datos",),
            "definicion": "Obtiene los metadatos asociados a una base de datos.",
            "traduccion": "Gets metadata associated with a database."},
        "generate_keys": {
            "categoria": ("Seguridad",),
            "definicion": "Genera claves públicas y privadas para criptografía.",
            "traduccion": "Generates public and private keys for cryptography."},
        "get_prime_numbers": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve una lista de números primos en un rango dado.",
            "traduccion": "Returns a list of prime numbers within a given range."},
        "generate_report": {
            "categoria": ("Automatización",),
            "definicion": "Crea un informe basado en datos analizados.",
            "traduccion": "Generates a report based on analyzed data."},
        "graph_visualizer": {
            "categoria": ("Visualización",),
            "definicion": "Herramienta para crear representaciones gráficas de datos.",
            "traduccion": "Tool for creating graphical data representations."},
        "grid_display": {
            "categoria": ("Interfaces gráficas",),
            "definicion": "Crea una cuadrícula para organizar elementos visuales.",
            "traduccion": "Creates a grid to organize visual elements."},
        "get_local_time": {
            "categoria": ("Fechas y horas",),
            "definicion": "Obtiene la hora local del sistema.",
            "traduccion": "Gets the local system time."},
        "generate_uuid": {
            "categoria": ("Identificadores",),
            "definicion": "Crea un identificador único universal.",
            "traduccion": "Generates a universally unique identifier."},
        "get_timezone": {
            "categoria": ("Fechas y horas",),
            "definicion": "Devuelve la zona horaria actual.",
            "traduccion": "Returns the current timezone."},
        "get_subgraph": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Obtiene un subgrafo a partir de un grafo existente.",
            "traduccion": "Gets a subgraph from an existing graph."},
        "generate_pie_chart": {
            "categoria": ("Visualización",),
            "definicion": "Crea un gráfico de pastel basado en datos.",
            "traduccion": "Generates a pie chart based on data."},
        "get_histogram": {
            "categoria": ("Estadísticas",),
            "definicion": "Devuelve el histograma de un conjunto de datos.",
            "traduccion": "Returns the histogram of a dataset."},
        "gradient_boosting": {
            "categoria": ("Aprendizaje automático",),
            "definicion": "Técnica para mejorar modelos de predicción.",
            "traduccion": "Technique for improving prediction models."},
        "get_child_nodes": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Devuelve los nodos hijos de un nodo específico.",
            "traduccion": "Returns the child nodes of a specific node."},
        "generate_test_cases": {
            "categoria": ("Pruebas",),
            "definicion": "Genera casos de prueba para un programa o aplicación.",
            "traduccion": "Generates test cases for a program or application."},
        "get_unique_values": {
            "categoria": ("Manipulación de datos",),
            "definicion": "Devuelve los valores únicos de una lista o conjunto.",
            "traduccion": "Returns the unique values of a list or set."},
        "generate_bar_chart": {
            "categoria": ("Visualización",),
            "definicion": "Crea un gráfico de barras basado en datos.",
            "traduccion": "Generates a bar chart based on data."},
        "generate_heatmap": {
            "categoria": ("Visualización",),
            "definicion": "Crea un mapa de calor para representar datos.",
            "traduccion": "Generates a heatmap to represent data."},
        "generate_3d_plot": {
            "categoria": ("Visualización",),
            "definicion": "Crea una gráfica tridimensional de datos.",
            "traduccion": "Generates a three-dimensional plot of data."},
        "get_function_signature": {
            "categoria": ("Depuración",),
            "definicion": "Devuelve la firma de una función.",
            "traduccion": "Returns the signature of a function."},
        "global_variables": {
            "categoria": ("Espacios de nombres",),
            "definicion": "Lista todas las variables globales en el espacio actual.",
            "traduccion": "Lists all global variables in the current space."},
        "generate_random_seed": {
            "categoria": ("Matemáticas",),
            "definicion": "Crea una semilla aleatoria para inicializar generadores.",
            "traduccion": "Generates a random seed for initializing generators."},
        "generate_latex_table": {
            "categoria": ("Automatización",),
            "definicion": "Crea una tabla formateada en LaTeX.",
            "traduccion": "Generates a formatted table in LaTeX."},
        "generate_hash": {
            "categoria": ("Seguridad",),
            "definicion": "Crea un hash seguro de un dato o archivo.",
            "traduccion": "Generates a secure hash of data or a file."},
        "generate_json_schema": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Crea un esquema JSON para validar datos.",
            "traduccion": "Generates a JSON schema for data validation."}},
    "h": {
        "hash": {
            "categoria": ("Matemáticas",),
            "definicion": "Devuelve el valor hash de un objeto.",
            "traduccion": "Returns the hash value of an object."},
        "help": {
            "categoria": ("Documentación",),
            "definicion": "Muestra la ayuda de un módulo, función o clase.",
            "traduccion": "Displays the help information of a module, function, or class."},
        "header": {
            "categoria": ("Redes",),
            "definicion": "Parte inicial de un paquete de datos que contiene información sobre el mismo.",
            "traduccion": "Initial part of a data packet that contains information about it."},
        "host": {
            "categoria": ("Redes",),
            "definicion": "Computadora o dispositivo que se conecta a una red.",
            "traduccion": "Computer or device that connects to a network."},
        "hyperlink": {
            "categoria": ("Internet",),
            "definicion": "Vínculo en una página web que lleva a otra página o recurso.",
            "traduccion": "Link in a webpage that leads to another page or resource."},
        "hashlib": {
            "categoria": ("Seguridad",),
            "definicion": "Biblioteca de Python que proporciona algoritmos de hash.",
            "traduccion": "Python library that provides hash algorithms."},
        "hamming_distance": {
            "categoria": ("Teoría de la información",),
            "definicion": "Mide el número de posiciones en las que dos cadenas de texto difieren.",
            "traduccion": "Measures the number of positions where two strings differ."},
        "heap": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Estructura de datos basada en un árbol binario completo.",
            "traduccion": "Data structure based on a complete binary tree."},
        "hash_table": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Estructura que asocia claves con valores usando una función hash.",
            "traduccion": "Structure that maps keys to values using a hash function."},
        "http_request": {
            "categoria": ("Redes",),
            "definicion": "Solicitud realizada por un cliente a un servidor web.",
            "traduccion": "Request made by a client to a web server."},
        "http_response": {
            "categoria": ("Redes",),
            "definicion": "Respuesta del servidor a una solicitud HTTP.",
            "traduccion": "Response from the server to an HTTP request."},
        "host_name": {
            "categoria": ("Redes",),
            "definicion": "Nombre asignado a un dispositivo en una red.",
            "traduccion": "Name assigned to a device in a network."},
        "hash_map": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Estructura que asocia claves y valores, similar a un diccionario.",
            "traduccion": "Structure that maps keys to values, similar to a dictionary."},
        "hadoop": {
            "categoria": ("Big Data",),
            "definicion": "Framework de código abierto para el procesamiento distribuido de grandes conjuntos de datos.",
            "traduccion": "Open-source framework for the distributed processing of large datasets."},
        "http_method": {
            "categoria": ("Redes",),
            "definicion": "Método que define la acción solicitada en una petición HTTP.",
            "traduccion": "Method that defines the action requested in an HTTP request."},
        "hash_function": {
            "categoria": ("Criptografía",),
            "definicion": "Función que toma una entrada y devuelve un valor hash de longitud fija.",
            "traduccion": "Function that takes an input and returns a fixed-length hash value."},
        "hibernate": {
            "categoria": ("Base de datos",),
            "definicion": "Framework para mapeo objeto-relacional en Java.",
            "traduccion": "Object-relational mapping framework in Java."},
        "heuristic": {
            "categoria": ("Algoritmos",),
            "definicion": "Método de resolución de problemas basado en la experiencia y la aproximación.",
            "traduccion": "Problem-solving method based on experience and approximation."},
        "http_code": {
            "categoria": ("Redes",),
            "definicion": "Código de estado devuelto por el servidor en una solicitud HTTP.",
            "traduccion": "Status code returned by the server in an HTTP request."},
        "host_ip": {
            "categoria": ("Redes",),
            "definicion": "Dirección IP asignada a un dispositivo en una red.",
            "traduccion": "IP address assigned to a device in a network."},
        "hashing_algorithm": {
            "categoria": ("Criptografía",),
            "definicion": "Algoritmo utilizado para convertir datos en un valor hash.",
            "traduccion": "Algorithm used to convert data into a hash value."},
        "header_field": {
            "categoria": ("Redes",),
            "definicion": "Campo en un encabezado de protocolo que contiene información adicional.",
            "traduccion": "Field in a protocol header that contains additional information."},
        "hosted_service": {
            "categoria": ("Servicios en la nube",),
            "definicion": "Servicio que se aloja en la nube y se accede a través de Internet.",
            "traduccion": "Service hosted in the cloud and accessed via the internet."},

        "hybrid_cloud": {
            "categoria": ("Servicios en la nube",),
            "definicion": "Modelo de computación en la nube que combina recursos privados y públicos.",
            "traduccion": "Cloud computing model that combines private and public resources."},
        "hexadecimal": {
            "categoria": ("Matemáticas",),
            "definicion": "Sistema numérico en base 16.",
            "traduccion": "Numerical system in base 16."},
        "hash_set": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Conjunto que almacena elementos de forma no ordenada utilizando un hash.",
            "traduccion": "Set that stores elements in an unordered fashion using a hash."},
        "high_order_function": {
            "categoria": ("Funciones",),
            "definicion": "Función que toma una o más funciones como argumentos o devuelve una función.",
            "traduccion": "Function that takes one or more functions as arguments or returns a function."},
        "hmac": {
            "categoria": ("Criptografía",),
            "definicion": "Código de autenticación de mensaje basado en hash.",
            "traduccion": "Hash-based message authentication code."},
        "hashable": {
            "categoria": ("Python",),
            "definicion": "Propiedad de un objeto que permite su uso como clave en un diccionario.",
            "traduccion": "Property of an object that allows it to be used as a key in a dictionary."},
        "http_session": {
            "categoria": ("Redes",),
            "definicion": "Sesión que mantiene el estado entre las solicitudes HTTP de un cliente.",
            "traduccion": "Session that maintains state between HTTP requests from a client."},
        "hypertext": {
            "categoria": ("Internet",),
            "definicion": "Texto que contiene enlaces a otros textos o recursos.",
            "traduccion": "Text that contains links to other texts or resources."},
        "http_2": {
            "categoria": ("Redes",),
            "definicion": "Protocolo de red que mejora el rendimiento de HTTP.",
            "traduccion": "Network protocol that improves HTTP performance."},
        "hls": {
            "categoria": ("Redes",),
            "definicion": "Sistema de transmisión de video en tiempo real sobre HTTP.",
            "traduccion": "Real-time video streaming system over HTTP."},
        "hashmap": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Implementación de un mapa clave-valor utilizando una función hash.",
            "traduccion": "Implementation of a key-value map using a hash function."},
        "home_directory": {
            "categoria": ("Sistemas operativos",),
            "definicion": "Directorio principal del usuario en un sistema.",
            "traduccion": "Main user directory in a system."},
        "http_redirect": {
            "categoria": ("Redes",),
            "definicion": "Redirección de una solicitud HTTP a una nueva URL.",
            "traduccion": "Redirecting an HTTP request to a new URL."},
        "html": {
            "categoria": ("Internet",),
            "definicion": "Lenguaje de marcado utilizado para crear páginas web.",
            "traduccion": "Markup language used to create web pages."},
        "header_file": {
            "categoria": ("Programación",),
            "definicion": "Archivo que contiene declaraciones de funciones y macros.",
            "traduccion": "File that contains function declarations and macros."},
        "hdfs": {
            "categoria": ("Big Data",),
            "definicion": "Sistema de archivos distribuido utilizado por Hadoop.",
            "traduccion": "Distributed file system used by Hadoop."},
        "hard_link": {
            "categoria": ("Sistemas operativos",),
            "definicion": "Enlace a un archivo que apunta directamente a los datos almacenados en disco.",
            "traduccion": "Link to a file that points directly to the data stored on disk."},
        "hashing": {
            "categoria": ("Criptografía",),
            "definicion": "Proceso de aplicar una función hash a los datos.",
            "traduccion": "Process of applying a hash function to data."},
        "http_404": {
            "categoria": ("Redes",),
            "definicion": "Código de estado HTTP que indica que la página no se encuentra.",
            "traduccion": "HTTP status code indicating that the page is not found."},
        "hypervisor": {
            "categoria": ("Virtualización",),
            "definicion": "Software que permite ejecutar máquinas virtuales en un sistema físico.",
            "traduccion": "Software that allows running virtual machines on a physical system."},
        "http_header": {
            "categoria": ("Redes",),
            "definicion": "Información adicional contenida en una solicitud o respuesta HTTP.",
            "traduccion": "Additional information contained in an HTTP request or response."},
        "http_client": {
            "categoria": ("Redes",),
            "definicion": "Software que realiza solicitudes HTTP a servidores web.",
            "traduccion": "Software that makes HTTP requests to web servers."},
        "hping": {
            "categoria": ("Redes",),
            "definicion": "Herramienta de red para pruebas de seguridad y auditoría.",
            "traduccion": "Network tool for security testing and auditing."},
        "hash_collision": {
            "categoria": ("Criptografía",),
            "definicion": "Situación donde dos entradas diferentes tienen el mismo valor hash.",
            "traduccion": "Situation where two different inputs have the same hash value."},
        "head": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Elemento que aparece primero en una lista enlazada.",
            "traduccion": "First element in a linked list."},
        "heap_sort": {
            "categoria": ("Algoritmos",),
            "definicion": "Algoritmo de ordenamiento basado en la estructura de heap.",
            "traduccion": "Sorting algorithm based on the heap data structure."},
        "http_server": {
            "categoria": ("Redes",),
            "definicion": "Software que maneja solicitudes HTTP y las responde.",
            "traduccion": "Software that handles HTTP requests and responds to them."},
        "hashing_algorithm": {
            "categoria": ("Criptografía",),
            "definicion": "Algoritmo usado para calcular un valor hash a partir de datos.",
            "traduccion": "Algorithm used to compute a hash value from data."},
        "huffman_code": {
            "categoria": ("Compresión",),
            "definicion": "Algoritmo de compresión que asigna códigos más cortos a los caracteres más frecuentes.",
            "traduccion": "Compression algorithm that assigns shorter codes to more frequent characters."},
        "http_request_method": {
            "categoria": ("Redes",),
            "definicion": "Métodos HTTP usados para interactuar con un servidor.",
            "traduccion": "HTTP methods used to interact with a server."},
        "hash_table_collision": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Situación donde dos claves hash diferentes tienen el mismo índice en la tabla.",
            "traduccion": "Situation where two different hash keys have the same index in the table."},
        "hosted_application": {
            "categoria": ("Servicios en la nube",),
            "definicion": "Aplicación que se aloja en un servidor remoto y se accede vía Internet.",
            "traduccion": "Application hosted on a remote server and accessed over the internet."},
        "http_redirect_status": {
            "categoria": ("Redes",),
            "definicion": "Código HTTP que indica que la página ha sido movida a otra URL.",
            "traduccion": "HTTP code indicating that the page has been moved to another URL."},
        "hypervisor_type": {
            "categoria": ("Virtualización",),
            "definicion": "Tipo de software de virtualización, como tipo 1 o tipo 2.",
            "traduccion": "Type of virtualization software, such as type 1 or type 2."},
        "head_pointer": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Puntero que apunta al primer elemento en una estructura de datos.",
            "traduccion": "Pointer that points to the first element in a data structure."},
        "hash_function_collision": {
            "categoria": ("Criptografía",),
            "definicion": "Problema en que dos entradas diferentes generan el mismo valor hash.",
            "traduccion": "Problem where two different inputs generate the same hash value."},
        "http_response_code": {
            "categoria": ("Redes",),
            "definicion": "Código de respuesta enviado por el servidor en respuesta a una solicitud HTTP.",
            "traduccion": "Response code sent by the server in reply to an HTTP request."},
        "hardware_abstraction_layer": {
            "categoria": ("Sistemas operativos",),
            "definicion": "Capa de software que oculta detalles del hardware al sistema operativo.",
            "traduccion": "Software layer that hides hardware details from the operating system."},
        "hash_set_operation": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Operación que realiza una acción sobre un conjunto basado en hash.",
            "traduccion": "Operation that performs an action on a hash-based set."},
        "hostname_resolution": {
            "categoria": ("Redes",),
            "definicion": "Proceso de convertir un nombre de dominio en una dirección IP.",
            "traduccion": "Process of converting a domain name into an IP address."},
        "http_session_management": {
            "categoria": ("Redes",),
            "definicion": "Manejo de la información de sesión entre cliente y servidor.",
            "traduccion": "Managing session information between client and server."},
        "heap_memory": {
            "categoria": ("Sistemas operativos",),
            "definicion": "Memoria dinámica usada por las aplicaciones durante la ejecución.",
            "traduccion": "Dynamic memory used by applications during execution."},
        "hashing_attack": {
            "categoria": ("Seguridad",),
            "definicion": "Técnica que intenta encontrar colisiones de valores hash para vulnerar la seguridad.",
            "traduccion": "Technique that attempts to find hash collisions to break security."},
        "http_proxy": {
            "categoria": ("Redes",),
            "definicion": "Servidor que actúa como intermediario entre el cliente y el servidor real.",
            "traduccion": "Server that acts as an intermediary between the client and the real server."},
        "heartbeat_signal": {
            "categoria": ("Redes",),
            "definicion": "Señal periódica enviada para indicar que un sistema está activo y funcionando.",
            "traduccion": "Periodic signal sent to indicate that a system is active and running."},
        "http_verbs": {
            "categoria": ("Redes",),
            "definicion": "Acciones que define una solicitud HTTP, como GET, POST, PUT.",
            "traduccion": "Actions defined by an HTTP request, such as GET, POST, PUT."},
        "http_cookie": {
            "categoria": ("Redes",),
            "definicion": "Pequeño archivo que un servidor envía al navegador para almacenar información de usuario.",
            "traduccion": "Small file sent by a server to the browser to store user information."},
        "hash_algorithm": {
            "categoria": ("Criptografía",),
            "definicion": "Algoritmo usado para mapear datos de longitud variable a una longitud fija.",
            "traduccion": "Algorithm used to map variable-length data to a fixed length."},
        "hubs": {
            "categoria": ("Redes",),
            "definicion": "Dispositivo de red que conecta varios dispositivos en una red de área local.",
            "traduccion": "Network device that connects multiple devices in a local area network."},
        "http_timeout": {
            "categoria": ("Redes",),
            "definicion": "Tiempo de espera antes de que una solicitud HTTP sea considerada fallida.",
            "traduccion": "Time limit before an HTTP request is considered to have failed."},
        "hyperthreading": {
            "categoria": ("Hardware",),
            "definicion": "Tecnología que permite a un procesador ejecutar múltiples hilos simultáneamente.",
            "traduccion": "Technology that allows a processor to run multiple threads simultaneously."},
        "http_request_header": {
            "categoria": ("Redes",),
            "definicion": "Parte de una solicitud HTTP que contiene información adicional sobre la solicitud.",
            "traduccion": "Part of an HTTP request that contains additional information about the request."},
        "hashable_object": {
            "categoria": ("Python",),
            "definicion": "Objeto que puede ser usado como clave en un diccionario debido a su valor hash.",
            "traduccion": "Object that can be used as a key in a dictionary due to its hash value."},
        "http_error": {
            "categoria": ("Redes",),
            "definicion": "Error que ocurre durante la comunicación HTTP entre cliente y servidor.",
            "traduccion": "Error that occurs during HTTP communication between client and server."},
        "hard_drive": {
            "categoria": ("Hardware",),
            "definicion": "Dispositivo de almacenamiento de datos en formato magnético.",
            "traduccion": "Data storage device in magnetic format."},
        "hashmap_lookup": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Operación de búsqueda en una tabla hash.",
            "traduccion": "Lookup operation in a hash table."},
        "http_redirect_url": {
            "categoria": ("Redes",),
            "definicion": "URL a la que se redirige una solicitud HTTP.",
            "traduccion": "URL to which an HTTP request is redirected."},
        "http_response_status": {
            "categoria": ("Redes",),
            "definicion": "Código que indica el estado de una respuesta HTTP.",
            "traduccion": "Code that indicates the status of an HTTP response."},
        "hash_map_insert": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Operación para insertar una clave y un valor en una tabla hash.",
            "traduccion": "Operation to insert a key and value into a hash table."},
        "http_compression": {
            "categoria": ("Redes",),
            "definicion": "Técnica para reducir el tamaño de los datos transmitidos a través de HTTP.",
            "traduccion": "Technique to reduce the size of data transmitted over HTTP."},
        "http_method": {
            "categoria": ("Redes",),
            "definicion": "Método de solicitud en el protocolo HTTP, como GET, POST, PUT.",
            "traduccion": "Request method in the HTTP protocol, such as GET, POST, PUT."},
        "http_status_code": {
            "categoria": ("Redes",),
            "definicion": "Código que indica el resultado de una solicitud HTTP.",
            "traduccion": "Code indicating the result of an HTTP request."},
        "hash_function": {
            "categoria": ("Criptografía",),
            "definicion": "Función que mapea datos de entrada a un valor de longitud fija.",
            "traduccion": "Function that maps input data to a fixed-length value."},
        "http_resource": {
            "categoria": ("Redes",),
            "definicion": "Recurso al que se accede mediante HTTP, como una página web o archivo.",
            "traduccion": "Resource accessed via HTTP, such as a webpage or file."},
        "http_get": {
            "categoria": ("Redes",),
            "definicion": "Método HTTP usado para solicitar datos de un servidor.",
            "traduccion": "HTTP method used to request data from a server."},
        "hardware_interface": {
            "categoria": ("Hardware",),
            "definicion": "Conjunto de señales que permiten la comunicación entre un dispositivo y el hardware del sistema.",
            "traduccion": "Set of signals that enable communication between a device and the system hardware."},
        "http_head": {
            "categoria": ("Redes",),
            "definicion": "Método HTTP utilizado para obtener solo los encabezados de una respuesta.",}},
    "i": {
        "immutable": {
            "categoria": ("Python",),
            "definicion": "Objeto cuya información no puede ser modificada después de ser creado.",
            "traduccion": "Object whose information cannot be modified after creation."},
        "index": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Posición de un elemento en una lista o arreglo.",
            "traduccion": "Position of an element in a list or array."},
        "input": {
            "categoria": ("Programación",),
            "definicion": "Datos proporcionados por el usuario o un sistema.",
            "traduccion": "Data provided by the user or a system."},
        "instance": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Un objeto creado a partir de una clase.",
            "traduccion": "An object created from a class."},
        "inheritance": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Mecanismo que permite a una clase derivada heredar atributos y métodos de una clase base.",
            "traduccion": "Mechanism that allows a derived class to inherit attributes and methods from a base class."},
        "interface": {
            "categoria": ("Programación",),
            "definicion": "Conjunto de métodos que una clase debe implementar.",
            "traduccion": "Set of methods that a class must implement."},
        "instance_method": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Método que opera sobre una instancia de una clase.",
            "traduccion": "Method that operates on an instance of a class."},
        "immutable_set": {
            "categoria": ("Python",),
            "definicion": "Conjunto cuyo contenido no puede ser alterado una vez creado.",
            "traduccion": "Set whose content cannot be altered once created."},
        "increment": {
            "categoria": ("Matemáticas",),
            "definicion": "Aumento en el valor de una variable en una unidad o cantidad específica.",
            "traduccion": "Increase in the value of a variable by one unit or specific amount."},
        "input_validation": {
            "categoria": ("Seguridad",),
            "definicion": "Proceso de verificar que los datos ingresados sean correctos y seguros.",
            "traduccion": "Process of verifying that input data is correct and secure."},
        "indexing": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Técnica para acceder a un elemento en una lista mediante su índice.",
            "traduccion": "Technique for accessing an element in a list using its index."},
        "insertion_sort": {
            "categoria": ("Algoritmos",),
            "definicion": "Algoritmo de ordenamiento que construye la lista ordenada uno a uno.",
            "traduccion": "Sorting algorithm that builds the sorted list one item at a time."},
        "integer": {
            "categoria": ("Matemáticas",),
            "definicion": "Número sin parte decimal.",
            "traduccion": "Number without a decimal part."},
        "iterable": {
            "categoria": ("Python",),
            "definicion": "Objeto que puede ser iterado en un ciclo.",
            "traduccion": "Object that can be iterated over in a loop."},
        "identifier": {
            "categoria": ("Programación",),
            "definicion": "Nombre que se usa para identificar variables, funciones y clases en el código.",
            "traduccion": "Name used to identify variables, functions, and classes in code."},
        "iteration": {
            "categoria": ("Programación",),
            "definicion": "Proceso de ejecutar un conjunto de instrucciones repetidamente.",
            "traduccion": "Process of executing a set of instructions repeatedly."},
        "IP_address": {
            "categoria": ("Redes",),
            "definicion": "Dirección única asignada a cada dispositivo en una red.",
            "traduccion": "Unique address assigned to each device in a network."},
        "if_statement": {
            "categoria": ("Programación",),
            "definicion": "Condicional que ejecuta un bloque de código solo si se cumple una condición.",
            "traduccion": "Conditional that executes a block of code only if a condition is true."},
        "interface_class": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Clase que define un conjunto de métodos sin implementación.",
            "traduccion": "Class that defines a set of methods without implementation."},
        "input_device": {
            "categoria": ("Hardware",),
            "definicion": "Dispositivo que permite a un usuario enviar datos a una computadora.",
            "traduccion": "Device that allows a user to send data to a computer."},
        "introspection": {
            "categoria": ("Python",),
            "definicion": "Proceso de examinar los atributos de un objeto en tiempo de ejecución.",
            "traduccion": "Process of examining an object's attributes at runtime."},
        "instance_variable": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Variable asociada a una instancia de una clase.",
            "traduccion": "Variable associated with an instance of a class."},
        "index_out_of_bounds": {
            "categoria": ("Programación",),
            "definicion": "Error que ocurre cuando se intenta acceder a un índice que no existe en una lista.",
            "traduccion": "Error that occurs when trying to access an index that does not exist in a list."},
        "input_output": {
            "categoria": ("Sistemas operativos",),
            "definicion": "Proceso de recibir datos de entrada y devolver resultados de salida.",
            "traduccion": "Process of receiving input data and returning output results."},
        "inplace": {
            "categoria": ("Algoritmos",),
            "definicion": "Operación que se realiza directamente sobre los datos sin usar espacio adicional.",
            "traduccion": "Operation performed directly on the data without using additional space."},
        "inherit": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Acción de obtener propiedades y métodos de una clase base.",
            "traduccion": "Action of inheriting properties and methods from a base class."},
        "index_of": {
            "categoria": ("Programación",),
            "definicion": "Método que devuelve la posición de un elemento en una lista o arreglo.",
            "traduccion": "Method that returns the position of an element in a list or array."},
        "instruction_set": {
            "categoria": ("Computación",),
            "definicion": "Conjunto de instrucciones que una CPU puede ejecutar.",
            "traduccion": "Set of instructions that a CPU can execute."},
        "iterable_object": {
            "categoria": ("Python",),
            "definicion": "Objeto que puede ser recorrido utilizando un ciclo.",
            "traduccion": "Object that can be iterated over using a loop."},
        "image_processing": {
            "categoria": ("Computación",),
            "definicion": "Procesamiento de imágenes para mejorarlas o extraer información.",
            "traduccion": "Processing of images to improve them or extract information."},
        "indirect_addressing": {
            "categoria": ("Redes",),
            "definicion": "Técnica que usa una dirección intermedia para acceder a los datos.",
            "traduccion": "Technique that uses an intermediate address to access data."},
        "instruction_pointer": {
            "categoria": ("Computación",),
            "definicion": "Registro que almacena la dirección de la próxima instrucción a ejecutar.",
            "traduccion": "Register that stores the address of the next instruction to be executed."},
        "integrated_circuit": {
            "categoria": ("Hardware",),
            "definicion": "Circuito electrónico que contiene varios componentes en un solo chip.",
            "traduccion": "Electronic circuit that contains multiple components on a single chip."},
        "integer_overflow": {
            "categoria": ("Seguridad",),
            "definicion": "Error que ocurre cuando un número excede el límite de almacenamiento de una variable.",
            "traduccion": "Error that occurs when a number exceeds the storage limit of a variable."},
        "identifier_name": {
            "categoria": ("Programación",),
            "definicion": "Nombre que se asigna a un identificador, como una variable o función.",
            "traduccion": "Name assigned to an identifier, such as a variable or function."},
        "input_buffer": {
            "categoria": ("Computación",),
            "definicion": "Área de almacenamiento temporal de datos de entrada.",
            "traduccion": "Temporary storage area for input data."},
        "interactive_mode": {
            "categoria": ("Programación",),
            "definicion": "Modo en el que el usuario interactúa directamente con el sistema para ejecutar comandos.",
            "traduccion": "Mode in which the user interacts directly with the system to execute commands."},
        "inverse": {
            "categoria": ("Matemáticas",),
            "definicion": "Operación que devuelve el recíproco de un número o función.",
            "traduccion": "Operation that returns the reciprocal of a number or function."},
        "inbox": {
            "categoria": ("Redes",),
            "definicion": "Carpeta de entrada de un sistema de correo electrónico.",
            "traduccion": "Inbox folder of an email system."},
        "invisible": {
            "categoria": ("Programación",),
            "definicion": "Propiedad de un objeto que no es visible en la interfaz del usuario.",
            "traduccion": "Property of an object that is not visible in the user interface."},
        "incremental_search": {
            "categoria": ("Algoritmos",),
            "definicion": "Método de búsqueda que encuentra el objetivo al aumentar gradualmente la posición.",
            "traduccion": "Search method that finds the target by gradually increasing the position."},
        "instanceof": {
            "categoria": ("Programación",),
            "definicion": "Operador utilizado para verificar si un objeto es una instancia de una clase específica.",
            "traduccion": "Operator used to check if an object is an instance of a specific class."},
        "image": {
            "categoria": ("Computación",),
            "definicion": "Representación visual que se guarda en un formato digital.",
            "traduccion": "Visual representation stored in a digital format."},
        "idle": {
            "categoria": ("Sistemas operativos",),
            "definicion": "Estado de un sistema o proceso cuando está inactivo y esperando una tarea.",
            "traduccion": "State of a system or process when it is inactive and waiting for a task."},
        "input_stream": {
            "categoria": ("Programación",),
            "definicion": "Flujo de datos que entra a un programa o proceso.",
            "traduccion": "Flow of data entering a program or process."},
        "identity": {
            "categoria": ("Matemáticas",),
            "definicion": "Relación entre dos elementos que siempre se cumplen en determinadas condiciones.",
            "traduccion": "Relationship between two elements that always holds under certain conditions."},
        "inbox": {
            "categoria": ("Redes",),
            "definicion": "Área donde se reciben mensajes o datos.",
            "traduccion": "Area where messages or data are received."},
        "inner_class": {
            "categoria": ("Programación",),
            "definicion": "Clase definida dentro de otra clase.",
            "traduccion": "Class defined within another class."},
        "initialization": {
            "categoria": ("Programación",),
            "definicion": "Proceso de asignar un valor inicial a una variable o estructura.",
            "traduccion": "Process of assigning an initial value to a variable or structure."},
        "index_error": {
            "categoria": ("Programación",),
            "definicion": "Error que ocurre cuando se intenta acceder a un índice fuera de los límites de una lista.",
            "traduccion": "Error that occurs when trying to access an index out of bounds in a list."},
        "inference": {
            "categoria": ("Inteligencia artificial",),
            "definicion": "Proceso de deducir información a partir de hechos conocidos.",
            "traduccion": "Process of deducing information from known facts."},
        "indexing_error": {
            "categoria": ("Programación",),
            "definicion": "Error que ocurre al usar un índice incorrecto en una estructura de datos.",
            "traduccion": "Error that occurs when using an incorrect index in a data structure."},
        "infinite_loop": {
            "categoria": ("Programación",),
            "definicion": "Bucle que se ejecuta indefinidamente sin una condición de terminación.",
            "traduccion": "Loop that runs indefinitely without a termination condition."},
        "instance_checking": {
            "categoria": ("Programación",),
            "definicion": "Verificación de si un objeto pertenece a una clase específica.",
            "traduccion": "Checking if an object belongs to a specific class."},
        "information_system": {
            "categoria": ("Tecnología",),
            "definicion": "Sistema que recopila, procesa, almacena y distribuye información.",
            "traduccion": "System that collects, processes, stores, and distributes information."},
        "interpreter": {
            "categoria": ("Programación",),
            "definicion": "Programa que ejecuta instrucciones de un lenguaje de programación de alto nivel.",
            "traduccion": "Program that executes instructions from a high-level programming language."},
        "insertion": {
            "categoria": ("Estructuras de datos",),
            "definicion": "Operación que coloca un nuevo elemento en una estructura de datos.",
            "traduccion": "Operation that places a new element in a data structure."},
        "isolation": {
            "categoria": ("Sistemas operativos",),
            "definicion": "Proceso de mantener un entorno independiente y seguro en un sistema.",
            "traduccion": "Process of keeping an environment isolated and secure within a system."},
        "instance_variable": {
            "categoria": ("Programación",),
            "definicion": "Variable que pertenece a una instancia específica de una clase.",
            "traduccion": "Variable that belongs to a specific instance of a class."},
        "interrupt": {
            "categoria": ("Sistemas operativos",),
            "definicion": "Señal que interrumpe el flujo normal de un programa para atender un evento externo.",
            "traduccion": "Signal that interrupts the normal flow of a program to address an external event."},
        "input_validation": {
            "categoria": ("Seguridad",),
            "definicion": "Proceso de verificar que los datos ingresados sean correctos y seguros.",
            "traduccion": "Process of verifying that input data is correct and secure."},
        "instance_method": {
            "categoria": ("Programación orientada a objetos",),
            "definicion": "Método que opera sobre una instancia de una clase.",
            "traduccion": "Method that operates on an instance of a class."},
        "idempotent": {
            "categoria": ("Matemáticas",),
            "definicion": "Operación que no cambia el resultado cuando se aplica varias veces.",
            "traduccion": "Operation that does not change the result when applied multiple times."},
        "identity_function": {
            "categoria": ("Matemáticas",),
            "definicion": "Función que devuelve su entrada sin alteraciones.",
            "traduccion": "Function that returns its input without alterations."},
        "input_output": {
            "categoria": ("Sistemas operativos",),
            "definicion": "Interacción entre un sistema y el mundo exterior a través de dispositivos de entrada y salida.",
            "traduccion": "Interaction between a system and the outside world through input and output devices."},
        "interface_class": {
            "categoria": ("Programación",),
            "definicion": "Clase que define un conjunto de métodos sin implementación.",
            "traduccion": "Class that defines a set of methods without implementation."},
        "incremental": {
            "categoria": ("Programación",),
            "definicion": "Proceso que se realiza de manera gradual o en pequeñas cantidades.",
            "traduccion": "Process carried out gradually or in small amounts."},
        "incompatible": {
            "categoria": ("Computación",),
            "definicion": "Descripción de dos elementos que no pueden funcionar juntos.",
            "traduccion": "Description of two elements that cannot work together."},
        "inline": {
            "categoria": ("Programación",),
            "definicion": "Código que se inserta directamente dentro de otro, en lugar de ser llamado desde una función externa.",
            "traduccion": "Code that is inserted directly into another, instead of being called from an external function."},
        "incremental_search": {
            "categoria": ("Algoritmos",),
            "definicion": "Método que realiza búsquedas de manera progresiva.",
            "traduccion": "Method that performs searches progressively."},
        "instance_variable": {
            "categoria": ("Programación",),
            "definicion": "Variable que pertenece a una instancia específica de una clase.",
            "traduccion": "Variable that belongs to a specific instance of a class."},
        "input_error": {
            "categoria": ("Programación",),
            "definicion": "Error que ocurre cuando los datos de entrada no cumplen con los requisitos esperados.",
            "traduccion": "Error that occurs when the input data does not meet the expected requirements."},
        "input_device": {
            "categoria": ("Hardware",),
            "definicion": "Dispositivo que permite al usuario enviar información a una computadora.",
            "traduccion": "Device that allows the user to send information to a computer."},
        "isolation_level": {
            "categoria": ("Bases de datos",),
            "definicion": "Nivel de control de acceso a datos en un sistema de base de datos.",
            "traduccion": "Level of control over access to data in a database system."},
        "introspection": {
            "categoria": ("Programación",),
            "definicion": "Proceso de inspección dinámica de las características de un objeto en tiempo de ejecución.",
            "traduccion": "Process of dynamically inspecting the features of an object at runtime."},
        "indirect_addressing": {
            "categoria": ("Redes",),
            "definicion": "Técnica que utiliza una dirección intermedia para llegar al destino final.",
            "traduccion": "Technique that uses an intermediate address to reach the final destination."},
        "i/o_buffer": {
            "categoria": ("Hardware",),
            "definicion": "Área de memoria utilizada para almacenar datos durante la transferencia entre dispositivos.",
            "traduccion": "Memory area used to store data during the transfer between devices."},
        "instance_variable": {
            "categoria": ("Programación",),
            "definicion": "Variable asociada a una instancia específica de una clase.",
            "traduccion": "Variable associated with a specific instance of a class."}},
    "j": {},

    "k": {},

    "l": {},

    "m": {},

    "n": {},
    
    "o": {},

    "p": {"pop": {"definicion": "Elimina y devuelve el último elemento de una lista.", "traduccion": "Removes and returns the last element of a list."}},

    "q": {},

    "r": {"reverse": {"definicion": "Invierte el orden de los elementos en una lista.", "traduccion": "Reverses the order of elements in a list."}},

    "s": {
        "sort": {"definicion": "Ordena los elementos de una lista en orden ascendente o descendente.", 
                 "traduccion": "Sorts the elements of a list in ascending or descending order."}, 
        "split": {"definicion": "Divide una cadena en una lista de subcadenas según un delimitador.", 
                  "traduccion": "Splits a string into a list of substrings based on a delimiter."}},

    "t": {},

    "u": {},

    "v": {},

    "w": {},

    "x": {},

    "y": {},
    
    "z": {
        "zscore": {
                "categoria": ("Estadística",),
                "definicion": "Función que calcula el valor z, que indica cuántas desviaciones estándar está un valor de la media.",
                "traduccion": "Function that calculates the z-score, which indicates how many standard deviations a value is from the mean."},
        "zoneinfo": {
                "categoria": ("Manejo de tiempo",),
                "definicion": "Módulo que proporciona soporte para zonas horarias en Python.",
                "traduccion": "Module that provides support for time zones in Python."},
        "zipfile": {
                "categoria": ("Manejo de archivos",),
                "definicion": "Módulo para crear, leer y modificar archivos ZIP.",
                "traduccion": "Module for creating, reading, and modifying ZIP files."},
        "zeta": {
                "categoria": ("Matemáticas",),
                "definicion": "Función matemática que involucra una serie infinita, generalmente utilizada en teoría de números.",
                "traduccion": "Mathematical function involving an infinite series, often used in number theory."},
        "zorder": {
                "categoria": ("Gráficos",),
                "definicion": "Propiedad que determina el orden de apilamiento de los objetos gráficos en un gráfico.",
                "traduccion": "Property that determines the stacking order of graphical objects in a plot."},
        "zfill": {
                "categoria": ("Manipulación de texto",),
                "definicion": "Método que completa una cadena con ceros hasta una longitud especificada.",
                "traduccion": "Method that pads a string with zeros to a specified length."},
        "zipapp": {
                "categoria": ("Herramientas",),
                "definicion": "Herramienta que permite empaquetar aplicaciones Python en archivos zip ejecutables.",
                "traduccion": "Tool that allows packing Python applications into executable zip files."},
        "zlib.decompress": {
                "categoria": ("Compresión de datos",),
                "definicion": "Función del módulo zlib que descomprime los datos previamente comprimidos.",
                "traduccion": "Function from the zlib module that decompresses data previously compressed."},
        "zlib.compress": {
                "categoria": ("Compresión de datos",),
                "definicion": "Función del módulo zlib que comprime datos en un formato específico.",
                "traduccion": "Function from the zlib module that compresses data into a specific format."},
        "zen_of_python": {
                "categoria": ("Buenas prácticas",),
                "definicion": "Conjunto de principios que guían el diseño y desarrollo de código Python claro y eficiente.",
                "traduccion": "Set of principles that guide the design and development of clear and efficient Python code."}}

}

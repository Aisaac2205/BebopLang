
# 🚀 BebopLang – Lenguaje inspirado en Cowboy Bebop

BebopLang es un lenguaje de programación educativo creado como parte de un proyecto de compiladores. Utiliza personajes y conceptos del universo de *Cowboy Bebop* para definir su léxico, sintaxis y semántica. Este compilador está desarrollado en Python usando ANTLR4 y genera tanto la tabla de símbolos como el árbol de derivación de forma visual.


## 📁 Estructura del Proyecto

beboplang/
- ├── grammar/
- │   └── BebopLang.g4
- ├── lib/
- │   └── antlr-4.13.2-complete.jar
- ├── src/
- │   ├── __init__.py
- │   ├── main.py
- │   ├── listener.py
- │   ├── tabla_simbolos.py
- │   ├── tabla_errores.py
- │   ├── BebopLangLexer.py
- │   └── BebopLangParser.py
- ├── tests/
- │   └── test.txt

---

# 🛠 Tecnologías y Herramientas

- **Python 3.12**
- **ANTLR 4.13.2**
- **Graphviz** (para renderizar el árbol de derivación)
- **Visual Studio Code**

---

# 🔤 Características del Lenguaje

- Inspirado en el universo de *Cowboy Bebop*.
- Tokens personalizados con nombres como `SPIKE`, `JET`, `FEY`, etc.
- Palabras reservadas (mínimo 15).
- Operadores matemáticos y lógicos básicos.
- Estructuras propias para declaraciones, ciclos y condiciones.
- Árbol de derivación en formato gráfico `.png`.
- Manejo de errores léxicos y sintácticos.
  
## **Ejecutar el compilador**
- cd ../src
- python main.py

# 📈 Salidas Generadas
- arbol_derivacion.png: Imagen generada del árbol de derivación.
- Tabla de símbolos: Mostrada por consola.
- Tabla de errores: Léxicos o sintácticos, también en consola.

# 📚 Manual de Usuario
- Escribe el código en tests/test.txt.
- Ejecuta main.py desde la carpeta src.
- Consulta la consola para ver:
- Tabla de símbolos
- Tabla de errores
- Abre arbol_derivacion.png para ver el árbol sintáctico generado.

# 🧠 Lógica del Compilador
- Análisis léxico: Basado en expresiones regulares dentro de BebopLangLexer.g4.
- Análisis sintáctico: Reglas definidas en BebopLangParser.g4 mediante BNF.
- Árbol de derivación: Recorre el árbol con un Listener y lo genera con graphviz.
- Tabla de símbolos: Almacena identificadores, tipos, valores y líneas.
- Tabla de errores: Muestra errores léxicos y sintácticos con contexto.

## Ejemplo del código:
- SPIKE x = 42;
- FEY mensaje = "Hello, space cowboy!";
- JET suma = x + 10;

# ✨ Créditos
Desarrollado por Isaac Flores, programador intergaláctico en misión académica.
Este lenguaje fue forjado como parte del curso de Compiladores, con pasión, lógica y unos cuantos cafés espaciales.
Inspirado por la inigualable serie Cowboy Bebop, cada línea de código rinde homenaje a los cazadores de recompensas más icónicos del anime.

"Whatever happens, happens..." – Spike Spiegel

# 🛸 See you, Space Cowboy...

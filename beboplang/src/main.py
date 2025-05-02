# Importación de módulos estándar y de terceros necesarios para el compilador
import os
import sys
from antlr4 import *  # Herramientas de ANTLR para análisis léxico/sintáctico
from colorama import Fore, Style, init  # Colores en consola
from tabulate import tabulate  # Tablas bonitas para tokens y símbolos

# Importación de componentes específicos del compilador BebopLang
from BebopLangLexer import BebopLangLexer
from BebopLangParser import BebopLangParser
from tabla_simbolos import TablaSimbolos
from tabla_errores import TablaErrores
from listener import BebopLangListenerImpl
from ErrorListener import BebopErrorListener

# Inicializa colorama y soporte para caracteres especiales en consola
init(autoreset=True)
sys.stdout.reconfigure(encoding='utf-8')  # Permite mostrar acentos, tildes y otros caracteres

def analizar_codigo(codigo, nombre_archivo="entrada"):
    """
    Realiza el análisis del código BebopLang, mostrando:
    - Tabla de tokens generados por el lexer
    - Tabla de símbolos construida por el listener
    - Errores léxicos, sintácticos o semánticos
    - Árbol de derivación generado y guardado como imagen PNG
    """
    input_stream = InputStream(codigo)
    lexer = BebopLangLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    # 🎯 Recolectar tokens para mostrar en una tabla legible
    tokens.fill()
    lista_tokens = []
    for token in tokens.tokens:
        if token.type != Token.EOF:
            try:
                nombre_token = lexer.symbolicNames[token.type]
            except IndexError:
                nombre_token = "TOKEN_INVÁLIDO"
            lista_tokens.append([
                token.text,
                nombre_token,
                token.line,
                token.column
        ])

    print(Fore.MAGENTA + "\n📌 Tabla de Tokens:")
    print(tabulate(lista_tokens, headers=["Lexema", "Token", "Línea", "Columna"], tablefmt="fancy_grid"))

    # 🔍 Preparar análisis sintáctico con parser personalizado
    simbolos = TablaSimbolos()
    errores = TablaErrores()

    parser = BebopLangParser(tokens)
    parser.removeErrorListeners()  # 🔥 Eliminar los listeners de error por defecto
    parser.addErrorListener(BebopErrorListener(errores))  # 🎯 Listener personalizado que guarda errores

    # Construcción del árbol de análisis sintáctico (AST)
    tree = parser.programa()
    listener = BebopLangListenerImpl(simbolos, errores)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # Mostrar tabla de símbolos
    print(Fore.GREEN + "\n✅ Tabla de Símbolos:")
    simbolos.mostrar()

    # Mostrar tabla de errores detectados
    print(Fore.YELLOW + "\n⚠️ Tabla de Errores:")
    errores.mostrar()

    # Generar y guardar el árbol de derivación como imagen
    print(Fore.CYAN + "\n🌳 Generando árbol de derivación...")
    os.makedirs("output", exist_ok=True)
    path = f"output/arbol_derivacion_{nombre_archivo}"
    listener.grafo.render(path, format="png", cleanup=True)
    print(Fore.CYAN + f"📁 Guardado como: {path}.png")

def modo_archivos():
    """
    Ejecuta el compilador sobre todos los archivos .txt en la carpeta 'tests'.
    Muestra el contenido del archivo y aplica el análisis completo a cada uno.
    """
    tests_dir = os.path.join(os.path.dirname(__file__), "..", "tests")
    tests_dir = os.path.abspath(tests_dir)

    if not os.path.exists(tests_dir):
        print(Fore.RED + f"❌ La carpeta {tests_dir} no existe.")
        return

    archivos = [f for f in os.listdir(tests_dir) if f.endswith(".txt")]
    if not archivos:
        print(Fore.YELLOW + "⚠️ No se encontraron archivos .txt en la carpeta de pruebas.")
        return

    for archivo in archivos:
        ruta = os.path.join(tests_dir, archivo)
        with open(ruta, "r", encoding="utf-8") as f:
            codigo = f.read()
            if not codigo.strip():
                print(Fore.YELLOW + f"⚠️ {archivo} está vacío.")
                continue
            print(Fore.MAGENTA + f"\n📝 Analizando: {archivo}")

            print(Fore.WHITE + Style.BRIGHT + "\n📄 Contenido:")
            print(codigo)

            analizar_codigo(codigo, archivo.replace(".txt", ""))

def modo_interactivo():
    """
    Permite al usuario ingresar código manualmente en consola (modo REPL).
    El análisis comienza al detectar una línea vacía o Ctrl+Z/D.
    """
    print(Fore.BLUE + "🧪 Modo interactivo. Escribe o pega tu código BebopLang.")
    print(Fore.BLUE + "👉 Finaliza con una línea vacía o Ctrl+Z (Windows) / Ctrl+D (Linux/macOS):")

    lineas = []
    try:
        for linea in sys.stdin:
            if linea.strip() == "":
                break
            lineas.append(linea.rstrip())
    except EOFError:
        pass

    codigo = "\n".join(lineas)

    if codigo.strip():
        print(Fore.WHITE + Style.BRIGHT + "\n📄 Contenido ingresado:")
        print(Fore.LIGHTWHITE_EX + codigo)
        analizar_codigo(codigo, "interactivo")
    else:
        print(Fore.YELLOW + "⚠️ Entrada vacía. Finalizado.")

if __name__ == "__main__":
    # Menú principal interactivo para elegir el modo de análisis
    while True:
        print(Fore.CYAN + "\n👾 BebopLang - Compilador")
        print("1️⃣  Analizar archivos en tests/")
        print("2️⃣  Escribir código manualmente (modo interactivo)")
        print("3️⃣  Salir")

        opcion = input("Elige una opción (1, 2 o 3): ").strip()

        if opcion == "1":
            modo_archivos()
        elif opcion == "2":
            modo_interactivo()
        elif opcion == "3":
            print(Fore.GREEN + "👋 Hasta luego, Space Cowboy...")
            break
        else:
            print(Fore.RED + "❌ Opción inválida.")

        input(Fore.BLUE + "\n🔁 Presiona Enter para volver al menú...")

        # Limpieza de pantalla según el sistema operativo
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

# Fin del archivo

import os
import sys
from antlr4 import *
from colorama import Fore, Style, init
from BebopLangLexer import BebopLangLexer
from BebopLangParser import BebopLangParser
from tabla_simbolos import TablaSimbolos
from tabla_errores import TablaErrores
from listener import BebopLangListenerImpl

init(autoreset=True)
sys.stdout.reconfigure(encoding='utf-8')  # Soporte para tildes y símbolos

def analizar_codigo(codigo, nombre_archivo="entrada"):
    input_stream = InputStream(codigo)
    lexer = BebopLangLexer(input_stream)
    tokens = CommonTokenStream(lexer)

    simbolos = TablaSimbolos()
    errores = TablaErrores()

    parser = BebopLangParser(tokens)
    tree = parser.programa()

    listener = BebopLangListenerImpl(simbolos, errores)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    print(Fore.GREEN + "\n✅ Tabla de Símbolos:")
    simbolos.mostrar()

    print(Fore.YELLOW + "\n⚠️ Tabla de Errores:")
    errores.mostrar()

    print(Fore.CYAN + "\n🌳 Generando árbol de derivación...")
    os.makedirs("output", exist_ok=True)
    path = f"output/arbol_derivacion_{nombre_archivo}"
    listener.grafo.render(path, format="png", cleanup=True)
    print(Fore.CYAN + f"📁 Guardado como: {path}.png")

def modo_archivos():
    tests_dir = "../tests"
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

            # 📄 Mostrar contenido del archivo
            print(Fore.WHITE + Style.BRIGHT + "\n📄 Contenido:")
            print(codigo)

            analizar_codigo(codigo, archivo.replace(".txt", ""))

def modo_interactivo():
    print(Fore.BLUE + "🧪 Modo interactivo. Escribe tu código BebopLang y presiona Enter dos veces para ejecutar:")
    lineas = []
    while True:
        try:
            linea = input()
            if linea == "":
                break
            lineas.append(linea)
        except EOFError:
            break
    codigo = "\n".join(lineas)
    if codigo.strip():
        print(Fore.WHITE + Style.BRIGHT + "\n📄 Contenido ingresado:")
        print(codigo)
        analizar_codigo(codigo, "interactivo")
    else:
        print(Fore.YELLOW + "⚠️ Entrada vacía. Finalizado.")

if __name__ == "__main__":
    print(Fore.CYAN + "👾 BebopLang - Compilador")
    print("1️⃣  Analizar archivos en tests/")
    print("2️⃣  Escribir código manualmente (modo interactivo)")
    opcion = input("Elige una opción (1 o 2): ").strip()

    if opcion == "1":
        modo_archivos()
    elif opcion == "2":
        modo_interactivo()
    else:
        print(Fore.RED + "❌ Opción inválida.")

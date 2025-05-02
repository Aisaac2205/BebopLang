# Importa la clase base generada por ANTLR para el listener
from BebopLangListener import BebopLangListener as BaseListener
# Importa la clase Digraph para construir el árbol de derivación con Graphviz
from graphviz import Digraph

class BebopLangListenerImpl(BaseListener):
    """
    Implementación personalizada del listener generado por ANTLR para BebopLang.
    Este listener genera un árbol de derivación, maneja la tabla de símbolos y errores semánticos.
    """

    def __init__(self, tabla_simbolos, tabla_errores):
        """
        Constructor que inicializa las estructuras necesarias.

        Args:
            tabla_simbolos (TablaSimbolos): Instancia para registrar identificadores y sus atributos.
            tabla_errores (TablaErrores): Instancia para registrar errores semánticos.
        """
        self.tabla_simbolos = tabla_simbolos
        self.tabla_errores = tabla_errores
        self.grafo = Digraph("Árbol de derivación")  # Árbol de derivación
        self.contador = 0  # Contador de nodos únicos
        self.pila = []  # Pila de nodos para controlar jerarquía

    def agregar_nodo(self, nombre):
        """
        Agrega un nodo al árbol de derivación y lo conecta con su nodo padre si existe.

        Args:
            nombre (str): Nombre del nodo a agregar.

        Returns:
            str: ID único del nodo agregado.
        """
        nodo_id = f"n{self.contador}"
        self.grafo.node(nodo_id, nombre)
        if self.pila:
            self.grafo.edge(self.pila[-1], nodo_id)
        self.pila.append(nodo_id)
        self.contador += 1
        return nodo_id

    def salir_nodo(self):
        """
        Finaliza un nodo en el árbol de derivación, saliendo del contexto actual.
        """
        if self.pila:
            self.pila.pop()

    # -- Nodo raíz
    def enterPrograma(self, ctx): self.agregar_nodo("programa")
    def exitPrograma(self, ctx): self.salir_nodo()

    # -- Instrucciones personalizadas
    def enterIniciar(self, ctx): self.agregar_nodo("iniciar misión")
    def exitIniciar(self, ctx): self.salir_nodo()

    def enterAsignacion(self, ctx):
        """
        Procesa una instrucción de asignación:
        - Detecta tipo de dato (jet, faye, ein, referencia)
        - Valida si el valor es numérico mayor a 100
        - Agrega a tabla de símbolos o errores si aplica
        """
        self.agregar_nodo("asignacion")
        try:
            id_nombre = ctx.ID().getText()
            tipo_texto = ctx.tipo().getText()
            valor_ctx = ctx.valor()

            if valor_ctx.NUMERO():
                valor = int(valor_ctx.NUMERO().getText())
                tipo = "jet"
                if valor > 100:
                    self.tabla_errores.agregar("Semántico", f"Número mayor a 100: {valor}", ctx.start.line)
            elif valor_ctx.CADENA():
                valor = valor_ctx.CADENA().getText()
                tipo = "faye"
            elif valor_ctx.TRUE() or valor_ctx.FALSE():
                valor = valor_ctx.getText()
                tipo = "ein"
            elif valor_ctx.ID():
                valor = valor_ctx.ID().getText()
                tipo = "referencia"
            else:
                raise ValueError("Tipo de valor no reconocido")

            self.tabla_simbolos.agregar(id_nombre, tipo, valor, ctx.start.line)

        except Exception as e:
            self.tabla_errores.agregar("Semántico", f"Error en asignación: {str(e)}", ctx.start.line)
    def exitAsignacion(self, ctx): self.salir_nodo()

    def enterRastreo(self, ctx): self.agregar_nodo("rastreo")
    def exitRastreo(self, ctx): self.salir_nodo()

    def enterCaptura(self, ctx): self.agregar_nodo("captura")
    def exitCaptura(self, ctx): self.salir_nodo()

    def enterImprimir(self, ctx):
        """
        Procesa instrucción de impresión de valores.
        """
        self.agregar_nodo("imprimir")
        print(f"📤 Imprimir: {ctx.valor().getText()}")
    def exitImprimir(self, ctx): self.salir_nodo()

    def enterEntrada(self, ctx):
        """
        Procesa instrucción de entrada de datos del usuario.
        """
        self.agregar_nodo("entrada")
        print(f"📥 Entrada para variable: {ctx.ID().getText()}")
    def exitEntrada(self, ctx): self.salir_nodo()

    def enterDecision(self, ctx): self.agregar_nodo("if")
    def exitDecision(self, ctx): self.salir_nodo()

    def enterCondicion(self, ctx):
        """
        Procesa condiciones dentro de estructuras condicionales.
        Verifica que los valores numéricos no superen 100.
        """
        self.agregar_nodo(f"condición {ctx.COMPARADOR().getText()}")
        try:
            val1 = ctx.valor(0)
            val2 = ctx.valor(1)
            for val in [val1, val2]:
                if val.NUMERO():
                    num = int(val.NUMERO().getText())
                    if num > 100:
                        self.tabla_errores.agregar("Semántico", f"Número mayor a 100: {num}", ctx.start.line)
        except Exception:
            self.tabla_errores.agregar("Semántico", "Error en condición", ctx.start.line)
    def exitCondicion(self, ctx): self.salir_nodo()

    def enterBucle(self, ctx): self.agregar_nodo("bucle")
    def exitBucle(self, ctx): self.salir_nodo()

    def enterAbandono(self, ctx): self.agregar_nodo("abandonar misión")
    def exitAbandono(self, ctx): self.salir_nodo()

    def enterFin(self, ctx): self.agregar_nodo("terminar misión")
    def exitFin(self, ctx): self.salir_nodo()

    def enterOperacionAditivaMultiplicativa(self, ctx):
        """
        Representa operaciones aritméticas en el árbol de derivación.
        """
        self.agregar_nodo(f"op {ctx.op.text}")
    def exitOperacionAditivaMultiplicativa(self, ctx): self.salir_nodo()

    def enterOperacionRelacional(self, ctx):
        """
        Representa operaciones relacionales en el árbol de derivación.
        """
        self.agregar_nodo(f"relación {ctx.op.text}")
    def exitOperacionRelacional(self, ctx): self.salir_nodo()

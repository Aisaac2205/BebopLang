from BebopLangParser import BebopLangParser
from BebopLangListener import BebopLangListener as BaseListener
from graphviz import Digraph

class BebopLangListenerImpl(BaseListener):
    def __init__(self, tabla_simbolos, tabla_errores):
        self.tabla_simbolos = tabla_simbolos
        self.tabla_errores = tabla_errores
        self.grafo = Digraph("Árbol de derivación")
        self.contador = 0
        self.pila = []

    def agregar_nodo(self, nombre):
        nodo_id = f"n{self.contador}"
        self.grafo.node(nodo_id, nombre)
        if self.pila:
            self.grafo.edge(self.pila[-1], nodo_id)
        self.pila.append(nodo_id)
        self.contador += 1
        return nodo_id

    def salir_nodo(self):
        if self.pila:
            self.pila.pop()

    def enterPrograma(self, ctx):
        self.agregar_nodo("programa")

    def exitPrograma(self, ctx):
        self.salir_nodo()

    def enterAsignacion(self, ctx):
        self.agregar_nodo("asignacion")
        id_nombre = ctx.ID().getText()
        valor = ctx.CADENA().getText()
        self.tabla_simbolos.agregar(id_nombre, "cadena", valor, ctx.start.line)

    def exitAsignacion(self, ctx):
        self.salir_nodo()

    def enterCaptura(self, ctx):
        self.agregar_nodo("captura")

    def exitCaptura(self, ctx):
        self.salir_nodo()

    def enterDecision(self, ctx):
        self.agregar_nodo("if")

    def exitDecision(self, ctx):
        self.salir_nodo()

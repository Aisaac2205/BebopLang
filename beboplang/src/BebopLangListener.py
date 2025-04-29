# Generated from grammar/BebopLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BebopLangParser import BebopLangParser
else:
    from BebopLangParser import BebopLangParser

# This class defines a complete listener for a parse tree produced by BebopLangParser.
class BebopLangListener(ParseTreeListener):

    # Enter a parse tree produced by BebopLangParser#programa.
    def enterPrograma(self, ctx:BebopLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by BebopLangParser#programa.
    def exitPrograma(self, ctx:BebopLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by BebopLangParser#instruccion.
    def enterInstruccion(self, ctx:BebopLangParser.InstruccionContext):
        pass

    # Exit a parse tree produced by BebopLangParser#instruccion.
    def exitInstruccion(self, ctx:BebopLangParser.InstruccionContext):
        pass


    # Enter a parse tree produced by BebopLangParser#iniciar.
    def enterIniciar(self, ctx:BebopLangParser.IniciarContext):
        pass

    # Exit a parse tree produced by BebopLangParser#iniciar.
    def exitIniciar(self, ctx:BebopLangParser.IniciarContext):
        pass


    # Enter a parse tree produced by BebopLangParser#asignacion.
    def enterAsignacion(self, ctx:BebopLangParser.AsignacionContext):
        pass

    # Exit a parse tree produced by BebopLangParser#asignacion.
    def exitAsignacion(self, ctx:BebopLangParser.AsignacionContext):
        pass


    # Enter a parse tree produced by BebopLangParser#rastreo.
    def enterRastreo(self, ctx:BebopLangParser.RastreoContext):
        pass

    # Exit a parse tree produced by BebopLangParser#rastreo.
    def exitRastreo(self, ctx:BebopLangParser.RastreoContext):
        pass


    # Enter a parse tree produced by BebopLangParser#captura.
    def enterCaptura(self, ctx:BebopLangParser.CapturaContext):
        pass

    # Exit a parse tree produced by BebopLangParser#captura.
    def exitCaptura(self, ctx:BebopLangParser.CapturaContext):
        pass


    # Enter a parse tree produced by BebopLangParser#abandono.
    def enterAbandono(self, ctx:BebopLangParser.AbandonoContext):
        pass

    # Exit a parse tree produced by BebopLangParser#abandono.
    def exitAbandono(self, ctx:BebopLangParser.AbandonoContext):
        pass


    # Enter a parse tree produced by BebopLangParser#fin.
    def enterFin(self, ctx:BebopLangParser.FinContext):
        pass

    # Exit a parse tree produced by BebopLangParser#fin.
    def exitFin(self, ctx:BebopLangParser.FinContext):
        pass


    # Enter a parse tree produced by BebopLangParser#decision.
    def enterDecision(self, ctx:BebopLangParser.DecisionContext):
        pass

    # Exit a parse tree produced by BebopLangParser#decision.
    def exitDecision(self, ctx:BebopLangParser.DecisionContext):
        pass


    # Enter a parse tree produced by BebopLangParser#condicion.
    def enterCondicion(self, ctx:BebopLangParser.CondicionContext):
        pass

    # Exit a parse tree produced by BebopLangParser#condicion.
    def exitCondicion(self, ctx:BebopLangParser.CondicionContext):
        pass



del BebopLangParser
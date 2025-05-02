from antlr4.error.ErrorListener import ErrorListener

class BebopErrorListener(ErrorListener):
    def __init__(self, tabla_errores):
        super(BebopErrorListener, self).__init__()
        self.tabla_errores = tabla_errores

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        descripcion = f"{msg} (columna {column})"
        self.tabla_errores.agregar("Sintáctico", descripcion, line)

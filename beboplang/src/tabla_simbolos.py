class TablaSimbolos:
    def __init__(self):
        self.simbolos = []

    def agregar(self, nombre, tipo, valor, linea):
        self.simbolos.append({
            "nombre": nombre,
            "tipo": tipo,
            "valor": valor,
            "linea": linea
        })

    def mostrar(self):
        print("🔢 Tabla de Símbolos:")
        for s in self.simbolos:
            print(f"{s['nombre']} -> {s['tipo']} = {s['valor']} (línea {s['linea']})")

class TablaErrores:
    def __init__(self):
        self.errores = []

    def agregar(self, tipo, descripcion, linea):
        self.errores.append({
            "tipo": tipo,
            "descripcion": descripcion,
            "linea": linea
        })

    def mostrar(self):
        print("⚠️ Tabla de Errores:")
        for e in self.errores:
            print(f"[{e['tipo']}] Línea {e['linea']}: {e['descripcion']}")

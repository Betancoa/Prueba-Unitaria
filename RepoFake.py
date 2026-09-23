class RepositorioFake:
    def __init__(self):
        self.compras = []

    def guardar(self, usuario, cantidad):
        self.compras.append({
            'usuario': usuario,
            'cantidad': cantidad
        })

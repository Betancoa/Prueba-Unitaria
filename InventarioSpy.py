class inventarioSpy:
    def __init__(self):
        self.veces_consultado = 0

    def consultar_disponibilidad(self):
        self.veces_consultado += 1
        return 50

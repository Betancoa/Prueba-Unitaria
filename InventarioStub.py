class InventarioStub:
    def consultar_disponibilidad(self):
        return 50


inventario = InventarioStub()
print(inventario.consultar_disponibilidad())

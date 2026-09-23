from unittest.mock import Mock


class TicketService:
    def __init__(self, inventario, repositorio, email_service):
        self.inventario = inventario
        self.repositorio = repositorio
        self.email_service = email_service

    def comprar(self, usuario, cantidad):
        disponibles = self.inventario.consultar_disponibilidad()
        if disponibles < cantidad:
            return False
        self.repositorio.guardar(usuario, cantidad)
        self.email_service.enviar_confirmacion(usuario)
        return True


if __name__ == "__main__":
    from InventarioSpy import inventarioSpy
    from RepoFake import RepositorioFake
    from Dummy import usuarioDummy

    email_mock = Mock()
    inventario_spy = inventarioSpy()

    service = TicketService(
        inventario_spy,         # Spy
        RepositorioFake(),      # Fake
        email_mock              # Mock
    )
    resultado = service.comprar("Ana", 2)
    assert resultado == True
    assert inventario_spy.veces_consultado == 1
    email_mock.enviar_confirmacion.assert_called_once_with("Ana")
    print("✅ Test pasó correctamente")

    service.comprar(usuarioDummy(), 1)
    print(inventario_spy.veces_consultado)

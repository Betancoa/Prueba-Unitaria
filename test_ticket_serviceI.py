from unittest.mock import Mock

from TicketPlus import TicketService
from InventarioSpy import inventarioSpy
from RepoFake import RepositorioFake
from Dummy import usuarioDummy


def test_flujo_completo_compra():

    inventario = inventarioSpy()

    repositorio = RepositorioFake()

    email = Mock()

    service = TicketService(
        inventario,
        repositorio,
        email
    )

    resultado = service.comprar(
        usuarioDummy(),
        2
    )

    assert resultado is True

    assert inventario.veces_consultado == 1

    assert len(repositorio.compras) == 1

    email.enviar_confirmacion.assert_called_once()

from unittest.mock import Mock

from TicketPlus import TicketService
from InventarioStub import InventarioStub
from RepoFake import RepositorioFake
from Dummy import usuarioDummy


def test_compra_exitosa():

    email_mock = Mock()

    service = TicketService(
        InventarioStub(),
        RepositorioFake(),
        email_mock
    )

    resultado = service.comprar(
        usuarioDummy(),
        2
    )

    assert resultado is True

    email_mock.enviar_confirmacion.assert_called_once()

"""Ponto de Entrada Principal da Aplicação Biblioteca CLI (v3.0).

Inicializa a aplicação, executa a apresentação visual de boas-vindas
e transfere o controle para o orquestrador de menus.
"""

try:
    from src.presentation.RenderizadorASCII import RenderizadorASCII
    from src.presentation.menu import MenuPrincipal
    from src.presentation.config import SUBTITULO
except ModuleNotFoundError:
    from RenderizadorASCII import RenderizadorASCII
    from menu import MenuPrincipal
    from config import SUBTITULO


def iniciar_aplicacao() -> None:
    # 1. Animação de boas-vindas (executada apenas na inicialização)
    renderizador = RenderizadorASCII()
    renderizador.exibir("Biblioteca\nvirtual", subtitulo=SUBTITULO, animado=True)

    # 2. Transfere o controle para o Menu Principal
    menu = MenuPrincipal()
    menu.executar()


if __name__ == "__main__":
    iniciar_aplicacao()

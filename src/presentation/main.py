try:
    from src.presentation.titulo import RenderizadorASCII
    from src.presentation.utils import desenhar_linha
except ModuleNotFoundError:
    from titulo import RenderizadorASCII
    from utils import desenhar_linha


VERSAO_BUILD = 3.0
DATA_VERSAO = "Data Da Versão: 2024-16-10"
LINK_REPOSITORIO = "https://github.com/mitureold-one/biblioteca-/tree/main"

outras_versoes = f"""
    Confira versões anteriores em: {LINK_REPOSITORIO}
"""

aviso_importante = """
Feito 100% Pela estupidez humana ! 
"""

subtitulo = f"""
    \tBem-Vindo a Nova Versão da nossa... a sua.... \"Biblioteca {VERSAO_BUILD}\" !
       
"""

linha = desenhar_linha(100)

menu = f"""
    {linha}
    ⬧ Livros
    ⬧ Usuários
    ⬧ Empréstimos
    ⬧ Devoluções
    ⬧ Sair
    {linha}
"""

footer = f"{DATA_VERSAO}\n{outras_versoes}\n{aviso_importante}"


def iniciar_aplicacao() -> None:
    # 1. Instancia o renderizador e executa a exibição animada do título ASCII
    renderizador = RenderizadorASCII()
    renderizador.exibir("Biblioteca\nvirtual", animado=True)

    # 2. Exibe o restante da interface de entrada
    print(subtitulo)
    print(menu)
    print(footer)


if __name__ == "__main__":
    iniciar_aplicacao()

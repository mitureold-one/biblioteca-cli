"""Módulo de Navegação e Menus da Camada de Apresentação (CLI).

Implementa a arquitetura de menus orientada a objetos com classes e herança:
- MenuBase: Classe base abstrata com o Template Method de execução e layout.
- MenuPrincipal: Subclasse para o menu raiz do sistema.
- MenuCRUD: Subclasse genérica e extensível para operações de entidades.
"""

from abc import ABC, abstractmethod

try:
    from src.presentation.RenderizadorASCII import RenderizadorASCII
    from src.presentation.utils import limpar_tela, pausar, desenhar_linha
    from src.presentation.config import SUBTITULO, LARGURA_TERMINAL, CARACTERE_DIVISORIA
except ModuleNotFoundError:
    from RenderizadorASCII import RenderizadorASCII
    from utils import limpar_tela, pausar, desenhar_linha
    from config import SUBTITULO, LARGURA_TERMINAL, CARACTERE_DIVISORIA


class MenuBase(ABC):
    """Classe base abstrata para telas e menus do terminal.

    Aplica o padrão Template Method no método 'executar', encapsulando
    o ciclo de vida da tela (desenhar, exibir opções, ler entrada e processar).
    """

    def __init__(self, titulo_secao: str | None = None) -> None:
        self.titulo_secao = titulo_secao
        self.renderizador = RenderizadorASCII()
        self.linha_divisoria = desenhar_linha(LARGURA_TERMINAL, CARACTERE_DIVISORIA)

    def _desenhar(self) -> None:
        """Limpa a tela e redesenha o título ASCII e o subtítulo de forma estática."""
        limpar_tela()
        sub = self.titulo_secao if self.titulo_secao is not None else SUBTITULO
        self.renderizador.exibir("Biblioteca\nvirtual", subtitulo=sub, animado=False)

    @abstractmethod
    def exibir_opcoes(self) -> None:
        """Exibe o bloco visual de opções do menu específico."""
        pass

    @abstractmethod
    def processar_opcao(self, opcao: str) -> bool:
        """Executa a ação correspondente à opção escolhida.

        Retorna True para continuar no loop do menu, ou False para sair/voltar.
        """
        pass

    def _placeholder(self, acao: str) -> None:
        """Exibe mensagem amigável de funcionalidade em desenvolvimento."""
        print(f"\n [EM BREVE] A funcionalidade '{acao}' será conectada ao Domínio/Casos de Uso.")
        pausar()

    def executar(self) -> None:
        """Template Method: Orquestra o ciclo de vida do menu até que seja solicitado sair."""
        while True:
            self._desenhar()
            self.exibir_opcoes()

            opcao = input("\n Escolha uma opção: ").strip()

            continuar = self.processar_opcao(opcao)
            if not continuar:
                break

    # Alias de conveniência
    iniciar = executar


class MenuPrincipal(MenuBase):
    """Subclasse responsável pelo menu principal de navegação do sistema."""

    def __init__(self) -> None:
        super().__init__()

    def exibir_opcoes(self) -> None:
        print(f"""{self.linha_divisoria}
    ⬧ 1. Livros
    ⬧ 2. Usuários
    ⬧ 3. Empréstimos
    ⬧ 4. Devoluções
    ⬧ 0. Sair
{self.linha_divisoria}""")

    def processar_opcao(self, opcao: str) -> bool:
        match opcao:
            case "1":
                MenuCRUD("Livro").executar()
            case "2":
                MenuCRUD("Usuário").executar()
            case "3":
                MenuCRUD("Empréstimo").executar()
            case "4":
                MenuCRUD("Devolução").executar()
            case "0":
                limpar_tela()
                print("\nAté logo! Obrigado por usar a Biblioteca Virtual. \n")
                return False
            case _:
                print("\n Opção inválida! Escolha um dos números do menu.")
                pausar()
        return True


class MenuCRUD(MenuBase):
    """Subclasse genérica responsável por operações de CRUD de qualquer entidade."""

    def __init__(self, entidade: str) -> None:
        super().__init__(titulo_secao=f"\t[ MÓDULO: GERENCIAMENTO DE {entidade.upper()}S ]")
        self.entidade = entidade

    def exibir_opcoes(self) -> None:
        print(f"""{self.linha_divisoria}
    ⬧ 1. Cadastrar {self.entidade}       (Create)
    ⬧ 2. Listar {self.entidade}s         (Read)
    ⬧ 3. Atualizar {self.entidade}       (Update)
    ⬧ 4. Remover {self.entidade}         (Delete)
    ⬧ 0. Voltar ao Menu Principal
{self.linha_divisoria}""")

    def processar_opcao(self, opcao: str) -> bool:
        match opcao:
            case "1":
                self._placeholder(f"Cadastrar {self.entidade}")
            case "2":
                self._placeholder(f"Listar {self.entidade}s")
            case "3":
                self._placeholder(f"Atualizar {self.entidade}")
            case "4":
                self._placeholder(f"Remover {self.entidade}")
            case "0":
                return False  # Encerra o loop e volta para o MenuPrincipal
            case _:
                print("\n Opção inválida!")
                pausar()
        return True


# Alias de compatibilidade
MenuApp = MenuPrincipal


if __name__ == "__main__":
    menu = MenuPrincipal()
    menu.executar()

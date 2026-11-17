"""Módulo de Utilitários de Terminal e Console.

Contém funções auxiliares e reutilizáveis para manipulação de terminal,
controle de fluxo de tela e formatação visual na camada de apresentação.
"""


def limpar_tela() -> None:
    """Limpa a tela do terminal e move o cursor para o topo (0, 0) via ANSI."""
    print("\033[H\033[J", end="", flush=True)


def pausar(mensagem: str = "Pressione [ENTER] para continuar...") -> None:
    """Pausa a execução do terminal aguardando confirmação do usuário."""
    input(f"\n{mensagem}")


def desenhar_linha(tamanho: int = 100, caractere: str = "-") -> str:
    """Gera uma string com uma linha divisória repetindo o caractere especificado."""
    return caractere * tamanho

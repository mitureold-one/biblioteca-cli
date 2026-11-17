"""Módulo de Fontes e Glifos em Arte ASCII.

Contém os desenhos matriciais de caracteres individuais (6 linhas de altura)
e o mapeamento do dicionário LETRAS para uso pelo renderizador visual.
"""

LETRA_A = """
░█████╗░
██╔══██╗
███████║
██╔══██║
██║░░██║
╚═╝░░╚═╝
"""

LETRA_B = """
██████╗░
██╔══██╗
██████╦╝
██╔══██╗
██████╦╝
╚═════╝░
"""

LETRA_C = """
░█████╗░
██╔══██╗
██║░░╚═╝
██║░░██╗
╚█████╔╝
░╚════╝░
"""

LETRA_E = """
███████╗
██╔════╝
█████╗░░
██╔══╝░░
███████╗
╚══════╝
"""

LETRA_I = """
██╗
██║
██║
██║
██║
╚═╝
"""

LETRA_L = """
██╗░░░░░
██║░░░░░
██║░░░░░
██║░░░░░
███████╗
╚══════╝
"""

LETRA_O = """
░█████╗░
██╔══██╗
██║░░██║
██║░░██║
╚█████╔╝
░╚════╝░
"""

LETRA_R = """
██████╗░
██╔══██╗
██████╔╝
██╔══██╗
██║░░██║
╚═╝░░╚═╝
"""

LETRA_T = """
████████╗
╚══██╔══╝
░░░██║░░░
░░░██║░░░
░░░██║░░░
░░░╚═╝░░░
"""

LETRA_U = """
██╗░░░██╗
██║░░░██║
██║░░░██║
██║░░░██║
╚██████╔╝
░╚═════╝░
"""

LETRA_V = """
██╗░░░██╗
██║░░░██║
╚██╗░██╔╝
░╚████╔╝░
░░╚██╔╝░░
░░░╚═╝░░░
"""

LETRA_ESPECIAL_EXCLAMACAO = """
██╗
██║
██║
╚═╝
██╗
╚═╝
"""

LETRA_ESPECIAL_INTERROGACAO = """
░█████╗░
██╔══██╗
╚═╝███╔╝
░░░╚══╝░
░░░██╗░░
░░░╚═╝░░
"""


def definir_linhas(letra: str) -> list[str]:
    """Converte uma string multiline de uma letra em uma lista de linhas.

    Aplica strip() para remover quebras nas bordas e splitlines() para
    separar a matriz nas 6 fatias horizontais que compõem o glifo.
    """
    return letra.strip().splitlines()


# Mapeamento oficial de caracteres suportados.
# Cada entrada é uma lista com exatamente 6 elementos (linhas).
LETRAS: dict[str, list[str]] = {
    "A": definir_linhas(LETRA_A),
    "B": definir_linhas(LETRA_B),
    "C": definir_linhas(LETRA_C),
    "E": definir_linhas(LETRA_E),
    "I": definir_linhas(LETRA_I),
    "L": definir_linhas(LETRA_L),
    "O": definir_linhas(LETRA_O),
    "R": definir_linhas(LETRA_R),
    "T": definir_linhas(LETRA_T),
    "U": definir_linhas(LETRA_U),
    "V": definir_linhas(LETRA_V),
    "!": definir_linhas(LETRA_ESPECIAL_EXCLAMACAO),
    "?": definir_linhas(LETRA_ESPECIAL_INTERROGACAO),
    " ": ["    "] * 6,  # Espaço em branco: 4 espaços de largura x 6 linhas de altura
}

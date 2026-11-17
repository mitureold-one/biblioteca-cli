"""Módulo de Renderização e Exibição de Título em Arte ASCII.

Este módulo decompõe o título em matrizes de caracteres individuais e as
recompõe horizontalmente para renderização no terminal CLI.
Os desenhos base foram adaptados de fontes ASCII com matrizes de 6 linhas.
"""

# ==============================================================================
# 1ª ETAPA: Glifos ASCII (Matrizes Individuais)
# Cada caractere é definido em uma string multiline com exatamente 6 linhas
# de altura e largura uniforme por caractere para evitar desalinhamento.
# ==============================================================================

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


# ==============================================================================
# 2ª ETAPA: Pré-processamento e Dicionário de Caracteres
# ==============================================================================

def definir_linhas(letra: str) -> list[str]:
    """Converte uma string multiline de uma letra em uma lista de linhas.

    Aplica strip() para remover quebras nas bordas e splitlines() para
    separar a matriz nas 6 fatias horizontais que compõem o glifo.
    """
    return letra.strip().splitlines()


# Mapeamento oficial de caracteres suportados.
# Cada entrada DEVE ser uma lista com exatamente 6 elementos (linhas).
LETRAS = {
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
    " ": ["    "] * 6,  # Espaço em branco: 4 espaços de largura x 6 linhas de altura
}


# ==============================================================================
# 3ª ETAPA: Formatação e Apresentação (Separação de Responsabilidades)
# ==============================================================================

def formatar_titulo(palavra: str) -> str:
    """Função pura responsável por compor uma única linha de texto em arte ASCII.

    - Converte a palavra para maiúsculas.
    - Localiza as matrizes de cada caractere no dicionário.
    - Utiliza zip(*...) para combinar horizontalmente cada uma das 6 linhas.
    - Retorna a string pronta com as linhas separadas por quebra de linha ('\\n').
    """
    palavra = palavra.upper()
    palavra_formatada = [LETRAS[letra] for letra in palavra]

    resultado = []
    for linha in zip(*palavra_formatada):
        resultado.append(" ".join(linha))

    return "\n".join(resultado)


def exibir_titulo(texto: str) -> None:
    """Função de apresentação (I/O) que imprime o título formatado no terminal.

    Permite textos com quebras de linha ('\\n'), processando e imprimindo
    cada linha de blocos sequencialmente.
    """
    for linha in texto.splitlines():
        texto_formatado = formatar_titulo(linha)
        print(texto_formatado)


# ==============================================================================
# Testes locais de execução
# ==============================================================================

if __name__ == "__main__":
    exibir_titulo("Biblioteca\nvirtual !")

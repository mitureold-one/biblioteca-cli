"""Módulo de Configurações da Camada de Apresentação (CLI).

Centraliza metadados do projeto, constantes visuais e textos fixos da interface,
evitando dados hardcoded nos arquivos de execução.
"""

# Metadados da Aplicação
NOME_APLICACAO = "Biblioteca Virtual"
VERSAO_BUILD = "3.0"
DATA_VERSAO = "16/10/2024"
LINK_REPOSITORIO = "https://github.com/mitureold-one/biblioteca-/tree/main"
AVISO_IMPORTANTE = "Feito 100% Pela estupidez humana !"

# Textos Padrão (Subtítulo consolidado com os metadados do projeto)
SUBTITULO = (
    f"\tBem-Vindo a Nova Versão da nossa... a sua.... \"{NOME_APLICACAO} {VERSAO_BUILD}\" !\n"
    f"\tv{VERSAO_BUILD} ({DATA_VERSAO})  │  Repositório Do Projeto antigo: {LINK_REPOSITORIO}\n"
    f"\t{AVISO_IMPORTANTE}"
)

# Parâmetros de Layout e Estilo
LARGURA_TERMINAL = 100
CARACTERE_DIVISORIA = "─"

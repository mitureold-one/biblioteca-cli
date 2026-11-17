"""Módulo de Renderização e Animação de Título em Arte ASCII.

Contém a classe RenderizadorASCII, responsável por compor os caracteres ASCII
horizontalmente e executar efeitos visuais de apresentação no terminal.
"""

import sys
import time

try:
    from src.presentation.fontes_ascii import LETRAS
    from src.presentation.utils import limpar_tela
except ModuleNotFoundError:
    from fontes_ascii import LETRAS
    from utils import limpar_tela


class RenderizadorASCII:
    """Responsável por renderizar e animar títulos em arte ASCII no terminal."""

    def __init__(
        self,
        fonte: dict[str, list[str]] | None = None,
        velocidade_digitacao: float = 0.06,
        repeticoes_embaralhamento: int = 5,
        velocidade_embaralhamento: float = 0.20,
        velocidade_subtitulo: float = 0.03,
    ) -> None:
        # Injeção de dependência da fonte (usa LETRAS por padrão)
        self.fonte: dict[str, list[str]] = fonte if fonte is not None else LETRAS
        self.velocidade_digitacao: float = velocidade_digitacao
        self.repeticoes_embaralhamento: int = repeticoes_embaralhamento
        self.velocidade_embaralhamento: float = velocidade_embaralhamento
        self.velocidade_subtitulo: float = velocidade_subtitulo

    def formatar(self, palavra: str) -> str:
        """Função pura que monta uma única linha de texto em arte ASCII.

        - Converte a palavra para maiúsculas.
        - Busca as matrizes no catálogo da fonte injetada (self.fonte).
        - Combina as linhas horizontalmente com zip(*...).
        - Retorna o desenho montado em uma string multiline.
        """
        palavra = palavra.upper()
        palavra_formatada = [self.fonte[letra] for letra in palavra]

        resultado = []
        for linha in zip(*palavra_formatada):
            resultado.append(" ".join(linha))

        return "\n".join(resultado)

    def animar_digitacao(self, texto: str) -> None:
        """Executa a animação de máquina de escrever letra por letra."""
        linhas_concluidas: list[str] = []

        for linha in texto.splitlines():
            for i in range(1, len(linha) + 1):
                fatia = linha[:i]

                limpar_tela()

                # Redesenha as linhas anteriores já concluídas
                for linha_pronta in linhas_concluidas:
                    print(linha_pronta)

                # Imprime a fatia atual sendo digitada
                print(self.formatar(fatia), flush=True)

                time.sleep(self.velocidade_digitacao)

            linhas_concluidas.append(self.formatar(linha))

    def animar_embaralhamento(self, texto: str) -> None:
        """Alterna os símbolos '?' e '!' no final do texto por N ciclos."""
        texto_base = texto.rstrip("!? ")
        simbolos = ["?", "!"]

        for i in range(self.repeticoes_embaralhamento * 2):
            simbolo = simbolos[i % 2]
            conteudo = f"{texto_base} {simbolo}"

            limpar_tela()
            for linha in conteudo.splitlines():
                print(self.formatar(linha))

            time.sleep(self.velocidade_embaralhamento)

    def animar_subtitulo(self, texto: str) -> None:
        """Datilografa o subtítulo caractere por caractere no terminal."""
        for caractere in texto:
            sys.stdout.write(caractere)
            sys.stdout.flush()
            time.sleep(self.velocidade_subtitulo)
        print()

    def exibir(self, texto: str, subtitulo: str | None = None, animado: bool = True) -> None:
        """Orquestrador de apresentação: exibe o título e o subtítulo opcional."""
        if animado:
            self.animar_digitacao(texto)
            self.animar_embaralhamento(texto)
        else:
            texto_final = f"{texto.rstrip('!? ')} !"
            for linha in texto_final.splitlines():
                print(self.formatar(linha))

        # Se houver subtítulo, exibe logo abaixo
        if subtitulo is not None:
            if animado:
                self.animar_subtitulo(subtitulo)
            else:
                print(subtitulo)


# ==============================================================================
# Função de Compatibilidade / Atalho
# ==============================================================================

def exibir_titulo(texto: str, subtitulo: str | None = None, animado: bool = True) -> None:
    """Atalho de conveniência que instancia e executa o RenderizadorASCII padrão."""
    renderizador = RenderizadorASCII()
    renderizador.exibir(texto, subtitulo=subtitulo, animado=animado)


# ==============================================================================
# Testes locais de execução
# ==============================================================================

if __name__ == "__main__":
    subtitulo_teste = '\tBem-Vindo a Nova Versão da nossa... a sua.... "Biblioteca 3.0" !'
    renderizador = RenderizadorASCII()
    renderizador.exibir("Biblioteca\nvirtual", subtitulo=subtitulo_teste, animado=True)

# Documentação: Evolução da Renderização do Título (CLI)

Este documento registra o processo de engenharia, arquitetura e refatoração da interface visual do título da aplicação **Biblioteca CLI (v3.0)**, localizada na camada de apresentação (`presentation`).

---

## 📌 Contexto e Visão Geral

O título em arte ASCII é o elemento visual central da CLI. O objetivo deste módulo foi evoluir de uma representação estática inicial para uma arquitetura modular, testável e capaz de suportar animações dinâmicas no terminal.

---

## 🛠️ Etapa 1: A Abordagem Estática (Rascunho)

**Arquivo:** `src/presentation/main.py`

### Implementação Inicial:
- O banner completo foi colado diretamente no código como uma única *string multiline* bruta.

### Lições Aprendidas:
- **Prós:** Facilidade imediata para testar se a arte cabe na largura padrão do terminal (80-120 colunas).
- **Contras:** Texto rígido e acoplado. Impossível alterar palavras dinamicamente ou aplicar efeitos como digitação ou animação.

---

## 🧩 Etapa 2: Decomposição em Glifos e Composição com `zip`

**Arquivo:** `src/presentation/titulo.py`

### Implementação:
1. **Catálogo de Glifos:** Isolamento de cada caractere em strings individuais de 6 linhas de altura (`LETRA_A`, `LETRA_B`, etc.).
2. **Fatiamento das Matrizes:** Criação da função `definir_linhas(letra: str) -> list[str]` aplicando `.strip().splitlines()`.
3. **Mapeamento em Dicionário:** O dicionário `LETRAS` associa o caractere char à sua lista de 6 linhas.
4. **Composição Horizontal:** Utilização de `zip(*palavra_formatada)` para parear a mesma linha horizontal de todas as letras da palavra, unindo-as com `" ".join(...)`.

---

## ⚙️ Etapa 3: Refatoração, Consistência da Matriz e Separação de Papéis

Durante os testes de integração e composição, foram identificados e solucionados três desafios de design e geometria de caracteres:

### 1. Separação de Responsabilidades (Função Pura vs. Efeito Colateral)
Para permitir testes unitários e reutilização, a lógica de impressão foi dividida:
- **`formatar_titulo(palavra: str) -> str` (Função Pura):**
  - Recebe a palavra e apenas processa os dados, retornando uma string única com as 6 linhas unidas por `\n`.
  - Não executa `print()`, tornando-a ideal para asserções em testes automatizados.
- **`exibir_titulo(texto: str) -> None` (Função de Apresentação):**
  - Responsável pelo I/O (saída de tela).
  - Trata quebras de linha com `texto.splitlines()`, permitindo chamadas com múltiplos blocos (ex: `"Biblioteca\nvirtual !"`).

### 2. O Caso do Espaço em Branco (`" "`)
- Para participar da operação do `zip`, **todos** os elementos do dicionário precisam ter exatamente 6 linhas de altura.
- O espaço foi implementado como uma lista de 6 linhas com 4 espaços de largura: `["    "] * 6`.

### 3. Integridade Geométrica dos Caracteres (Bug do Desalinhamento)
- **Sintoma:** A palavra `"VIRTUAL"` aparecia distorcida/torta no terminal.
- **Diagnóstico:** Análise de comprimento linha a linha revelou que `LETRA_V` e `LETRA_U` possuíam linhas internas com 8 caracteres em vez de 9 (faltando um ponto `░`).
- **Impacto no `zip`:** Quando um glifo perde caracteres em uma linha específica, todas as letras à direita são puxadas para a esquerda naquela linha.
- **Correção:** Equalização de todas as 6 linhas de cada letra para uma largura uniforme e estrita.

---

## 🎬 Etapa 4: Próximo Passo — Animação no Terminal

Com os glifos estáveis e a função `formatar_titulo` desacoplada da impressão, a arquitetura está pronta para a camada de animação:
- **Efeito Máquina de Escrever:** Fatiamento progressivo (`palavra[:i]`), renderização via `formatar_titulo` e atualização de tela com intervalo de tempo (`time.sleep`) e limpeza de tela.

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

Durante os testes de integração e composição, foram identificados e solucionados desafios de design e geometria de caracteres:

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

## 🎬 Etapa 4: Animações no Terminal

Implementação de duas animações na camada de apresentação:

### 1. Limpeza de Tela com Códigos ANSI (`limpar_tela`)
- Em vez de chamadas lentas de sistema operacional (`os.system('cls')`) que causam *flickering* (tela piscando), usamos códigos de controle ANSI nativos: `\033[H\033[J`. O cursor volta ao topo e limpa a tela instantaneamente e sem piscar.

### 2. Efeito Máquina de Escrever (`anima_digitacao`)
- Fatiamento progressivo (`linha[:i]`).
- Mantém o histórico das linhas anteriores completas enquanto digita a linha atual logo abaixo.
- Parâmetro configurável de `velocidade`.

### 3. Efeito Alternância / Embaralhamento (`anima_embaralhamento`)
- Implementação do glifo `?` (`LETRA_ESPECIAL_INTERROGACAO`).
- Alterna entre `?` e `!` no final da frase por um número definido de repetições (`repeticoes=5`), estabilizando em `!` no final.


---

## 🏛️ Etapa 5: Refatoração Arquitetural — Separação de Dados e Lógica

Para manter os princípios de **Clean Code** e **Single Responsibility**:
- **`fontes_ascii.py` (Dados):** Isola os 14 glifos em matrizes puras e o dicionário `LETRAS`. Adicionar novas letras no futuro altera apenas este arquivo, sem risco de quebrar a lógica de renderização.
- **`titulo.py` (Lógica e Apresentação):** Reduzido para menos de 100 linhas, contendo exclusivamente a orquestração, a formatação pura (`zip(*...)`), as animações e os utilitários de tela.
- **`main.py` (Aplicação):** Ponto de entrada limpo e desacoplado que apenas orquestra o fluxo inicial.


---

## 🧩 Etapa 6: Orientação a Objetos (`RenderizadorASCII`)

Refatoração das funções procedurais para a classe `RenderizadorASCII`:

### Estrutura da Classe:
- **`__init__(fonte, velocidade_digitacao, repeticoes_embaralhamento, velocidade_embaralhamento)`:**
  - Encapsula as configurações visuais e o catálogo de glifos (`self.fonte`).
  - Suporta **Injeção de Dependência**: é possível injetar diferentes fontes ou velocidades no momento da instanciação.
- **`formatar(palavra)`:** Método que gera a string matricial horizontal usando `self.fonte`.
- **`animar_digitacao(texto)`:** Executa a animação de máquina de escrever.
- **`animar_embaralhamento(texto)`:** Executa a alternância de símbolos.
- **`exibir(texto, animado=True)`:** Ponto único de entrada e orquestração.

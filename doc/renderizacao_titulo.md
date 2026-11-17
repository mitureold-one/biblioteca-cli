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


---

## 🎬 Etapa 7: Animação do Subtítulo (Datilografia em Linha)

Diferente do banner ASCII multiline, o subtítulo é um texto corrido. Implementamos o método `animar_subtitulo(texto, velocidade=0.03)` dentro de `RenderizadorASCII`:
- **Sem Limpeza de Tela:** Utiliza `sys.stdout.write` e `sys.stdout.flush()`, inserindo caractere a caractere logo abaixo do título ASCII já estabilizado.
- **Orquestração Completa:** O método `exibir(texto, subtitulo, animado=True)` une o título ASCII com a datilografia suave do subtítulo em uma única chamada.

---

## ⚙️ Etapa 8: Centralização de Configurações (`config.py`)

Aplicação do princípio de **Separação de Configuração e Execução**:
- Criação de `src/presentation/config.py` para isolar metadados (`NOME_APLICACAO`, `VERSAO_BUILD`, `DATA_VERSAO`, `LINK_REPOSITORIO`, `AVISO_IMPORTANTE`), textos consolidados e constantes de layout (`LARGURA_TERMINAL = 100`, `CARACTERE_DIVISORIA = "─"`).
- O arquivo `main.py` foi esvaziado de dados hardcoded e números mágicos, transformando-se em um orquestrador limpo de inicialização.

---

## 🧭 Etapa 9: Arquitetura de Menus com POO e Polimorfismo (`menu.py`)

Evolução da navegação interativa no terminal aplicando padrões de engenharia:
- **Padrão Template Method:** Criação da classe base abstrata `MenuBase(ABC)` que implementa o loop de execução `executar()`, desenha o cabeçalho fixo estático (`_desenhar()`) e delega a exibição e o processamento de opções para as subclasses (`exibir_opcoes()` e `processar_opcao()`).
- **Eliminação de Código Duplicado (Princípio DRY):** Em vez de 4 funções separadas e repetitivas, implementamos a subclasse genérica `MenuCRUD(entidade)`, capaz de gerar menus de CRUD para qualquer entidade dinamicamente.
- **Structural Pattern Matching (`match / case`):** Substituição de estruturas de `if/elif/else` pelo `match/case` idiomático do Python para roteamento de opções.
- **Persistência de Layout Estático:** A cada transição de submenu, a tela limpa e redesenha o título ASCII e o subtítulo instantaneamente (`animado=False`), garantindo que apenas a seção central da interface mude dinamicamente enquanto o topo permanece fixo.

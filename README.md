# Biblioteca CLI (v3.0) 📚

Sistema de gerenciamento de biblioteca via interface de linha de comando (CLI), desenvolvido em Python com arquitetura em camadas (`domain`, `application`, `infrastructure`, `presentation`).

Este projeto é uma releitura e evolução de um projeto acadêmico anterior ([biblioteca-](https://github.com/mitureold-one/biblioteca-)), criado para exercitar boas práticas de arquitetura, design de software (*The Pragmatic Programmer*) e avaliar o progresso contínuo como desenvolvedor.

---

## 🏗️ Estrutura do Projeto

```text
Biblioteca/
├── doc/                         # Documentações técnicas e registros de evolução
│   └── renderizacao_titulo.md   # Registro de evolução visual e arquitetural da CLI
├── src/
│   ├── application/             # Casos de uso e regras de aplicação
│   ├── domain/                  # Entidades de negócio e interfaces de repositório
│   ├── Infrastructure/          # Implementação de persistência e recursos externos
│   └── presentation/            # Interface CLI, telas e renderizadores visuais (ASCII)
│       ├── config.py            # Configurações, metadados e parâmetros da CLI
│       ├── fontes_ascii.py      # Catálogo de glifos e matrizes ASCII
│       ├── main.py              # Ponto de entrada da aplicação
│       ├── menu.py              # Orquestrador de menus e navegação interativa (POO)
│       ├── RenderizadorASCII.py # Classe renderizadora e animadora em ASCII
│       └── utils.py             # Utilitários de terminal e console
├── .gitignore
└── README.md
```

---

## 🎨 Destaques de Implementação

- **Renderizador ASCII Modular:** Conversão dinâmica de palavras em matrizes de caracteres de 6 linhas usando decomposição de glifos e pareamento horizontal com `zip(*...)`.
- **Efeitos de Animação no Terminal:** Máquina de escrever progressiva, alternância de símbolos (`?` / `!`) e datilografia de subtítulo suave via códigos de escape ANSI nativos (sem piscar a tela).
- **Separação de Responsabilidades (SRP & DRY):**
  - Dados isolados em `fontes_ascii.py` e `config.py`.
  - Utilitários reutilizáveis de terminal em `utils.py`.
  - Algoritmo de renderização encapsulado na classe `RenderizadorASCII`.
- **Arquitetura de Menus com POO e Polimorfismo:**
  - Aplicação do padrão **Template Method** com classe base abstrata `MenuBase(ABC)`.
  - Subclasse genérica `MenuCRUD` para operações completas de entidades sem duplicação de código.
  - Controle de fluxo com Structural Pattern Matching moderno (`match / case`).
- **Documentação de Engenharia:** Processo documentado detalhadamente na pasta [`doc/`](doc/renderizacao_titulo.md).

---

## 🚀 Como Executar

### Executar a Aplicação Principal
```bash
python src/presentation/main.py
```

### Testar a Renderização Isolada do Título (ASCII)
```bash
python src/presentation/RenderizadorASCII.py
```

### Testar a Navegação de Menus Isolada
```bash
python src/presentation/menu.py
```

# Biblioteca CLI (v3.0) 📚

Sistema de gerenciamento de biblioteca via interface de linha de comando (CLI), desenvolvido em Python com arquitetura em camadas (`domain`, `application`, `infrastructure`, `presentation`).

Este projeto é uma releitura e evolução de um projeto acadêmico anterior ([biblioteca-](https://github.com/mitureold-one/biblioteca-)), criado para exercitar boas práticas de arquitetura, design de software (*The Pragmatic Programmer*) e avaliar o progresso contínuo como desenvolvedor.

---

## 🏗️ Estrutura do Projeto

```text
Biblioteca/
├── doc/                 # Documentações técnicas e registros de evolução
│   └── renderizacao_titulo.md
├── src/
│   ├── application/     # Casos de uso e regras de aplicação
│   ├── domain/          # Entidades de negócio e interfaces de repositório
│   ├── Infrastructure/  # Implementação de persistência e recursos externos
│   └── presentation/    # Interface CLI, telas e renderizadores visuais (ASCII)
│       ├── fontes_ascii.py # Catálogo de glifos e matrizes ASCII
│       ├── main.py      # Ponto de entrada da aplicação
│       ├── titulo.py    # Renderizador modular de títulos em arte ASCII
│       └── utils.py     # Utilitários de terminal e console
├── .gitignore
└── README.md
```

---

## 🎨 Destaques de Implementação

- **Renderizador ASCII Modular:** Conversão dinâmica de palavras em matrizes de caracteres de 6 linhas usando decomposição de glifos e pareamento horizontal com `zip(*...)`.
- **Separação de Responsabilidades:** Funções puras de formatação desacopladas das funções de apresentação I/O no terminal.
- **Documentação de Engenharia:** Processo documentado detalhadamente na pasta [`doc/`](doc/renderizacao_titulo.md).

---

## 🚀 Como Executar

### Executar a Aplicação Principal
```bash
python src/presentation/main.py
```

### Testar a Renderização do Título (ASCII)
```bash
python src/presentation/titulo.py
```

# Biblioteca CLI (v3.0) 📚

Sistema de gerenciamento de biblioteca via interface de linha de comando (CLI), desenvolvido em Python com arquitetura em camadas (`domain`, `application`, `infrastructure`, `presentation`).

Este projeto é uma releitura e evolução de um projeto acadêmico anterior ([biblioteca-](https://github.com/mitureold-one/biblioteca-)), criado para exercitar boas práticas de arquitetura, design de software e avaliar o progresso como desenvolvedor.

---

## 🏗️ Estrutura do Projeto

```text
Biblioteca/
├── src/
│   ├── application/     # Casos de uso e regras de aplicação
│   ├── domain/          # Entidades de negócio e interfaces de repositório
│   ├── Infrastructure/  # Implementação de persistência e recursos externos
│   └── presentation/    # Interface CLI e telas
├── .gitignore
└── README.md
```

## 🚀 Como Executar

```bash
python src/presentation/main.py
```

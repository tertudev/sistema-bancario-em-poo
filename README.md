# 🏦 Sistema Bancário em POO
Um sistema bancário simplificado implementado em Python, demonstrando os princípios da Programação Orientada a Objetos (POO).

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Repo Size](https://img.shields.io/github/repo-size/tertudev/sistema-bancario-em-poo?style=flat-square)](https://github.com/tertudev/sistema-bancario-em-poo)
[![Last Commit](https://img.shields.io/github/last-commit/tertudev/sistema-bancario-em-poo?style=flat-square)](https://github.com/tertudev/sistema-bancario-em-poo/commits/main)

## 🧐 Sobre o Projeto

Este repositório apresenta um sistema bancário básico desenvolvido em Python, com foco na aplicação e demonstração dos conceitos fundamentais da Programação Orientada a Objetos (POO). O projeto visa simular operações bancárias comuns, como criação de contas e clientes, depósitos, saques e visualização de extratos, utilizando classes, objetos, encapsulamento e herança para estruturar o código de forma modular e extensível.

A arquitetura do sistema é centrada em entidades bem definidas: `Cliente`, `Conta` (com subclasses como `ContaCorrente` e `ContaPoupanca` para demonstrar polimorfismo e herança), e `Transacao`. Cada entidade possui suas responsabilidades bem encapsuladas, facilitando a manutenção e a adição de novas funcionalidades. O sistema é operado através de uma interface de linha de comando simples, que interage com as classes do modelo para executar as operações.

## ✨ Funcionalidades

As principais funcionalidades implementadas neste sistema incluem:

*   **Criação de Clientes:** Registro de novos clientes com informações básicas.
*   **Criação de Contas:** Abertura de diferentes tipos de contas bancárias (e.g., Corrente, Poupança) associadas a clientes.
*   **Depósito:** Realização de depósitos em contas específicas.
*   **Saque:** Efetivação de saques, com validação de saldo e limites.
*   **Extrato:** Consulta do histórico de transações de uma conta.
*   **Listagem de Contas:** Visualização de todas as contas cadastradas no sistema.
*   **Listagem de Clientes:** Visualização de todos os clientes registrados.

## 🛠️ Tecnologias

O projeto foi desenvolvido utilizando as seguintes tecnologias:

*   **Python:** Linguagem de programação principal.

## 🚀 Como Começar

Para configurar e executar o projeto em sua máquina local, siga os passos abaixo.

### Pré-requisitos

Certifique-se de ter o Python 3.9 ou superior instalado em seu sistema.

```bash
python --version
```

### Instalação

1.  Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/tertudev/sistema-bancario-em-poo.git
    ```

2.  Navegue até o diretório do projeto:

    ```bash
    cd sistema-bancario-em-poo
    ```

### Execução

Para iniciar o sistema bancário, execute o arquivo principal `labproject.py`:

```bash
python labproject.py
```

O sistema será iniciado no terminal, apresentando um menu de opções para interação.

## 📂 Estrutura

O projeto é composto por um único arquivo Python que encapsula toda a lógica do sistema:

```
.
├── .gitignore
├── LICENSE
├── README.md
└── labproject.py  # Contém todas as classes e a lógica de execução do sistema bancário.
```

## 🤝 Contribuição

Contribuições são bem-vindas! Se você deseja aprimorar este projeto, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.

Para contribuir:

1.  Faça um *fork* do projeto.
2.  Crie uma nova *branch* (`git checkout -b feature/sua-feature`).
3.  Faça suas alterações e *commit* (`git commit -m 'Adiciona nova feature'`).
4.  Envie para a *branch* original (`git push origin feature/sua-feature`).
5.  Abra um *Pull Request*.

## 📜 Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

Vamos codar o futuro! 🚀

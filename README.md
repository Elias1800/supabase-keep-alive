# Supabase Keep-Alive

![Versão](https://img.shields.io/badge/versão-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Status](https://img.shields.io/badge/status-Ativo-success)
[![Licença MIT](https://img.shields.io/badge/licença-MIT-yellow)](LICENSE)

> Script simples e leve projetado para realizar requisições periódicas ao **Supabase**, evitando que o projeto seja pausado por inatividade no plano gratuito.

---

# Tabela de Conteúdos

- [Principais Funcionalidades](#-principais-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Como Usar](#-como-usar)
- [Licença](#-licença)

---

# Principais Funcionalidades

- • **Consulta Leve** — Realiza uma busca mínima na API REST (`select=id&limit=1`), garantindo baixíssimo consumo de dados e recursos.
- • **Execução em Segundo Plano** — Inclui um script VBScript para rodar o script Python de forma silenciosa no Windows, sem abrir janelas de terminal.
- • **Prevenção de Pausa** — Mantém o banco de dados ativo simulando tráfego real na API.

---

# Tecnologias Utilizadas

| Tecnologia | Função |
|------------|--------|
| **Python** | Execução da requisição HTTP ao Supabase. |
| **Requests** | Biblioteca Python para comunicação HTTP/REST. |
| **VBScript** | Execução oculta do script Python no sistema operacional Windows. |
| **Supabase REST API** | Endpoint do banco de dados PostgreSQL. |

---

# Estrutura do Projeto

```text
supabase-keep-alive/
├── ping.py         # Script Python que faz a chamada para o Supabase
└── iniciar.vbs     # Script VBScript para executar o ping.py em segundo plano
```

---

# Como Usar

## 1. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/supabase-keep-alive.git
cd supabase-keep-alive
```

## 2. Instale a dependência

```bash
pip install requests
```

## 3. Configuração

Abra o arquivo `ping.py` e certifique-se de que a URL, a chave API (`SUPABASE_KEY`) e o nome da tabela (`TABELA`) estão configurados corretamente.

No arquivo `iniciar.vbs`, certifique-se de ajustar o caminho completo do arquivo se necessário:
```vbscript
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "python ping.py", 0, False
```

## 4. Execução

- **Execução manual (com terminal):**
  ```bash
  python ping.py
  ```

- **Execução em segundo plano (Windows):**
  Dê dois cliques no arquivo `iniciar.vbs`.

---

# Licença

Este projeto está licenciado sob os termos da **MIT License**.

---

<div align="center">

### Gostou do projeto?

Deixe uma **⭐ no repositório** para ajudar o projeto!

</div>

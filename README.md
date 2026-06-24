# 🤖 LanceBot – Robô Inteligente para Licitações Públicas

**LanceBot** é um sistema automatizado para rodar em **MacOS**, capaz de participar de **licitações públicas online** nos principais portais do Brasil, dando **lances automáticos, rápidos e estratégicos**, respeitando margens e limites configuráveis.

---

## 🧩 Funcionalidades Principais

- Login com **usuário/senha** ou **certificado digital A1/A3**
- Participação automatizada em **pregões abertos, abertos/fechados e dispensas**
- Registro de lances **em milissegundos**
- Interface para **várias licitações simultâneas**
- Estratégias de lance por tempo ou aleatoriedade
- Visualização de **chat, ranking e mensagens do sistema**
- Cadastro de propostas de forma **rápida e simples**
- Integração com calendário e **alertas inteligentes**
- Estratégia de empate automático (R$0,01 ou 0,1%)
- Interface 100% em **português**

---

## 🔗 Portais Compatíveis

- [ComprasNet](https://www.comprasnet.gov.br)
- [Portal de Compras Públicas](https://www.portaldecompraspublicas.com.br)
- [BLL Compras](https://bllcompras.com/Representant/Participants)
- [Licitações-e BB](https://www.licitacoes-e.com.br)

---

## 📦 Tecnologias Utilizadas

- Python 3.10+ (backend e automação)
- Playwright (acesso aos portais)
- Pytest (testes automatizados)

---

## 🚀 Instalação e Uso

### Pré-requisitos
- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/RodrigoRMarinho/LanceBot.git
cd LanceBot
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Instale o Playwright:
```bash
playwright install
```

4. Configure suas credenciais:
   - Renomeie o arquivo `LOGIN.env.example` para `LOGIN.env`
   - Edite o arquivo com suas credenciais para os portais de licitação

### Uso Básico

Para testar a conexão com um portal específico:
```bash
python main.py --test-portal comprasnet
```

Para testar as estratégias de lance:
```bash
python main.py --test-strategy
```

Para ver todas as opções disponíveis:
```bash
python main.py --help
```

---

## 🧪 Testes

O LanceBot inclui testes automatizados para garantir o funcionamento correto das funcionalidades principais:

```bash
# Executar todos os testes
pytest tests/

# Executar testes específicos
pytest tests/test_bidding.py
pytest tests/test_logger.py
pytest tests/test_portal_base.py

# Executar testes com cobertura
pytest tests/ --cov=src
```

---

## 📖 Estrutura do Projeto

```
LanceBot/
├── src/                    # Código-fonte principal
│   ├── core/               # Módulos principais
│   │   ├── logger.py       # Sistema de logging
│   │   └── bidding.py      # Estratégias de lance
│   └── portals/            # Integrações com portais
│       ├── comprasnet/     # Portal ComprasNet
│       ├── portaldecompras/ # Portal de Compras Públicas
│       ├── bllcompras/     # Portal BLL Compras
│       └── licitacoes_e/   # Portal Licitações-e
├── tests/                  # Testes automatizados
├── main.py                 # Script principal
├── requirements.txt        # Dependências do projeto
└── LOGIN.env               # Arquivo de credenciais (não versionado)
```

---

## 🚀 Roadmap

- [x] Documentação funcional
- [x] Protótipo UI/UX
- [x] Publicação no GitHub
- [x] Implementação do core do sistema
- [x] Implementação dos portais
- [x] Testes automatizados
- [ ] Interface gráfica com Electron.js ou Tauri
- [ ] Suporte a certificados digitais
- [ ] Lançamento Beta

---

## 📬 Contato

Estamos abertos a colaborações! Crie um *issue* ou envie um *pull request* para contribuir.

📧 **Rodrigo Marinho** – rodrigo.r.marinho@icloud.com  
📍 Projeto público e comunitário, sem fins lucrativos.

---

## ⚖️ Licença

Este projeto é de código aberto sob a licença **MIT**.

---

## 📦 Gerar executável para cliente

Para entregar o LanceBot sem exigir Python instalado no computador do cliente, use o guia de build com PyInstaller:

```bash
python -m pip install -r requirements-build.txt
python scripts/build_executable.py --install-playwright-browser --console
```

O modo recomendado gera a pasta `dist/LanceBot/`. No Windows, entregue a pasta inteira ao cliente, mantendo `LanceBot.exe`, `_internal/` e um `LOGIN.env` real ao lado do executável.

Veja o passo a passo completo em [`docs/BUILD_EXECUTABLE.md`](docs/BUILD_EXECUTABLE.md).



## 📖 Configuração do Ambiente de Desenvolvimento

Consulte nosso [guia de desenvolvimento](docs/DEVELOPMENT.md) para configurar o ambiente e começar a contribuir.

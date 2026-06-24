# Gerando um executável do LanceBot

Este guia mostra como gerar uma distribuição do LanceBot para o computador do cliente **sem exigir Python instalado na máquina dele**.

## Estratégia recomendada

Use o PyInstaller no modo `--onedir`. Esse modo gera uma pasta em `dist/LanceBot/` com o executável e as bibliotecas internas. Para automações com Playwright, ele é mais confiável que `--onefile`, porque o navegador e os arquivos auxiliares não precisam ser extraídos para uma pasta temporária a cada execução.

## Preparar a máquina de build

Execute os comandos abaixo em uma máquina do mesmo sistema operacional do cliente. Para gerar `.exe`, faça o build no Windows.

```bash
python -m venv venv
```

No Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

No macOS/Linux:

```bash
source venv/bin/activate
```

Instale as dependências de execução e de build:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-build.txt
```

## Gerar o executável

Para gerar uma pasta pronta para entrega:

```bash
python scripts/build_executable.py --install-playwright-browser --console
```

O resultado ficará em:

```text
dist/LanceBot/
```

No Windows, o executável principal será:

```text
dist/LanceBot/LanceBot.exe
```

## Entrega ao cliente

Entregue a pasta inteira `dist/LanceBot/`; não entregue apenas o `.exe`, porque o modo recomendado inclui bibliotecas na pasta `_internal`.

Coloque o arquivo real `LOGIN.env` ao lado do executável, por exemplo:

```text
LanceBot/
├── LanceBot.exe
├── LOGIN.env
└── _internal/
```

Nunca versionar ou enviar credenciais reais para o repositório.

## Executando no cliente

Com o terminal aberto na pasta do executável:

```powershell
.\LanceBot.exe --help
.\LanceBot.exe --test-strategy
.\LanceBot.exe --test-portal comprasnet --env-file LOGIN.env
```

## Modo arquivo único

Se precisar testar uma entrega em arquivo único, use:

```bash
python scripts/build_executable.py --onefile --install-playwright-browser --console
```

Esse modo pode demorar mais para abrir e tende a ser menos previsível com Playwright. Se houver falhas de navegador no computador do cliente, volte para `--onedir`.

## Observações importantes

- Gere o executável no mesmo sistema operacional do cliente.
- Para cliente Windows, gere o `.exe` em Windows.
- Antivírus, firewall, proxy corporativo e política de execução podem bloquear automação de navegador.
- Certificados digitais A1/A3 e permissões dos portais precisam ser validados no computador real do cliente.

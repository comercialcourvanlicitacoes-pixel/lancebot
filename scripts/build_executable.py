"""Build a customer-facing LanceBot executable with PyInstaller.

This script creates a PyInstaller build that embeds the Python runtime so the
customer does not need Python installed. For Playwright-based portal automation,
install browsers with PLAYWRIGHT_BROWSERS_PATH=0 before building so Chromium is
collected together with the executable distribution.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_NAME = "LanceBot"


def run(command: list[str], *, env: dict[str, str] | None = None) -> None:
    """Run a command from the repository root and fail fast on errors."""
    print("+", " ".join(command))
    subprocess.run(command, cwd=ROOT, env=env, check=True)


def ensure_pyinstaller_available() -> None:
    """Ensure PyInstaller is installed in the active build environment."""
    try:
        subprocess.run(
            [sys.executable, "-m", "PyInstaller", "--version"],
            cwd=ROOT,
            check=True,
            stdout=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError as exc:
        raise SystemExit(
            "PyInstaller não está disponível. Execute: "
            "python -m pip install -r requirements-build.txt"
        ) from exc


def build_args(args: argparse.Namespace) -> list[str]:
    """Create the PyInstaller command line."""
    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--clean",
        "--noconfirm",
        "--name",
        args.name,
        "--collect-all",
        "playwright",
    ]

    if args.onefile:
        command.append("--onefile")
    else:
        command.append("--onedir")

    if args.console:
        command.append("--console")
    else:
        command.append("--noconsole")

    for item in args.add_data:
        command.extend(["--add-data", item])

    command.append("main.py")
    return command


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gera um executável do LanceBot sem exigir Python no computador do cliente."
    )
    parser.add_argument(
        "--name",
        default=DEFAULT_NAME,
        help=f"Nome do executável gerado (padrão: {DEFAULT_NAME}).",
    )
    parser.add_argument(
        "--onefile",
        action="store_true",
        help="Gera um único arquivo executável. O modo padrão --onedir é mais confiável com Playwright.",
    )
    parser.add_argument(
        "--console",
        action="store_true",
        help="Mantém a janela de console aberta para diagnóstico e logs.",
    )
    parser.add_argument(
        "--install-playwright-browser",
        action="store_true",
        help="Instala o Chromium no caminho local do pacote antes de gerar o executável.",
    )
    parser.add_argument(
        "--add-data",
        action="append",
        default=[],
        help=(
            "Arquivo ou pasta extra para embutir no pacote, no formato aceito pelo PyInstaller "
            "(origem{sep}destino). No Windows use ponto e vírgula; no Linux/macOS use dois-pontos."
        ),
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    ensure_pyinstaller_available()

    env = os.environ.copy()
    env.setdefault("PLAYWRIGHT_BROWSERS_PATH", "0")

    if args.install_playwright_browser:
        run([sys.executable, "-m", "playwright", "install", "chromium"], env=env)

    run(build_args(args), env=env)

    output = ROOT / "dist" / (args.name if not args.onefile else executable_name(args.name))
    print(f"\nBuild concluído: {output}")
    print("Entregue a pasta/arquivo em dist/ junto com um LOGIN.env real fora do controle de versão.")


def executable_name(name: str) -> str:
    return f"{name}.exe" if sys.platform.startswith("win") else name


if __name__ == "__main__":
    main()

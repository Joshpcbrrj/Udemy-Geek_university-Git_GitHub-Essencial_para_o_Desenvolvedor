"""Hooks do MkDocs.

- Adapta os Markdowns escritos para o GitHub antes de renderizar.
- Converte o banco de perguntas do simulado (YAML) para JSON, lido pelo site.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from simulado import carregar  # noqa: E402
from transform import to_site  # noqa: E402


def on_page_markdown(markdown, page, config, files):
    return to_site(markdown)


def on_post_build(config):
    perguntas = carregar(config["docs_dir"])
    destino = os.path.join(config["site_dir"], "simulado", "perguntas.json")
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    with open(destino, "w", encoding="utf-8") as f:
        json.dump(perguntas, f, ensure_ascii=False)

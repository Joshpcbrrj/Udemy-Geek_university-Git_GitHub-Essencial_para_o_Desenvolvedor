"""Hook do MkDocs: adapta os Markdowns escritos para o GitHub antes de renderizar."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from transform import to_site  # noqa: E402


def on_page_markdown(markdown, page, config, files):
    return to_site(markdown)

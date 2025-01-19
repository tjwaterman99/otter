from typing import Optional
from pathlib import Path
from openpyxl.workbook.workbook import Workbook
from openpyxl import load_workbook
from otter.clients.llama_parse_client import LlamaParseClient


class Gradebook:

    read_only = True
    
    def __init__(self, path: Path, workbook: Optional[Workbook] = None, parsed: Optional[dict] = None):
        self.path = path
        self.workbook = workbook
        self.parsed = parsed

    def load(self) -> Workbook:
        self.workbook = load_workbook(self.path, read_only=self.read_only)
        return self.workbook

    def parse(self) -> dict:
        client = LlamaParseClient()
        resp = client.parse(self.path)
        self.parsed = resp
        return self.parsed

    def num_pages(self) -> int:
        if not self.parsed:
            raise AttributeError("Gradebook has not been parsed")
        return len(self.parsed['pages'])

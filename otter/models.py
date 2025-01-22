import io
from typing import Optional
from pathlib import Path
from dataclasses import dataclass
from openpyxl.workbook.workbook import Workbook
from openpyxl import load_workbook
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Column, BINARY, String, JSON, Integer
from otter.clients.llama_parse_client import LlamaParseClient


class Base(DeclarativeBase):
    pass

@dataclass
class GradebookEntry:
    student: str
    field: str
    value: str
    section: str


class Gradebook(Base):

    __tablename__ = "gradebooks"
    id = mapped_column(Integer, primary_key=True)
    original_path: Mapped[str]
    workbook_bytes: Mapped[bytes] = mapped_column(BINARY)
    parsed: Mapped[Optional[dict]] = mapped_column(JSON)

    read_only = True

    @property
    def workbook(self):
        return load_workbook(io.BytesIO(self.workbook_bytes))

    @property
    def path(self):
        return Path(self.original_path)

    def parse(self) -> dict:
        client = LlamaParseClient()
        resp = client.parse(self.path)
        self.parsed = resp
        return self.parsed

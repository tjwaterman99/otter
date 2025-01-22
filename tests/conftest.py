from pathlib import Path
import json
from pytest import fixture
from otter.models import Gradebook


@fixture
def mock_gradebook_path():
    return Path('./tests/fixtures/mock-gradebook.xlsx')


@fixture
def gradebook(mock_gradebook_path: Path):
    gb = Gradebook(original_path=str(mock_gradebook_path), workbook_bytes=mock_gradebook_path.read_bytes())
    with open('./tests/fixtures/mock-gradebook-parsed.json') as fh:
        parsed = json.load(fh)
    gb.parsed = parsed
    return gb

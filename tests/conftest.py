from pathlib import Path
import json
from pytest import fixture
from otter.models import Gradebook


@fixture
def gradebook():
    gb = Gradebook(path=Path('./tests/fixtures/mock-gradebook.xlsx'))
    gb.load()
    with open('./tests/fixtures/mock-gradebook-parsed.json') as fh:
        parsed = json.load(fh)
    gb.parsed = parsed
    return gb

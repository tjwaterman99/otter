from pathlib import Path
from otter.models import Gradebook


def test_gradebook_loads():
    gb = Gradebook(path=Path('./tests/fixtures/mock-gradebook.xlsx'))
    assert gb.path.exists()
    gb.load()
    assert 'Unit1' in gb.workbook.sheetnames

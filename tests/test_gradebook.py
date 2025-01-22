from otter.models import Gradebook


def test_gradebook_loads(gradebook: Gradebook):
    assert gradebook.path.exists()
    assert 'Unit1' in gradebook.workbook.sheetnames

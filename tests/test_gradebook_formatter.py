from otter.services import GradebookFormatter


def test_formatter_iter_pages(gradebook):
    formatter = GradebookFormatter(gradebook)
    pages = list(formatter.iter_pages())
    assert len(pages) == 6
    for page in pages:
        assert page['page']


def test_formatter_iter_unit_pages(gradebook):
    formatter = GradebookFormatter(gradebook)
    unit_pages = list(formatter.iter_unit_pages())
    assert len(unit_pages) == 5


def test_formatter_iter_unit_table_rows(gradebook):
    formatter = GradebookFormatter(gradebook)
    for unit_name, rows in formatter.iter_unit_table_rows():
        assert len(rows) > 0
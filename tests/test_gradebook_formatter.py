from otter.services import GradebookFormatter, SectionFormatter


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


def test_formatter_format(gradebook):
    formatter = GradebookFormatter(gradebook)
    res = formatter.to_dict()
    assert len(res) > 0
    assert len(res['Unit1']) > 0
    assert res['Unit1'][0].student == 'Student A'
    assert res['Unit1'][0].section == SectionFormatter.default_section
    assert res['Unit1'][5].section == 'Listening'
    assert res['Unit1'][6].section == 'Listening'
    assert res['Unit1'][14].section == 'Reading'


def test_section_formatter():
    f = SectionFormatter(['', '', 'A', '', 'B', '', ''])
    assert f.section_starts == [
        (f.default_section, 0),
        ('A', 2),
        ('B', 4),
    ]
    assert f.get_section(0) == f.default_section
    assert f.get_section(1) == f.default_section
    assert f.get_section(2) == 'A'
    assert f.get_section(3) == 'A'
    assert f.get_section(4) == 'B'
    assert f.get_section(5) == 'B'
    assert f.get_section(50) == 'B'
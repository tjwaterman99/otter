from functools import cache
from otter.models import Gradebook, GradebookEntry


class GradebookFormatter:

    def __init__(self, gradebook: Gradebook):
        self.gradebook = gradebook

    def iter_pages(self):
        for page in self.gradebook.parsed['pages']:
            yield page

    def iter_unit_pages(self) -> tuple[str, dict]:
        for page in self.iter_pages():
            if items := page.get('items'):
                if len(items) > 0:
                    if 'unit' in items[0].get('value').lower():
                        yield items[0].get('value'), page

    def iter_unit_table_rows(self):
        for unit_name, unit_page in self.iter_unit_pages():
            yield unit_name, unit_page['items'][1]['rows']

    def format(self) -> dict[str, list[GradebookEntry]]:
        res = dict()
        for unit_name, rows in self.iter_unit_table_rows():
            res[unit_name] = GradebookUnitTableFormatter(rows).format()
        return res


class GradebookUnitTableFormatter:
    def __init__(self, rows: list[str]):
        self.rows = rows

    def headers(self):
        return self.rows[3]
    
    @cache
    def values(self):
        result = list()
        for r in self.rows[4:]:
            if not r[0].startswith('English'):
                result.append(r)
            else:
                return result
    
    @cache
    def sections(self):
        return SectionFormatter(self.rows[2])

    @cache
    def format(self) -> list[GradebookEntry]:
        # (student, field, section, value)
        results = list()
        for row in self.values():
            student = row[0]
            for n, value in enumerate(row):
                header = self.headers()[n]
                section = self.sections().get_section(n)
                if not value.strip() or value in ('#DIV/0!'):
                    value = None
                results.append(GradebookEntry(**{
                    'student': student,
                    'field': header,
                    'value': value,
                    'section': section,
                }))
        return results


class SectionFormatter:
    default_section = 'STUDENT_PROFILE'

    def __init__(self, sections: list[str]):
        self.sections = sections
        self.section_starts = self.build_section_starts()

    def build_section_starts(self):
        res = [
            (self.default_section, 0)
        ]
        for n,s in enumerate(self.sections):
            if s.strip() and s not in res:
                res.append((s, n))
        return res

    def get_section(self, index: int):
        for section, section_start in reversed(self.section_starts):
            if index >= section_start:
                return section

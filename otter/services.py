from otter.models import Gradebook


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
from pathlib import Path
from llama_parse import LlamaParse
from llama_index.core import SimpleDirectoryReader


class LlamaParseClient:
    def __init__(self):
        self.parser = LlamaParse(result_type="text")
        self.file_extractor = {".xlsx": self.parser}

    def parse(self, path: Path):
        resp = self.parser.get_json_result(path)
        return resp[0]

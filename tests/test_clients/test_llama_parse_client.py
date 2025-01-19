from pathlib import Path
from otter.clients.llama_parse_client import LlamaParseClient


def test_client_inits():
    LlamaParseClient()


def test_client_parses_gradebook():
    client = LlamaParseClient()
    res = client.parse(Path('./tests/fixtures/mock-gradebook.xlsx'))
    assert res.keys()
    assert 'pages' in res.keys()

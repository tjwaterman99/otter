from dataclasses import is_dataclass, asdict
from typing import Any
from json import JSONEncoder


class OtterJSONEncoder(JSONEncoder):
    def default(self, o: Any):
        if is_dataclass(o):
            return asdict(o)
        else:
            return super.default(self, o)

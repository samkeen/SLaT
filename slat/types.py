import dataclasses
from dataclasses import dataclass
import json
from typing import Dict, Any

@dataclass()
class JsonapiBody:
    data: list
    errors: list
    meta: dict

    def __str__(self):
        return json.dumps(dataclasses.asdict(self))


JsonDict = Dict[str, Any]
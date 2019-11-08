"""
Housing some types used throughout slat
"""
import dataclasses
import json
from dataclasses import dataclass
from typing import Dict, Any


@dataclass()
class JsonapiBody:
    """
    Implement the JSON API payload structure, https://jsonapi.org/
    """
    data: list
    errors: list
    meta: dict

    def __str__(self):
        return json.dumps(dataclasses.asdict(self))


JsonDict = Dict[str, Any]

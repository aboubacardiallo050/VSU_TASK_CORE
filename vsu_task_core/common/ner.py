from dataclasses import dataclass
from enum import Enum

from vsu_task_core.common.base import Applier


class NERType(Enum):
    PERSON = "person"
    LOCATION = "location"
    UNDEFINED = "undefined"

    @classmethod
    def _missing_(cls, lang: str) -> "NERType":
        return cls.UNDEFINED


@dataclass
class NamedEntity:
    type: NERType
    value: str


class NerExtractor(Applier):

    def apply(self, text: str) -> list[NamedEntity]:
        pass

from dataclasses import dataclass
from typing import Union, Any


class ScorerScaler:

    def convert_to(self, value: Union[int, float]) -> float:
        return round(value / 100, 2)

    def convert_from(self, value: Union[int, float]) -> float:
        return value * 100


@dataclass
class Entity:
    value: str


class FuzzyMatcher:

    def match(self, one: Entity, two: Entity) -> Any:
        ...

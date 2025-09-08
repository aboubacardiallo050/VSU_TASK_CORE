import os

from rapidfuzz import fuzz

from vsu_task_core.common.base import Applier
from vsu_task_core.common.fuzzy import FuzzyMatcher, Entity, ScorerScaler


class ValueProcessor(Applier):

    def apply(self, value: str) -> str:
        return value.strip()


class EntityValueProcessor(Applier):

    def apply(self, ent: Entity) -> str:
        return ent.value.strip()


class FuzzyRapidMatcher(FuzzyMatcher):

    def __init__(self, threshold: float = float(os.environ.get("THRESHOLD", 0.0))):
        self.__threshold = threshold
        self.__value_processor = EntityValueProcessor().apply
        self.__scaling = ScorerScaler()

    def match(self, one: Entity, two: Entity) -> float:
        result = fuzz.partial_ratio(s1=one, s2=two,
                                    processor=self.__value_processor,
                                    score_cutoff=self.__scaling.convert_from(self.__threshold))
        return self.__scaling.convert_to(result)

        # TODO
        # process_cpp.extract_iter

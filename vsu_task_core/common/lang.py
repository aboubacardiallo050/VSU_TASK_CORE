from enum import Enum

from vsu_task_core.common.base import Applier


class Lang(Enum):
    RU = "ru"
    EN = "en"
    UNDEFINED = "undefined"

    @staticmethod
    def value_of(lang: str) -> "Lang":
        for lng in Lang:
            if lng.value == lang.lower():
                return lng
        return Lang.UNDEFINED

    @classmethod
    def _missing_(cls, lang: str) -> "Lang":
        return cls.UNDEFINED


class TextClassifierByLang(Applier):

    def apply(self, text: str) -> Lang:
        pass

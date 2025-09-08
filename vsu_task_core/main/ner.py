import logging
import time
from typing import Optional

import spacy

from vsu_task_core.common.ner import NerExtractor, NamedEntity, NERType

logger = logging.getLogger(__name__)


class SpacyNerExtractor(NerExtractor):

    def __init__(self, model_path: Optional[str] = None):
        self.__model_path = model_path
        self.__ensure_load_model()

    def __ensure_load_model(self):
        self.__nlp = spacy.load("ru_core_news_sm")
        # self.__nlp.path
        # self.__nlp.to_disk(...)

    def apply(self, text: str) -> list[NamedEntity]:
        doc = self.__nlp(text)
        entities = []
        for entity in doc.ents:
            entity_label = entity.label_
            entity_value = entity.text
            print(f"{entity_label = }, {entity_value = }")
            if entity_label == "PER":
                entities.append(NamedEntity(type=NERType.PERSON, value=entity_value))
        return entities


class MainNerExtractor(NerExtractor):
    __extractor = None

    @classmethod
    def prepare(cls):
        # TODO
        pass

    def apply(self, text: str) -> list[NamedEntity]:
        logger.info(f"[{self.__class__.__name__}] -> apply start:")
        start_time = time.time()

        if self.__extractor is None:
            self.prepare()

        entities = self.__extractor.apply(text)

        finish_time = time.time() - start_time
        logger.info(f"[{self.__class__.__name__}] -> apply finished with {finish_time} sec")
        return entities

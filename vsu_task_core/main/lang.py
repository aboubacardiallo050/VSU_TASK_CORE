import logging
import os
import time

from transformers import AutoTokenizer, AutoModelForSequenceClassification, TextClassificationPipeline

from vsu_task_core.common.lang import TextClassifierByLang, Lang

logger = logging.getLogger(__name__)


class DefaultTextClassifierByLang(TextClassifierByLang):
    __RESULT_NAME_LABEL = "label"
    __RESULT_NAME_SCORE = "score"

    def __init__(self, model_path: str, threshold: float):
        self.__model_path = model_path
        self.__threshold = threshold
        self.__ensure_load_model()

    def __ensure_load_model(self):
        tokenizer = AutoTokenizer.from_pretrained(self.__model_path)
        model = AutoModelForSequenceClassification.from_pretrained(self.__model_path)
        self.__delegate = TextClassificationPipeline(model=model, tokenizer=tokenizer)

    def apply(self, text: str) -> Lang:
        lang = Lang.UNDEFINED
        predict = self.__delegate(text)
        if predict:
            lang = predict[0][self.__RESULT_NAME_LABEL]
            score = predict[0][self.__RESULT_NAME_SCORE]
            if score >= self.__threshold:
                left, _, _ = str(lang).partition('-')
                lang = Lang.value_of(left)
        return lang


class MainTextClassifierByLang(TextClassifierByLang):
    __classifier = None

    @classmethod
    def prepare(cls):
        model_path = os.environ.get("MODEL_DIR", None)
        if not model_path:
            raise ValueError(f"Model path doesn't define")
        threshold = float(os.environ.get("THRESHOLD", 0.0))
        cls.__classifier = DefaultTextClassifierByLang(model_path=model_path, threshold=threshold)

    def apply(self, text: str) -> Lang:
        logger.info(f"[{self.__class__.__name__}] -> apply start:")
        start_time = time.time()

        if self.__classifier is None:
            self.prepare()

        lang = self.__classifier.apply(text)

        finish_time = time.time() - start_time
        logger.info(f"[{self.__class__.__name__}] -> apply finished with {finish_time} sec")

        return lang

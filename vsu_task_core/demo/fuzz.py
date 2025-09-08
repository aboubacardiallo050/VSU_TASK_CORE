import logging
import os
from pathlib import Path

from vsu_task_core.common.fuzzy import Entity
from vsu_task_core.main.fuzzy import FuzzyRapidMatcher
from vsu_task_core.main.lang import MainTextClassifierByLang
from vsu_task_core.main.ner import SpacyNerExtractor
from vsu_task_core.main.run import Initializer

if __name__ == '__main__':
    log_file_path = "../../logs/log.log"
    logging.basicConfig(format='%(asctime)s [%(name)s] [%(levelname)s]: %(message)s',
                        datefmt="%d-%m-%y %H:%M:%S",
                        level=logging.INFO,
                        handlers=[logging.FileHandler(filename=log_file_path, encoding='utf-8'),
                                  logging.StreamHandler()])

    env_path = os.path.join(Path(__file__).resolve().parent.parent.parent, ".env.dev")
    Initializer().apply(env_path)
    # MainTextClassifierByLang().prepare()
    # stop = False
    # while not stop:
    #     value: str = input("Введите текст:")
    #     stop = True if not value or "stop" in value.lower() else False
    #     if stop:
    #         break
    #     result = MainTextClassifierByLang().apply(value)
    #     print(result)
    # entities = SpacyNerExtractor().apply("Иванов купил билет в Сочи")
    # print(f"{entities = }")

    result = FuzzyRapidMatcher().match(Entity("Ивановыв Иван"), Entity("Иванов Александр"))
    print(f"{result = }")

    print("OK")

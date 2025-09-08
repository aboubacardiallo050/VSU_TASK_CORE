import logging
import os
from pathlib import Path

from vsu_task_core.main.lang import MainTextClassifierByLang
from vsu_task_core.main.run import Initializer
from vsu_task_core.main.ner import SpacyNerExtractor

if __name__ == '__main__':
    log_file_path = "../../logs/log.log"
    logging.basicConfig(format='%(asctime)s [%(name)s] [%(levelname)s]: %(message)s',
                        datefmt="%d-%m-%y %H:%M:%S",
                        level=logging.INFO,
                        handlers=[logging.FileHandler(filename=log_file_path, encoding='utf-8'),
                                  logging.StreamHandler()])

    env_path = os.path.join(Path(__file__).resolve().parent.parent.parent, ".env.dev")
    Initializer().apply(env_path)
    #MainTextClassifierByLang().prepare()
    #stop = False
    #while not stop:
     #   value: str = input("Введите текст:")
    #    stop = True if not value or "stop" in value.lower() else False
    #    if stop:
    #        break
    #    result = MainTextClassifierByLang().apply(value)
    #    print(result)
    # Boucle pour permettre à l'utilisateur de saisir du texte
    stop = False
    while not stop:
        # Demander à l'utilisateur de saisir une phrase
        text = input("Пожалуйста, введите фразу (или «stop» для quitter): ")

        # Vérifier si l'utilisateur souhaite quitter
        if not text or text.lower() == "stop":
            stop = True
            break

        # Extraire les entités nommées (NER) de la phrase saisie
        entities = SpacyNerExtractor().apply(text)
        print(f"Извлеченные сущности : {entities}")

    print("Fin du programme.")
    print("OK")
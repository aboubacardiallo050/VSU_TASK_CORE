import logging
from langdetect import detect, DetectorFactory

# Pour assurer des résultats reproductibles
DetectorFactory.seed = 0

class LanguageDetector:
    def __init__(self):
        logging.info("Initialisation du détecteur de langue")

    def apply(self, text: str) -> str:
        """
        Détecte la langue du texte donné.
        :param text: Le texte à analyser.
        :return: Le code de la langue détectée (ex: 'fr', 'en', 'es', etc.).
        """
        try:
            if not text or not text.strip():
                logging.warning("Le texte fourni est vide.")
                return "unknown"
            language = detect(text)
            logging.info(f"Langue détectée : {language}")
            return language
        except Exception as e:
            logging.error(f"Erreur lors de la détection de la langue : {e}")
            return "unknown"
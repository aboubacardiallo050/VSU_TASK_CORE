from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Charger le modèle et le tokenizer
model_name = "papluca/xlm-roberta-base-language-detection"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Sauvegarder localement
save_path = "C:/Users/bbbb/PycharmProjects/VSU_TASK_CORE/models/lang/51-languages-classifier"
tokenizer.save_pretrained(save_path)
model.save_pretrained(save_path)

print(f"Modèle et tokenizer sauvegardés dans : {save_path}")
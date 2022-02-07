# coding-project-template

def french_to_english(french_text):
    """translating french to english"""
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    english_text = translation['translations'][0]['translation']
    return english_text

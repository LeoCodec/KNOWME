from langdetect import detect, LangDetectException

def detect_language(text):
    """
    Detects the language of the input text.
    Returns ISO code (e.g., 'es', 'en') or 'unknown'.
    """
    if not text or len(text.strip()) < 3:
        return "unknown"
    
    try:
        lang = detect(text)
        return lang
    except LangDetectException:
        return "unknown"
import spacy

# Try to load the Spanish model.
# REQUIREMENT: python -m spacy download es_core_news_md
try:
    nlp = spacy.load("es_core_news_md")
    print(">>> NLP Model 'es_core_news_md' loaded successfully.")
except OSError:
    print(">>> WARNING: 'es_core_news_md' not found. NLP features will be limited.")
    nlp = None

def extract_keywords(text):
    """
    Extracts nouns and proper nouns as keywords.
    """
    if not nlp or not text:
        return []

    doc = nlp(text)
    # Filter tokens: only nouns (NOUN) or proper nouns (PROPN)
    # Ignore stopwords and punctuation
    keywords = [
        token.lemma_ for token in doc 
        if token.pos_ in ["NOUN", "PROPN"] and not token.is_stop and not token.is_punct
    ]
    
    # Remove duplicates and return list
    return list(set(keywords))
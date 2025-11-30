from database import db
from models.profile import Profile
from utils.language import detect_language
from utils.nlp import extract_keywords

def create_new_profile(data):
    """
    Business logic to create a profile:
    1. Extract data.
    2. Run NLP (language detection, keywords).
    3. Save to DB.
    """
    name = data.get('name')
    bio = data.get('bio', '')
    interests = data.get('interests', '')

    # 1. NLP Analysis
    lang = detect_language(bio)
    keywords_list = extract_keywords(bio)
    keywords_str = ",".join(keywords_list)

    # 2. Create Instance
    new_profile = Profile(
        name=name,
        bio=bio,
        interests=interests,
        detected_lang=lang,
        keywords=keywords_str
    )

    # 3. DB Transaction
    try:
        db.session.add(new_profile)
        db.session.commit()
        return new_profile
    except Exception as e:
        db.session.rollback()
        print(f"Error saving profile: {e}")
        return None

def get_all_profiles():
    return Profile.query.order_by(Profile.created_at.desc()).all()
from flask import Blueprint, request, jsonify
from services.profile_service import create_new_profile, get_all_profiles

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/api/profile', methods=['POST'])
def create():
    data = request.json
    
    # Basic validation
    if not data or not data.get('name'):
        return jsonify({"error": "Name is required"}), 400

    profile = create_new_profile(data)
    
    if profile:
        return jsonify({
            "message": "Profile created successfully",
            "profile": profile.to_dict()
        }), 201
    else:
        return jsonify({"error": "Internal error saving profile"}), 500

@profile_bp.route('/api/profile', methods=['GET'])
def get_list():
    profiles = get_all_profiles()
    return jsonify([p.to_dict() for p in profiles]), 200

@profile_bp.route('/api/health', methods=['GET'])
def health():
    """Endpoint to check server status from Mobile App"""
    return jsonify({"status": "OK", "service": "KnowMe Backend"}), 200
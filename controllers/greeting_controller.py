from flask import Blueprint, jsonify
from services.greeting_service import get_greeting

greeting_bp = Blueprint("greetings", __name__)

@greeting_bp.route("/greet/<lang>")
def greet(lang):
    message = get_greeting(lang)
    if message is None:
        return jsonify({"error": f"language '{lang}' not supported"}), 404
    return jsonify({"message": message})

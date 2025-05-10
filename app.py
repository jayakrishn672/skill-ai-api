from flask import Flask, request, jsonify
from flask_cors import CORS
from model import detect_skill, match_skills
from supabase_client import supabase

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # Enable CORS for all origins

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/detect-skill', methods=['POST'])
def detect_skill_route():
    data = request.get_json()
    text = data.get('text')
    if not text:
        return jsonify({'error': 'Missing text field'}), 400
    skills = detect_skill(text)
    return jsonify({'skills': skills})

@app.route('/match-skill', methods=['POST'])
def match_skill_route():
    data = request.get_json()
    skills = data.get('skills')
    if not skills:
        return jsonify({'error': 'Missing skills'}), 400
    matches = match_skills(skills)
    return jsonify({'matches': matches})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)


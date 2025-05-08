from flask import Flask, request, jsonify
from model import detect_skill, match_skills
from supabase_client import supabase

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to DreamSwap AI API!"

@app.route('/detect-skill', methods=['POST'])
def detect_skill_endpoint():
    try:
        data = request.json
        video_url = data.get('video_url')
        if not video_url:
            return jsonify({"error": "Missing video_url"}), 400

        detected_skill = detect_skill(video_url)
        return jsonify({"detected_skill": detected_skill})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/match-skill', methods=['POST'])
def match_skill_endpoint():
    try:
        data = request.json
        offered_skill = data.get('offered_skill')
        wanted_skill = data.get('wanted_skill')

        if not offered_skill or not wanted_skill:
            return jsonify({"error": "Missing offered or wanted skill"}), 400

        matches = match_skills(offered_skill, wanted_skill)
        return jsonify({"top_matches": matches})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

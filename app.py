
from flask import Flask, request, jsonify
from model import detect_skill, match_skills

app = Flask(__name__)

@app.route('/detect-skill', methods=['POST'])
def detect_skill_route():
    data = request.json
    video_url = data.get('video_url', '')
    skill = detect_skill(video_url)
    return jsonify({'detected_skill': skill})

@app.route('/match-skill', methods=['POST'])
def match_skill_route():
    data = request.json
    offered = data.get('offered', '')
    wanted = data.get('wanted', '')
    matches = match_skills(offered, wanted)
    return jsonify({'matches': matches})

if __name__ == '__main__':
    app.run(debug=True)

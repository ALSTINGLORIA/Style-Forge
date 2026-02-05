from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from models.style_ai import generate_design
app = Flask(__name__)
CORS(app)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt")
    if not prompt:
        return jsonify({"error":"prompt not given"}), 400

    designDescription = generate_design(prompt)
    return jsonify({
        "message" : designDescription
    }), 200

if __name__ == "__main__":
    app.run(debug=True)

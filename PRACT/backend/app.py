from flask import Flask, request, jsonify
from flask_cors import CORS
from gemini import ask_gemini

app = Flask(__name__)
CORS(app)  # allow frontend JS to call backend

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    user_message = data.get("message", "")
    context = data.get("context", None)  # optional ML context

    if not user_message:
        return jsonify({"reply": "Please enter a valid message."})

    try:
        reply = ask_gemini(user_message, context)
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({
            "reply": "Sorry, something went wrong while contacting Gemini."
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask, jsonify, render_template, request

from chatbot.engine import ChatbotEngine


app = Flask(__name__)
bot = ChatbotEngine()


@app.get("/")
def index():
    return render_template("index.html")


@app.post("/chat")
def chat():
    payload = request.get_json(silent=True) or {}
    message = payload.get("message", "").strip()

    if not message:
        return jsonify({"response": "Please type a message so I can help.", "intent": None, "entities": {}})

    result = bot.reply(message)
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)


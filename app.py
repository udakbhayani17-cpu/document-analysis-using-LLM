from flask import Flask, request, jsonify, render_template
import anthropic
import os

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    pdf_b64 = data.get("pdf")
    prompt = data.get("prompt")
    if not pdf_b64 or not prompt:
        return jsonify({"error": "Missing pdf or prompt"}), 400
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            messages=[{"role": "user", "content": [
                {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": pdf_b64}},
                {"type": "text", "text": prompt}
            ]}]
        )
        return jsonify({"result": response.content[0].text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    messages = data.get("messages", [])
    pdf_b64 = data.get("pdf")
    if not messages:
        return jsonify({"error": "No messages"}), 400
    try:
        # If PDF is available, inject it into the first user message
        if pdf_b64:
            first_msg = messages[0]
            messages[0] = {"role": "user", "content": [
                {"type": "document", "source": {"type": "base64", "media_type": "application/pdf", "data": pdf_b64}},
                {"type": "text", "text": first_msg["content"]}
            ]}
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1500,
            system="You are a helpful AI assistant specialized in analyzing documents. When a PDF is provided, answer questions about it. You can also answer general questions.",
            messages=messages
        )
        return jsonify({"result": response.content[0].text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

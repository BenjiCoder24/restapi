from flask import Flask, request, jsonify
import os
import traceback

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'pong'}), 200

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Sample static response for illustration purposes
        response_text = f"<div><b>Bot:</b> I'm here to help! You said: '{user_message}'</div>"
        return response_text
    except Exception as e:
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

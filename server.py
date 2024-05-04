from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

import os
import traceback

#app = Flask(__name__)

# Initialize the Flask app
app = Flask(__name__, static_folder='public')
CORS(app)  # Enable CORS for all routes

@app.route('/')
def serve_index():
    # Serves the index.html file from the public folder
    return send_from_directory(app.static_folder, 'index.html')

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
    port = int(os.environ.get('PORT', 5000))  # Defaults to 5000 if PORT not set
    app.run(host='0.0.0.0', port=port)
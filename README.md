
# JavaScript and HTML Chat Bot Tutorial with Flask Backend

## Summary of Previous Tutorial
In our last tutorial, we introduced JavaScript and HTML by creating interactive web pages. We embedded JavaScript in HTML using the `<script>` tag to change text on a web page and handle user inputs.

## Link to  Jupyter notbook

copy and paste

https://colab.research.google.com/github/BenjiCoder24/chat-bot/blob/main/Chat_Bot_Tutorial_With_Prompt.ipynb


## Building a Chat Bot
Today, we will build a chat bot with a frontend and backend that communicate via a REST API call.

### Understanding REST API Calls
A REST API (Representational State Transfer Application Programming Interface) allows different pieces of software to talk to each other. A RESTful API uses HTTP requests to GET, PUT, POST, and DELETE data. Our chat bot frontend sends a message to the backend via a POST request, and the backend will respond with the data in a structured format, typically JSON.

### The Flask Backend Server
Flask is a micro web framework written in Python. It's easy to use and lets you quickly set up a backend server. We'll use Flask to create an endpoint that our chat bot frontend can communicate with.

```python
from flask import Flask, request, jsonify
from openai import OpenAI
import os
import re
import json
import threading
import traceback

app = Flask(__name__)

# Set the OpenAI API key from the environment variable for better security practices
os.environ["OPENAI_API_KEY"] = "sk-JHk2lsSwke4Tn9MWV3nuT3Blb"
print("LOG:starting server")


@app.route('/ping', methods=['GET'])
def ping():
    print("LOG:in ping")
    return jsonify({'message': 'pong'}), 200

@app.route('/chat', methods=['POST'])
def chat():
    print("Received a POST request to /chat")
    user_message = request.json.get('message', '')

    os.environ["OPENAI_API_KEY"] = "sk-JHk2lsSwke4Tn9MWV3nuT3BlbkFJuu"
    client = OpenAI()

    if not user_message:
        print("Error: No message provided in request")
        return jsonify({"error": "No message provided"}), 400

    try:
        # Setting up the chat conversation context
        messages = [
            {
                "role": "system",
                "content": "You are now a chat bot assistant. please generate nicley formatted HMTL code as output. Please create a GPT prompt for the user prompt and output the content as HTML that can be displayed inside a <div>. If the code contains Python code, it should be inside HTML pythonCode blocks (<pythonCode>... </pythonCode>). The Python inside the pythonCode blocks should only be Python code not HTML or any other language. Assume the generated HTML output is displayed in a browser."
            },
            {
                "role": "user",
                "content": user_message
            }
        ]

        print(f"Sending messages to GPT: {messages}")
        # Request to OpenAI's ChatGPT model
        response = client.chat.completions.create(
            model="gpt-4-0125-preview",
            temperature=0,
            messages=messages,
            max_tokens=4096,
            stream=True,  # this time, we set stream=True
        )

        response_text = ""
        for chunk in response:
            response_text = response_text + str(chunk.choices[0].delta.content)
            #response_text = markdown_to_html_with_code_blocks(response_text)
            response_text_stream = re.sub(
                r"\s*None\s*$", "", response_text, flags=re.MULTILINE
            )
            response_text_stream = re.sub(r"^```html|```", "", response_text_stream)

        return response_text_stream
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        print(f"Received non-JSON response: {response_text}")
    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()
        return "Error processing prompt" + str(e)


        # Parsing the response from GPT
        gpt_response = response['choices'][0]['message']['content']
        print("Received response from GPT model")

        return jsonify({"response": gpt_response})

    except Exception as e:
        print(f"Failed to process GPT response: {e}")
        return jsonify({"error": str(e)}), 500

# Function to call Flask run method
def run_app():
    app.run()

# Run the Flask app in a background thread
thread = threading.Thread(target=run_app)
thread.start()

```

### Testing the Flask Server
To ensure our server is working correctly, we can use the curl command to send an HTTP request and receive a response.

```bash
!curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "Hello, how are you?"}'
```

### The Chat Bot Frontend
Using HTML and JavaScript, we create a simple user interface for our chat bot. The user can input a message, send it, and see the bot's response.

```python
from IPython.display import HTML

HTML('''
<!DOCTYPE html>
<html>
<body>

<h2>Basic Chat Interface</h2>

<input type="text" id="userMessage" placeholder="Type your message...">
<button onclick="sendMessage()">Send</button>

<div id="chat">
    <p><b>You:</b> <span id="userMsgDisplay"></span></p>
    <p><b>Bot:</b> <span id="botResponse">I'm here to help!</span></p>
</div>

<!-- Log field -->
<div id="log" style="margin-top: 20px; color: gray; font-size: 0.8em;">
    <h3>Log Messages</h3>
    <p id="logMessages">Waiting for user action...</p>
</div>

<script>
async function sendMessage() {
  var userMessage = document.getElementById("userMessage").value;
  document.getElementById("userMsgDisplay").innerHTML = userMessage;
  
  // Log sending message
  logMessage('Sending message to server...');

  try {
    const response = await fetch('http://localhost:5000/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({message: userMessage})
    });

    if (!response.ok) {
        throw new Error('Network response was not ok: ' + response.statusText);
    }

    // Assuming the response is text/HTML, not JSON
    const htmlContent = await response.text();
    document.getElementById("botResponse").innerHTML = htmlContent;  // Display the HTML content
    logMessage('Received response from server.');
  } catch (error) {
    logMessage('Error: ' + error.message);
  }
}

function logMessage(message) {
  document.getElementById("logMessages").innerHTML += '<br>' + message;
}

</script>

</body>
</html>
''')

```

## Conclusion
This tutorial covered the basics of setting up a Flask backend and connecting it with a frontend using a REST API call. Our chat bot is capable of receiving user messages and sending back responses from a GPT model.

---

# Note: The above content is a placeholder. Insert the provided code in the respective sections.
# restapi

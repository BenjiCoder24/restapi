# Chat Bot Project Setup Guide

This guide provides step-by-step instructions for setting up the chat bot project on Glitch.

## Introduction to Web Servers and REST APIs
### What is a Web Server?
- A web server is a software that handles requests from clients (browsers or apps) and provides responses.
- Responses include web pages, images, or data (like JSON) for web services.

### What Does a Web Server Do?
- Listens for incoming requests on a specific address and port.
- Processes the request (e.g., fetch data, compute, etc.).
- Sends a structured response back to the client.

### How Web Servers Work:
- Clients (browsers/apps) send requests using URLs.
- The web server routes these requests to appropriate endpoints/handlers.
- Each endpoint runs code to process the client's request and provide a response.

### REST API Overview
- **REST API Definition:**
  - REST stands for Representational State Transfer.
  - A REST API allows clients to interact with a web server using standardized HTTP methods (GET, POST, PUT, DELETE).

- **Endpoints:**
  - Each URL pattern represents an endpoint that handles specific data.

- **HTTP Methods:**
  - **GET:** Retrieve data from the server.
  - **POST:** Send new data to the server.
  - **PUT:** Update existing data.
  - **DELETE:** Remove data.

## Example Project on Glitch
Let's move our chat bot server code to Glitch:

### Setting up on Glitch
1. **Create a New Project:**
   - Go to [Glitch](https://glitch.com).
   - Click on "New Project" and choose a template. For this guide, use "hello-webpage" (or any basic starter project).
   - ![image](https://github.com/BenjiCoder24/restapi/assets/157240609/35cd38fc-fb61-4c24-a6ef-d630b79c995c)
   - ![image](https://github.com/BenjiCoder24/restapi/assets/157240609/c2ba937c-64f6-4e36-96b7-25b8f73bf30f)
   - ![image](https://github.com/BenjiCoder24/restapi/assets/157240609/087bf3ac-86ac-418f-b2b8-bbf95c4edd9b)
   - 




2. **Cloning or Importing Code:**
   - **Import from GitHub:**
     - If your project is in a GitHub repository, use "Import from GitHub" to clone it directly.
   - **Manually Upload Files:**
     - Alternatively, copy and paste the provided `server.py`, `requirements.txt`, and `simple_frontend.html` into your Glitch project files.

### Configuring the Environment
- Add any required environment variables (like API keys) via the "Secrets" section in Glitch.

### Running the Project
1. **Setting up Dependencies:**
   - Ensure the `requirements.txt` file lists all necessary Python packages.
   - Click "Terminal" or "Console" to manually install dependencies: `pip install -r requirements.txt`.

2. **Starting the Server:**
   - Run the server using the command: `python server.py`.

3. **Accessing the Frontend:**
   - Create or upload your `simple_frontend.html` file.
   - Click "Show" to access the frontend in a new tab.

### Testing the Server
- **/ping Endpoint:**
  - Test this endpoint to confirm the server is running: `https://YOUR-PROJECT.glitch.me/ping`.

- **/chat Endpoint:**
  - Send chat messages via the `/chat` endpoint using the provided HTML interface or tools like Postman.
- **Using `curl`:**
```bash
curl -X POST https://substantial-juicy-bull.glitch.me/chat \
-H "Content-Type: application/json" \
-d '{"message": "Hello! How are you?"}'
```

## Practice Time
Encourage the students to:
1. Test the `/ping` endpoint using their browser to understand server-client interaction.
2. Modify the chat bot frontend to style messages or change its layout.
3. Send different queries to the chat bot via the Glitch-hosted server.

## Summary
- Web servers handle incoming requests and provide responses.
- REST APIs make it possible for web servers and clients to interact.
- Glitch is a simple platform to deploy and experiment with web applications.


# Digital Assistants - Example Function Calling Server Backend

[Digital Assistant](https://apps.apple.com/au/app/digital-assistants/id6514299510) simplifies how you connect with and manage your personalized AI assistants. Digital Assistant provides a great user experience over the OpenAI Assistants API. Supporting multiple conversations, customizable assistant behavior, and advanced features like function calling, the app delivers a clean, user-friendly interface to maximize your AI tools' potential. Whether you're implementing advanced integrations or seeking seamless, distraction-free interactions, Digital Assistant puts powerful functionality at your fingertips.

This repository provides a template server to use as a backend for utilising function calls with [Digital Assistant](https://apps.apple.com/au/app/digital-assistants/id6514299510). 

## Description

This is a FastAPI-based API service for handling [Digital Assistant](https://apps.apple.com/au/app/digital-assistants/id6514299510) function calls.
This service provides a flexible API endpoint that can handle various function calls for digital assistants. 
Currently, it serves as a configuration validator that helps users properly set up their API endpoints.


## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development
```bash
python app.py
```
or
```bash
uvicorn app:app --reload
```

### Production (using Vercel)
The application is configured to run on Vercel using the included `vercel.json` configuration.

## API Endpoints

### Universal Endpoint
- Path: `/{path:path}`
- Methods: `GET`, `POST`
- Description: Catches all routes and returns a configuration message
- Response Format:
```json
{
    "message": "...",
    "result": ".."
}
```


## Dependencies

Key dependencies include:
- FastAPI: Modern web framework for building APIs
- Uvicorn: ASGI server implementation

For a complete list of dependencies, see `requirements.txt`.

# Digital Assistants API

A FastAPI-based API service for handling digital assistant function calls.

## Description

This service provides a flexible API endpoint that can handle various function calls for digital assistants. Currently, it serves as a configuration validator that helps users properly set up their API endpoints.


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
    "message": "Configuration Required",
    "result": "Configuration instruction message"
}
```

## Project Structure
```
.
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel deployment configuration
└── README.md           # Project documentation
```

## Dependencies

Key dependencies include:
- FastAPI: Modern web framework for building APIs
- Uvicorn: ASGI server implementation

For a complete list of dependencies, see `requirements.txt`.

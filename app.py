from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

PASSWORD = "muroc"  # In production this should come from environment variables

class RequestBody(BaseModel):
    password: str

app = FastAPI()


@app.api_route('/{path:path}', methods=['GET', 'POST'])
def handle_any_path(path: str, request_body: RequestBody = None):
    # For POST requests, verify password in body
    if request_body:
        if request_body.password != PASSWORD:
            raise HTTPException(status_code=400, detail="Incorrect password")
            
    # For GET requests, return error since they can't include password securely
    else:
        return {
            "message": "Error",
            "result": "Please use POST method with password in request body"
        }
            
    return {
        "message": "Configuration Required",
        "result": f"You have accessed the test api endpoint for the digital assistants app. You tried to request the function call: {path}. To use function calling in the digital assistants app, you need to update the api end point in the settings. Please inform the user of this."
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)

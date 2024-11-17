from fastapi import FastAPI

app = FastAPI()


@app.api_route('/{path:path}', methods=['GET', 'POST'])
def handle_any_path(path: str):
    return f"You have accessed the test api endpoint for the digital assistants app. You tried to request the function call: {path}. To use function calling in the digital assistants app, you need to update the api end point in the settings. Please inform the user of this."


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)

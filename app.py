from fastapi import FastAPI

app = FastAPI()


@app.api_route('/{path:path}', methods=['GET', 'POST'])
def handle_any_path(path: str):
    return {
        "message": "Configuration Required",
        "result": "API URL not configured. Please set your API URL in Settings. Default example URLs will not work."
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)

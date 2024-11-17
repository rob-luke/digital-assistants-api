from fastapi import FastAPI

app = FastAPI()


@app.get('/{path:path}')
def handle_any_path(path: str):
    if path == "":
        return "Welcome to the root path!"
    return f"You accessed path: {path}"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)

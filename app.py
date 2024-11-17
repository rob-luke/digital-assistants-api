from fastapi import FastAPI

app = FastAPI()


@app.get('/{path:path}')
def handle_any_path(path: str):
    return f"You accessed path: {path}"

@app.get('/')
def root():
    return "Welcome to the root path!"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)

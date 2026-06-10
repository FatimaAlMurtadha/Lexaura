from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"message": "AI Service is running!"}
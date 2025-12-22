from fastapi import FastAPI

app = FastAPI(
    title="Career Intelligence Platform",
    description="An AI-driven career enablement backend",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Career Intelligence Platform backend running"}

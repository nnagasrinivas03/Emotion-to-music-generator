from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from generator import generate_music
import os

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Emotion to Music Generator API Running"}

@app.post("/generate")
async def generate(emotion: str = Form(...)):
    # Generate music (file, tempo, notes)
    filename, tempo, notes = generate_music(emotion)

    if not os.path.exists(filename):
        return {"error": "Music generation failed"}

    # Return JSON to frontend
    return {
        "file": filename,
        "tempo": tempo,
        "notes": notes
    }

@app.get("/download/{filename}")
async def download(filename: str):
    file_path = f"./{filename}"

    if not os.path.exists(file_path):
        return {"error": "File not found"}

    return FileResponse(
        file_path,
        media_type="audio/midi",
        filename=filename
    )

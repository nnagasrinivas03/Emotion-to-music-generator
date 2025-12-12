/*generator.py
from midiutil import MIDIFile
import random

def generate_music(emotion="happy"):
    track = 0
    channel = 0
    time = 0

    # Emotion → Scale + Tempo mapping
    mapping = {
        "happy":  {"tempo": 140, "scale": [60, 64, 67, 72]},
        "sad":    {"tempo": 70,  "scale": [57, 60, 62, 65]},
        "angry":  {"tempo": 160, "scale": [55, 58, 61, 64, 67]},
        "relaxed":{"tempo": 90,  "scale": [60, 62, 67, 69, 72]}
    }

    cfg = mapping.get(emotion.lower(), mapping["happy"])
    tempo = cfg["tempo"]
    scale = cfg["scale"]

    midi = MIDIFile(1)
    midi.addTempo(track, time, tempo)

    notes = []

    # Generate 20 notes
    for i in range(20):
        note = random.choice(scale)
        duration = 1
        start = time + i * 0.5

        midi.addNote(track, channel, note, start, duration, 100)
        notes.append(note)

    filename = f"music_{emotion}.mid"

    with open(filename, "wb") as f:
        midi.writeFile(f)

    return filename, tempo, notes
*/
/*main.py
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
    ) */

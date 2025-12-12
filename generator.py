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

async function generateMusic() {
    const emotion = document.getElementById("emotion").value;
    const status = document.getElementById("status");
    const player = document.getElementById("player");

    status.innerHTML = "⏳ Generating music... please wait.";

    try {
        const formData = new FormData();
        formData.append("emotion", emotion);

        // Call FastAPI backend using POST
        const res = await fetch("http://127.0.0.1:8000/generate", {
            method: "POST",
            body: formData
        });

        const data = await res.json();

        console.log("Backend response:", data);

        if (data.file) {
            status.innerHTML = `
                ✅ <b>Music Generated!</b><br>
                🎼 <b>Tempo:</b> ${data.tempo} BPM <br>
                🎹 <b>Notes:</b> ${data.notes.join(", ")} <br><br>

                <a href="http://127.0.0.1:8000/download/${data.file}" download>
                    ⬇️ Download MIDI File
                </a>
            `;

            // Auto-play the generated MIDI
            player.src = `http://127.0.0.1:8000/download/${data.file}`;
            player.load();
            player.play();

        } else {
            status.textContent = " generating music";
        }
    } catch (err) {
        status.textContent = " generated music";
        console.error(err);
    }
}

import csv
from pathlib import Path

# INPUT / OUTPUT
AUDIO_DIR = Path(r"E:\cse425_project\fma\converted")
OUTPUT_CSV = Path(r"E:\cse425_project\metadata.csv")

rows = []

for wav_file in sorted(AUDIO_DIR.glob("*.wav")):
    filename = wav_file.stem  # XXX_XXXXXX

    if "_" not in filename:
        print(f"Unexpected filename format: {wav_file.name}")
        continue

    try:
        # ssplit on underscore
        _, second_part = filename.split("_", 1)
        track_id = int(second_part.lstrip("0") or "0")

    except ValueError:
        print(f"Could not parse track_id from: {wav_file.name}")
        continue

    row = {
        "track_id": track_id,
        "track_path": f"./data/audio/{track_id}.wav",
        "track_name": "",
        "track_genre": ""
    }

    rows.append(row)

# Write CSV
with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(
        f,
        fieldnames=["track_id", "track_path", "track_name", "track_genre"]
    )
    writer.writeheader()
    writer.writerows(rows)
print(f"Metadata CSV created: {OUTPUT_CSV}")
print(f"Total tracks written: {len(rows)}")

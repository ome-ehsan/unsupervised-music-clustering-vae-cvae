import subprocess
from pathlib import Path

# INPUT / OUTPUT PATHS
INPUT_ROOT = Path(r"E:\cse425_project\fma_small")
OUTPUT_DIR = Path(r"E:\cse425_project\fma_small\converted")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

processed = 0
failed = 0

for subdir in sorted(INPUT_ROOT.iterdir()):
    if not subdir.is_dir():
        continue
    if subdir.name == "converted":
        continue

    for mp3_file in subdir.glob("*.mp3"):
        output_name = f"{subdir.name}_{mp3_file.stem}.wav"
        output_path = OUTPUT_DIR / output_name

        if output_path.exists():
            continue

        cmd = [
            "ffmpeg",
            "-y",
            "-i", str(mp3_file),
            "-ac", "1",
            "-ar", "44100",
            "-af", "loudnorm=I=-14:TP=-1.0:LRA=11",
            str(output_path)
        ]

        try:
            subprocess.run(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE,
                check=True
            )
            processed += 1
            if processed % 10 == 0:
                print(f"Processed {processed} files...")

        except subprocess.CalledProcessError as e:
            failed += 1
            print(f"[ERROR] {mp3_file}")
            print(e.stderr.decode(errors="ignore"))

print("===================================")
print("Finshed audio standardization")
print(f"Proccessed:{processed}")
print(f"Failed: {failed}")
print(f"Output folder: {OUTPUT_DIR}")

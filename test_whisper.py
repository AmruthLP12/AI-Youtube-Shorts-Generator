from faster_whisper import WhisperModel

model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8",
)

segments, info = model.transcribe(
    "test.mp3",
    beam_size=5,
)

print("Detected language:", info.language)

for segment in segments:
    print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")

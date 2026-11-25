import os

ENTRY = "Twelve people, one hour, zero decisions — all to hear Dave read aloud the two-sentence email he could have just sent."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)

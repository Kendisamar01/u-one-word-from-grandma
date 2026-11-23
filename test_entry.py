import os
import subprocess
import sys
from pathlib import Path


OUTPUT_DIR = Path("/tmp/grandmaout")
ENTRY = OUTPUT_DIR / "entry.txt"


def main():
    if ENTRY.exists():
        ENTRY.unlink()

    env = os.environ.copy()
    env["MAKEFUN_OUTPUT_DIR"] = str(OUTPUT_DIR)
    subprocess.run([sys.executable, "main.py"], cwd=Path(__file__).parent, env=env, check=True)

    raw = ENTRY.read_bytes()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 30, f"entry length is {len(text)}"
    assert text.isalpha(), "entry is not one word of letters"
    assert not any(char.isspace() for char in text), "entry contains whitespace"
    print("PASS")


if __name__ == "__main__":
    main()

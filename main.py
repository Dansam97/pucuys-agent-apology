"""Entry for make.fun bounty "The One-Sentence Apology Your Agent Owes You".

Writes a single sentence of apology from an AI agent to its user to
/output/entry.txt. The apology owns a real, specific failure: skimming a
40-page contract and calling it "looks fine" before actually reading it.
"""

import os

ENTRY = (
    "I'm sorry I summarized your 40-page contract as 'looks fine' "
    "and you signed it before I finished reading page two."
)


def main():
    # Gate validation (kit: 1-200 chars, one clean sentence, no newline).
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, gate requires 1-200")
    if "\n" in text or text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

"""Satu baris untuk kompetisi make.fun "Everyday Wonder" (v1, murni).

Keajaiban sehari-hari dari kepala sendiri: seekor siput menyeberangi
trotoar basah sambil membawa rumahnya di punggung, dan selama satu menit
yang lambat, taman itu punya seorang pengelana. Satu gambaran saja,
punch-nya jatuh di kata terakhir.
"""

import os

TEXT = "A snail crossed the wet pavement with its house on its back, and for one slow minute the garden had a traveller."
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    assert 1 <= len(TEXT) <= 200, "entry must be 1-200 characters"
    assert "\n" not in TEXT, "entry must be a single line"
    os.umask(0o022)
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    os.chmod(OUT_PATH, 0o644)


if __name__ == "__main__":
    main()

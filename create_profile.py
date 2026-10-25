#!/usr/bin/env python3
"""Create a Cyber Lab GitHub profile repository starter.

Run: python create_profile.py
Existing banner.svg and divider.svg files are preserved by default.
"""
from pathlib import Path

ROOT = Path("rajbhagure99-arch")

README = r"""<!-- Paste your finalized profile README.md here, or use the README.md
included alongside this script in the generated project folder. -->"""

BANNER = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="280" viewBox="0 0 1200 280"><rect width="1200" height="280" rx="18" fill="#070B10"/><path d="M0 32H1200M0 64H1200M0 96H1200M0 128H1200M0 160H1200M0 192H1200M0 224H1200M0 256H1200" stroke="#00E5FF" stroke-opacity=".12"/><text x="60" y="110" fill="#00E5FF" font-family="monospace" font-size="18">[ SYSTEM ONLINE ]</text><text x="60" y="165" fill="#E6EDF3" font-family="monospace" font-size="44" font-weight="bold">CYBER LAB</text><text x="60" y="205" fill="#00D084" font-family="monospace" font-size="17">SECURITY • CODE • CONTINUOUS LEARNING</text></svg>"""
DIVIDER = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="36" viewBox="0 0 1200 36"><path d="M0 18H450l18-10h90l18 10H1200" fill="none" stroke="#00E5FF" stroke-width="2"/><circle cx="600" cy="18" r="5" fill="#00D084"/></svg>"""

def write_if_missing(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        print(f"Preserved existing file: {path}")
        return
    path.write_text(content, encoding="utf-8")
    print(f"Created: {path}")

def main() -> None:
    ROOT.mkdir(exist_ok=True)
    # The complete README in this starter folder is the preferred source.
    source_readme = Path(__file__).with_name("README.md")
    if source_readme.exists():
        write_if_missing(ROOT / "README.md", source_readme.read_text(encoding="utf-8"))
    else:
        write_if_missing(ROOT / "README.md", "# RAJBHAGURE99-ARCH\n\nAdd your Cyber Lab profile README here.\n")
    write_if_missing(ROOT / "banner.svg", BANNER)
    write_if_missing(ROOT / "divider.svg", DIVIDER)
    write_if_missing(ROOT / "LICENSE", "MIT License\n\nCopyright (c) 2026 Raj Bhagure\n")
    write_if_missing(ROOT / ".github/workflows/snake.yml",
        Path(__file__).with_name(".github").joinpath("workflows", "snake.yml").read_text(encoding="utf-8")
        if Path(__file__).with_name(".github/workflows/snake.yml").exists()
        else "# Add the contribution snake workflow from the project template.\n")
    print(f"\nDone. Open {ROOT.resolve()} and review the README placeholders before pushing.")
    print("Do not commit secrets, access tokens, or private lab data.")

if __name__ == "__main__":
    main()

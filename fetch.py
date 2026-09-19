# /// script
# requires-python = ">=3.10"
# ///

from pathlib import Path
from urllib.request import Request, urlopen

HERE = Path(__file__).parent
DATA = HERE / "data"
FILE = "hk-jellyfish.zip"
URL = "https://ipt.taibif.tw/archive.do?r=hk-jellyfish&v=1.4"

OUTPUT = DATA / FILE


def main():
    DATA.mkdir(exist_ok=True)

    # Do not fetch again if the raw file already exists.
    if OUTPUT.exists():
        print(f"Already exists: {OUTPUT}")
        return

    request = Request(
        URL,
        headers={"User-Agent": "Mozilla/5.0"},
    )

    print("Fetching official dataset...")

    with urlopen(request) as response:
        raw = response.read()

    OUTPUT.write_bytes(raw)

    print(f"Saved raw file: {OUTPUT}")


if __name__ == "__main__":
    main()
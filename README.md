# newsimg20bot

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/ibrahimskertt/newsimg20bot/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/ibrahimskertt/newsimg20bot/reward.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

One image summing up the world news of Friday 20 November 2026: Russia's massive overnight missile and drone attack on Ukraine leads, with the UK-EU deal, Trump's AI data-centre threat, Anthropic's share slide and BepiColombo's arrival at Mercury as supporting stories. A Python program renders the poster and copies it to the output directory.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=accjskkr&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards</sub>

## Design & Palette
- **Canvas**: 1024x1024 pixels, PNG format (< 1 MiB).
- **Palette**: Deep ink navy background gradient (`#0B1220` to `#12233F`), gold accents (`#D4AF37`), paper white (`#F7F3E9`), ivory panel (`#F4EDDE`), ink text (`#14213D`), muted blue-grey text (`#C9D6F2`), and alert red accent (`#C0392B`).
- **Typography**: Clean, professional bold sans-serif hierarchy (DejaVu Sans / Bold) ensuring zero text overflow and absolute readability.

## Repository Structure
- `render_poster.py`: Pillow-based generator script that builds `entry.png` in the repository root.
- `entry.png`: The final 1024x1024 rendered poster image.
- `main.py`: Standard library Python 3.13 script that reads `entry.png` and copies it to `MAKEFUN_OUTPUT_DIR` (defaulting to `/output/entry.png`).
- `docs/research.md`: Verified research notes with sources.
- `README.md`: Entry documentation.
- `LICENSE`: MIT License.

## How to Build and Run

### 1. Build the Poster (requires Pillow)
```bash
python3 render_poster.py
```

### 2. Run Deployment Script
```bash
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License
Licensed under the MIT License (see `LICENSE` file).

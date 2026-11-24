# news-of-2026-11-23

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/hatyibei/news-of-2026-11-23/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/hatyibei/news-of-2026-11-23/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A drawn newspaper front page that sums up the world news of Monday 23 November 2026 in one 1024x1024 image: six stories, drawn with Pillow by draw.py and written out by main.py.

## Run it

```sh
python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=9zw8vvbd&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>

# The World in One Day — Monday 23 November 2026

An entry for make.fun's **"Sum up 23 November's world news in one image"**
bounty (`news-image-20261123`).

`main.py` writes one 1024×1024 PNG, `entry.png`, to the output directory.
The image is a drawn newspaper front page that sums up the world news of
Monday 23 November 2026 in six stories:

1. **Business / United States** — Jensen Huang returns as Nvidia's chief
   executive 11 days after resigning; Nvidia shares leap about 31%, the
   Nasdaq jumps 6.5% and the S&P 500 climbs 4.7%.
2. **War / Libya & Ukraine** — Zelenskyy says seven Ukrainian naval drones
   sank the Russian corvette Merkury in Benghazi port, Libya.
3. **Middle East / Iran** — Iran vows to use all its tools against the US
   naval blockade as Washington sanctions Iran's shadow-banking network;
   explosions are reported in the Strait of Hormuz.
4. **Climate / Türkiye** — COP31 ends without a new climate deal,
   deadlocked over fossil fuels and finance.
5. **Asia / Nepal & India** — Nepal's PM Balendra Shah ends his Delhi
   visit with eight pacts signed, the Ayodhya–Janakpur express launched
   and a $1.6bn Indian rebuild fund pledged.
6. **Americas / Mexico** — Mexican special forces capture Sinaloa cartel
   boss "El Chapo Isidro", an FBI most-wanted fugitive.

## Files

- `main.py` — the entry program (Python 3.13, standard library only).
  Copies the committed `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
  (default `/output/entry.png`), byte for byte, so repeated runs are
  identical.
- `entry.png` — the front page itself (1024×1024, under 1 MiB).
- `draw.py` — the Pillow script that drew `entry.png` from scratch
  (headlines, captions and simple icon illustrations; no photographs).

## License

MIT — see `LICENSE`.

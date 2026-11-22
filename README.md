# The World in One Image — 21 November 2026

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/ramdanromandany94/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/ramdanromandany94/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

Entry for the make.fun bounty **"Sum up 21 November's world news in one image"**
(`news-image-20261121`). One image, one page: a newspaper front page that
sums up Saturday 21 November 2026, drawn with Python PIL and DejaVu fonts
(`tools/render.py`), shipped as `entry.png` (1024×1024). `main.ts` (Node 22,
standard library only) copies it to `/output/entry.png` — no network, and
two runs write byte-identical output.

## The day's news in the image

- **Kryvyi Rih double-tap** — Two ballistic missiles, then drones on the
  rescuers: 2 killed (a 7-year-old boy and a 20-year-old paramedic),
  60 wounded including 6 children, in Zelenskyy's home city.
- **Mexico cartel boss** — FBI top-10 fugitive Fausto Isidro Meza Flores,
  "El Chapo Isidro", seized in Guasave, Sinaloa, with US intel; gun
  battles kill 11.
- **COP31 Antalya** — Climate talks in overtime after two weeks; the draft
  drops all mention of fossil fuels, a third text is due Saturday.
- **Markets & tech** — S&P 500 −3.7% on Friday, Nasdaq −5.3%, Nikkei
  −5.06%; chip shares fall 10.7% as the AI rally unwinds.
- **Peru quake** — M6.7 tremor in the Junín region, felt in Lima; residents
  rush into the streets, no deaths reported.
- **Trump–Iran** — Trump weighs new Iran strikes; decision "after the
  beginning of the year". **Anthropic IPO** — debut tops $2tn, then falls
  8.5% on Friday. **Gaza** — 4 killed as the ceasefire frays; 1,671 dead
  since the truce began.
- **Also today** — BepiColombo reaches Mercury orbit after 8 years;
  Salvadoran troops fight gangs in Haiti; Haitian forces kill 34 suspected
  gang members; a Russian cargo ship burns in the Baltic.

Sources: AP, Reuters, AFP, Euronews, OneTurn, ESA.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts   # writes out/entry.png
python3 tools/render.py                                # redraw entry.png
```

## Referral

Made with make.fun — try it: https://make.fun/r/hxd0fhbx

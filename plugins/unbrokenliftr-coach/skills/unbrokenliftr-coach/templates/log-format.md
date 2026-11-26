# Log format

One line per day. The user keeps these in a file or note and pastes them back for reviews. `scripts/calc.py` reads this format.

```
date,weight,kcal,protein,day_type,note
2026-11-13,167.4,2369,170.2,lifting,
2026-11-14,165.8,2676,183.6,lifting,
2026-11-15,167.2,2353.5,176.9,run,4 km Zone 2
```

- `weight`: morning weight in the user's unit (leave blank if missed).
- `kcal`, `protein`: the closed day's totals (leave blank if the day was not fully logged; do not guess).
- `day_type`: lifting, run, swim, rest, etc.
- `note`: anything that affects the scale (salty meal, travel, bad sleep).

Weekly measurements go in a separate block:

```
date,waist,chest,biceps,thigh,neck,hip
2026-11-16,32.25,40,13.5,20,14,
```

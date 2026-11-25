# Physique Coach

A Claude skill that coaches you from skinny-fat to muscular. It logs your food meal by meal, keeps a running count of calories and protein left for the day, judges your weight on 7-day averages instead of daily noise, tracks your weekly tape measurements, and tells you when to add or cut calories, using fixed rules instead of guesswork.

It's built from a real transformation: a nine-month cut from about 222 lb to about 163 lb, a reverse diet, and a lean bulk, all run in Claude chat.

**Status: v0.2, being tested.** The nutrition, tracking, phase sequence and training method are in. A few training details (sets for big muscle groups, the exact progression rule) are still marked "confirm".

## What it does
- **Food logging:** each entry gets an itemised table with kcal and protein, day totals, and calories and protein remaining against your target for that day type.
- **Weight trend:** 7-day averages and the weekly rate of change. It won't overreact to one high reading.
- **Measured maintenance:** works out your real maintenance calories from 14+ days of logs and morning weights, rather than a formula.
- **Rule-based adjustments** for cutting, recomp and lean bulking.
- **Weekly tape and Navy body-fat estimate.**
- **Safety rules:** calorie floors, a maximum rate of loss, and redirects for under-18s, disordered eating and medical conditions.

## Install

### Claude chat (claude.ai, desktop, mobile)
1. Download this repository as a zip (green **Code** button → **Download ZIP**) and unzip it.
2. Zip just the folder `plugins/physique-coach/skills/physique-coach`.
3. In Claude, open **Settings**, find the skills section, and upload that zip. Code execution needs to be switched on for the calculator to run. Skills availability depends on your Claude plan.
4. Start a chat and say: "Set me up as a new physique coaching client."

**Tip:** create a Claude **Project**, and save your completed profile (`templates/profile.md`) and your daily log there. The skill itself doesn't remember between chats. Your profile and log do.

### Claude Code
```
/plugin marketplace add <github-user>/<this-repo>
/plugin install physique-coach@physique-coach-marketplace
```

## Files
```
plugins/physique-coach/skills/physique-coach/
├── SKILL.md                 the coaching method
├── references/methods.md    weigh-in, tape, body fat, maintenance
├── references/training.md   training programme: splits, exercises, effort, progression
├── templates/profile.md     client profile to fill in
├── templates/log-format.md  daily log format
└── scripts/calc.py          Navy body fat, weekly trend, measured maintenance
```

## Disclaimer
This is coaching guidance, not medical advice. If you have a medical condition, are recovering from surgery, are pregnant, or are under 18, see a doctor before changing your diet or training.

# UnbrokenLiftr Coach

A Claude skill that coaches you from skinny-fat to muscular. It logs your food meal by meal, keeps a running count of calories and protein left for the day, judges your weight on 7-day averages instead of daily noise, tracks your weekly tape measurements, and tells you when to add or cut calories, using fixed rules instead of guesswork.

It's built by someone who did it the wrong way first. I started skinny-fat and spent over a decade stuck in the cycle: cut, feel too small, eat, feel fat, cut again. I never built muscle and ended up at 222 lb. Cutting down to 160 lb left me small with little muscle. This skill is the right way: recomp first, cut properly, never bulk past 16-17% body fat, and never switch phases because of how you look in the mirror on a given day.

**Status: v0.5, being tested.** Nutrition, tracking, phase sequence, body-fat limits, the skinny-fat trap rules and the training method are all in. Female body-fat targets are still defaults.

## What it does
- **Food logging:** each entry gets an itemised table with kcal and protein, day totals, and calories and protein remaining against your target for that day type.
- **Weight trend:** 7-day averages and the weekly rate of change. It won't overreact to one high reading.
- **Measured maintenance:** works out your real maintenance calories from 14+ days of logs and morning weights, rather than a formula.
- **Rule-based adjustments** for cutting, recomp and lean bulking.
- **Protection against the skinny-fat trap:** phases change only at scheduled reviews, based on tape, photos and lifts, never on a bad mirror day.
- **Weekly tape and Navy body-fat estimate.**
- **Safety rules:** calorie floors, a maximum rate of loss, and redirects for under-18s, disordered eating and medical conditions.

## Install

### Claude chat (claude.ai, desktop, mobile)
1. Download [`dist/unbrokenliftr-coach.zip`](dist/unbrokenliftr-coach.zip) (open it on GitHub, then click the download button).
2. Don't unzip it.
3. In Claude, open **Settings**, find the skills section, and upload that zip. Code execution needs to be switched on for the calculator to run. Skills availability depends on your Claude plan.
4. Start a chat and say: "Set me up as a new physique coaching client."

**Tip:** create a Claude **Project**, and save your completed profile (`templates/profile.md`) and your daily log there. The skill itself doesn't remember between chats. Your profile and log do.

### Claude Code
```
/plugin marketplace add mjanan1/Claude
/plugin install unbrokenliftr-coach@unbrokenliftr
```

## Files
```
plugins/unbrokenliftr-coach/skills/unbrokenliftr-coach/
├── SKILL.md                 the coaching method
├── references/methods.md    weigh-in, tape, body fat, maintenance
├── references/training.md   training programme: splits, exercises, effort, progression
├── templates/profile.md     client profile to fill in
├── templates/log-format.md  daily log format
└── scripts/calc.py          Navy body fat, waist targets, weekly trend, measured maintenance
```

## Disclaimer
This is coaching guidance, not medical advice. If you have a medical condition, are recovering from surgery, are pregnant, or are under 18, see a doctor before changing your diet or training.

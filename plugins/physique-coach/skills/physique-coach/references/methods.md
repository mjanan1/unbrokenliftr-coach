# Methods: weigh-ins, measurements, body fat and maintenance

## Morning weigh-in
1. Wake, pee.
2. Weigh before any water, coffee or food, in the same clothes (or none).
3. Then drink water and coffee.
Keep every reading. Tag unusual ones (travel, salty or late meal, bad sleep, no bowel movement) instead of deleting them.

## Weekly tape (same day each week, after the weigh-in)
Relaxed, end of a normal exhale, tape level and snug but not compressing. Take each measurement three times and average.
- Waist at the navel
- Chest at nipple line
- Right biceps, flexed
- Right mid-thigh, relaxed
- Neck, just below the Adam's apple
- Women: also hips at the widest point (needed for the Navy formula)
Same side, same flex, same time every week.

Realistic lean gains: arms about 0.25-0.5 in (0.6-1.3 cm) a month; chest and thighs about 0.5 in (1.3 cm) a month. Judge muscle gain monthly, not weekly.

## Navy body-fat estimate
Use `scripts/calc.py navy`. Formulas (inches):
- Men: BF% = 86.010 × log10(waist − neck) − 70.041 × log10(height) + 36.76
- Women: BF% = 163.205 × log10(waist + hip − neck) − 97.684 × log10(height) − 78.387
Error is about 3-4 points either way. For men, each 0.5 in on the waist moves it about 1 point. Use it for trend, not as truth. To turn a body-fat target into a tape target (e.g. "cut ends at 12%"), run `scripts/calc.py waist-for-bf`. A DEXA scan is only worth it if repeated on the same machine months later.

## Maintenance calories
**Measured (preferred):** 14+ days of honest logs and morning weights.
maintenance ≈ average daily intake − (change in 7-day average weight × 3,500 ÷ days)
Run `scripts/calc.py maintenance`.

**Formula estimate (until measured data exists):** Mifflin-St Jeor BMR × activity factor.
- Men: BMR = 10 × kg + 6.25 × cm − 5 × age + 5
- Women: BMR = 10 × kg + 6.25 × cm − 5 × age − 161
- Activity factor: 1.2 desk job, no training; 1.375 light (3 sessions a week or about 7,000 steps); 1.55 moderate (4-5 sessions or 10,000+ steps); 1.725 very active (physical job plus training).
Formulas can be off by 10-20%. After a long cut, real maintenance is often lower than the formula says.

## Logging accuracy leaks to watch
- Raw vs cooked meat weights (cooked meat has roughly 1.3-1.5× the calories per gram of raw).
- Takeaways (often ±250 kcal) and cheat meals (±500 kcal): log a conservative, higher estimate.
- Oils and sauces left off the log.
- Protein pushed late in the day: aim for a 40 g+ protein first meal.

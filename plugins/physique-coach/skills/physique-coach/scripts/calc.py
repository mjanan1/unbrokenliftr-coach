#!/usr/bin/env python3
"""Physique coach calculator. Standard library only.

Commands:
  navy --sex m --waist 32.25 --neck 14 --height 72 [--hip H] [--cm]
  waist-for-bf --sex m --bf 12 16 --neck 14 --height 72 [--hip H] [--cm]
                                waist measurement that corresponds to each body-fat target
  trend LOG.csv [--kg]          7-day averages and weekly rate of change
  maintenance LOG.csv [--days N] [--kg]
                                measured maintenance from intake and weight trend

LOG.csv columns: date,weight,kcal,protein,day_type,note (see templates/log-format.md).
Blank weight or kcal cells are skipped, never guessed.
"""
import argparse
import csv
import math
import sys
from datetime import date, timedelta

KCAL_PER_LB = 3500
KCAL_PER_KG = 7700


def navy(sex, waist, neck, height, hip=None, cm=False):
    if cm:
        waist, neck, height = waist / 2.54, neck / 2.54, height / 2.54
        hip = hip / 2.54 if hip else None
    if sex == "m":
        if waist <= neck:
            raise ValueError("waist must be larger than neck")
        return 86.010 * math.log10(waist - neck) - 70.041 * math.log10(height) + 36.76
    if hip is None:
        raise ValueError("women need --hip")
    return 163.205 * math.log10(waist + hip - neck) - 97.684 * math.log10(height) - 78.387


def waist_for_bf(sex, bf, neck, height, hip=None, cm=False):
    """Inverse Navy formula: the waist that gives `bf` percent, in the input unit."""
    k = 2.54 if cm else 1.0
    n, h = neck / k, height / k
    if sex == "m":
        w = 10 ** ((bf - 36.76 + 70.041 * math.log10(h)) / 86.010) + n
    else:
        if hip is None:
            raise ValueError("women need --hip")
        w = 10 ** ((bf + 78.387 + 97.684 * math.log10(h)) / 163.205) + n - hip / k
    return w * k


def _num(s):
    s = (s or "").strip()
    return float(s) if s else None


def read_log(path):
    rows = []
    with (sys.stdin if path == "-" else open(path, newline="")) as f:
        for r in csv.DictReader(f):
            if not (r.get("date") or "").strip():
                continue
            rows.append({
                "date": date.fromisoformat(r["date"].strip()),
                "weight": _num(r.get("weight")),
                "kcal": _num(r.get("kcal")),
                "protein": _num(r.get("protein")),
            })
    rows.sort(key=lambda r: r["date"])
    return rows


def rolling_avg(rows, end, days=7):
    start = end - timedelta(days=days - 1)
    w = [r["weight"] for r in rows if start <= r["date"] <= end and r["weight"] is not None]
    return (sum(w) / len(w), len(w)) if w else (None, 0)


def cmd_trend(rows, kg):
    unit = "kg" if kg else "lb"
    if not rows:
        print("No rows.")
        return
    end = rows[-1]["date"]
    print(f"Weekly 7-day averages ({unit}), newest last:")
    prev = None
    weeks = []
    d = end
    while d >= rows[0]["date"]:
        weeks.append(d)
        d -= timedelta(days=7)
    for wk in reversed(weeks):
        avg, n = rolling_avg(rows, wk)
        if avg is None:
            continue
        line = f"  week ending {wk}: {avg:.2f} ({n} readings)"
        if prev is not None:
            line += f"  change {avg - prev:+.2f}/week"
        if n < 4:
            line += "  [too few readings to trust]"
        print(line)
        prev = avg


def cmd_maintenance(rows, days, kg):
    end = rows[-1]["date"]
    start = end - timedelta(days=days - 1)
    window = [r for r in rows if start <= r["date"] <= end]
    kcals = [r["kcal"] for r in window if r["kcal"] is not None]
    first_avg, n1 = rolling_avg(rows, start + timedelta(days=6))
    last_avg, n2 = rolling_avg(rows, end)
    if len(kcals) < days * 0.8 or first_avg is None or last_avg is None or n1 < 4 or n2 < 4:
        print(f"Not enough data: {len(kcals)} logged days of {days}, "
              f"{n1} and {n2} weights in the first and last week. Need 80% of days logged and 4+ weights per week.")
        return
    span = (end - (start + timedelta(days=6))).days
    if span <= 0:
        print("Window too short; use --days 14 or more.")
        return
    per_unit = KCAL_PER_KG if kg else KCAL_PER_LB
    avg_kcal = sum(kcals) / len(kcals)
    change = last_avg - first_avg
    daily_balance = change * per_unit / span
    maint = avg_kcal - daily_balance
    unit = "kg" if kg else "lb"
    print(f"Window {start} to {end}: average intake {avg_kcal:.0f} kcal over {len(kcals)} logged days")
    print(f"7-day average moved {first_avg:.2f} -> {last_avg:.2f} {unit} ({change:+.2f} over {span} days)")
    print(f"Estimated maintenance: {maint:.0f} kcal (about +/-150; water and glycogen shifts distort short windows)")


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    n = sub.add_parser("navy")
    n.add_argument("--sex", choices=["m", "f"], required=True)
    n.add_argument("--waist", type=float, required=True)
    n.add_argument("--neck", type=float, required=True)
    n.add_argument("--height", type=float, required=True)
    n.add_argument("--hip", type=float)
    n.add_argument("--cm", action="store_true", help="inputs in cm (default inches)")
    w = sub.add_parser("waist-for-bf")
    w.add_argument("--sex", choices=["m", "f"], required=True)
    w.add_argument("--bf", type=float, nargs="+", required=True)
    w.add_argument("--neck", type=float, required=True)
    w.add_argument("--height", type=float, required=True)
    w.add_argument("--hip", type=float)
    w.add_argument("--cm", action="store_true")
    t = sub.add_parser("trend")
    t.add_argument("log")
    t.add_argument("--kg", action="store_true")
    m = sub.add_parser("maintenance")
    m.add_argument("log")
    m.add_argument("--days", type=int, default=14)
    m.add_argument("--kg", action="store_true")
    a = p.parse_args()

    if a.cmd == "navy":
        bf = navy(a.sex, a.waist, a.neck, a.height, a.hip, a.cm)
        print(f"Navy body fat: {bf:.1f}% (error about 3-4 points; use for trend only)")
    elif a.cmd == "waist-for-bf":
        unit = "cm" if a.cm else "in"
        for bf in a.bf:
            print(f"{bf:g}% body fat -> waist about {waist_for_bf(a.sex, bf, a.neck, a.height, a.hip, a.cm):.2f} {unit} "
                  f"(at neck {a.neck:g}{unit}; Navy estimate, use as a tape target)")
    elif a.cmd == "trend":
        cmd_trend(read_log(a.log), a.kg)
    else:
        rows = read_log(a.log)
        if not rows:
            print("No rows.")
            return
        cmd_maintenance(rows, a.days, a.kg)


if __name__ == "__main__":
    main()

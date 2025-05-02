from datetime import datetime, timedelta
import calendar


def last_included_weekday(allowed_days, reference_date=datetime.today()):
    return next(reference_date - timedelta(days=i) for i in range(7) if (reference_date - timedelta(days=i)).strftime("%A") in allowed_days) if allowed_days else None


def megasort(arr: list[int]) -> list[int]:
    """maximum efficiency sorting algorithm for list of ints with length 1-7 and no duplicates"""
    seen = [False] * 7
    for num in arr:
        seen[num] = True
    return [i for i, present in enumerate(seen) if present]


def sort_plan(plan: list):
    """sorts workout plan. supports list of strings length 1-7"""
    for idx, i in enumerate(plan):
        plan[idx] = list(calendar.day_name).index(i)
    plan: list = megasort(plan)
    for idx, i in enumerate(plan):
        plan[idx] = calendar.day_name[i]
    return plan

print(sort_plan(["Wednesday", "Monday", "Friday"]))
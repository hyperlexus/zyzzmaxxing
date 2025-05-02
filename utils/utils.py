from datetime import datetime, timedelta

conversion_dict = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
    }
reverse_conversion_dict = {v:k for k, v in conversion_dict.items()}

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
        plan[idx] = conversion_dict[i]
    plan: list = megasort(plan)
    for idx, i in enumerate(plan):
        plan[idx] = reverse_conversion_dict[i]
    return plan
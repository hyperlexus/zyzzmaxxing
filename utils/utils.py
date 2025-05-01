from datetime import datetime, timedelta

def last_included_weekday(allowed_days, reference_date=datetime.today()):
    return next(reference_date - timedelta(days=i) for i in range(7) if (reference_date - timedelta(days=i)).strftime("%A") in allowed_days) if allowed_days else None
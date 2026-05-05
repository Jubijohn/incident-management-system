from datetime import datetime, timedelta

recent_signals = {}

def should_create_incident(component: str):
    now = datetime.utcnow()

    if component in recent_signals:
        if now - recent_signals[component] < timedelta(seconds=10):
            return False

    recent_signals[component] = now
    return True
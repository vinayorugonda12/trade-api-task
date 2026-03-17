sessions = {}

def track_session(ip: str):
    if ip not in sessions:
        sessions[ip] = {"count": 0}
    sessions[ip]["count"] += 1
    return sessions[ip]

def create_dict(problemID, start_time, end_time, duration, solved, difficulty, tags, notes):
    result_dict = {
        "problemID": problemID,
        "start_time": start_time,
        "end_time": end_time,
        "duration": duration,
        "solved": solved,
        "difficulty": difficulty,
        "tags": tags,
        "notes": notes
    }
    return result_dict

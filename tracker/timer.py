import os
from rich import print
import json
from tracker import logger
from tracker import utils
from datetime import datetime

TIMER_TMP_FILE= ".lc_tmptimer.json"

def startTimer(problemID):
    if os.path.exists(TIMER_TMP_FILE):
        with open(TIMER_TMP_FILE, 'r') as f:
            data = json.load(f)
        print(f"[red]A timer is already running for the problem: {data['problemID']}[/red]")
        return
    data = {
        "problemID": problemID,
        "start_time": datetime.now().isoformat()
    }
    with open(TIMER_TMP_FILE, 'w') as f:
        json.dump(data,f,indent=4)
    print(f"[green]Timer has been started for {problemID} at {datetime.fromisoformat(data['start_time'])}[/green]")
    return

def endTimer(solved, difficulty, tags, notes):
    if not os.path.exists(TIMER_TMP_FILE):
        print(f"[red]There is no active timer running for any problem. Start a timer first before ending.[/red]")
        return
    with open(TIMER_TMP_FILE, 'r') as f:
        data = json.load(f)
    start_time = datetime.fromisoformat(data['start_time'])
    end_time = datetime.now()
    duration = end_time - start_time
    os.remove(TIMER_TMP_FILE)
    data_dict = utils.create_dict(data['problemID'], start_time.strftime("%H:%M:%S"), end_time.strftime("%H:%M:%S"), duration, solved, difficulty, tags, notes)
    logger.log_to_csv(data_dict)
    print(f"[yellow]Timer has been ended for {data['problemID']}, here are some stats,\nStart Time: {start_time.strftime("%H:%M:%S")}\nEnd Time: {end_time.strftime("%H:%M:%S")}\nDuration: {duration}[/yellow]")
    return
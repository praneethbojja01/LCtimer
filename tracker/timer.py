import os
from rich import print
import json
from datetime import datetime

TIMER_TEMP= ".lc_tmptimer.json"

def startTimer(problemID):
    if os.path.exists(TIMER_TEMP):
        with open(TIMER_TEMP, 'r') as f:
            data = json.load(f)
        print(f"[red]A timer is already running for the problem: {data['problemID']}[/red]")
        return
    data = {
        "problemID": problemID,
        "startTime": datetime.now().isoformat()
    }
    with open(TIMER_TEMP, 'w') as f:
        json.dump(data,f,indent=4)
    print(f"[green]Timer has been started for {problemID} at {datetime.fromisoformat(data['startTime'])}[/green]")
    return

def endTimer():
    if not os.path.exists(TIMER_TEMP):
        print(f"[red]There is no active timer running for any problem. Start a timer first before ending.[/red]")
        return
    with open(TIMER_TEMP, 'r') as f:
        data = json.load(f)
    startTime = datetime.fromisoformat(data['startTime'])
    endTime = datetime.now()
    duration = endTime - startTime
    os.remove(TIMER_TEMP)
    print(f"[yellow]Timer has been ended for {data['problemID']}, here are some stats,\nStart Time: {startTime}\nEnd Time: {endTime}\nDuration: {duration}[/yellow]")
    return
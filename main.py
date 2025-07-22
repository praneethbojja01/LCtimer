import typer
from tracker.timer import startTimer, endTimer

app = typer.Typer()

@app.command()
def start(id: str=typer.Option(..., "--id", "-id", help="problem ID and name for better tracking")):
    startTimer(id)

@app.command()
def end():
    endTimer()

if __name__=="__main__":
    app()

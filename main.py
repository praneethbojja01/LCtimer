import typer
from tracker.timer import startTimer, endTimer
from rich import print

app = typer.Typer()

@app.command()
def start(id: str=typer.Option(
    ...,
    "--id", "-i",
    help="problem ID and name for better tracking",
    prompt="Please add a problemID for this(LCID_Problem_name)")):

    #print(f"[green]Problem id received {id}[/green]")
    startTimer(id)

@app.command()
def end(solved: str=typer.Option(..., "--solved", "-s", help= "Was able to solve the question(?)", prompt="Please add this value, Solved(?)"),
        difficulty: str=typer.Option(..., "--difficulty", "-d", help= "difficulty level of the problem. Easy/Medium/Hard", prompt="Please add this value, Difficulty"),
        tags: str= typer.Option(..., "--tags", "-t", help= "tags related to the problem", prompt="Please add this value, tags"),
        notes: str= typer.Option(..., "--notes", "-n", help= "short notes to remember about the problem", prompt="Please add this value, Notes")):
    endTimer(solved, difficulty, tags, notes)

if __name__=="__main__":
    app()

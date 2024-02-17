import sys
import typer

from roco.main import generate_runtime_config
from roco.config import get_settings


app = typer.Typer()


@app.command()
def run(settings: bool = False):
    if settings:
        se = get_settings()
        click.echo(f"prefix = {se.Config.env_prefix}")
        click.echo(se.dict())
        sys.exit(0)

    output = generate_runtime_config()
    print(output)


if __name__ == "__main__":
    app()

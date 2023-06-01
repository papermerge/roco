import click

from roco.main import generate_runtime_config


@click.command()
def cli():
    output = generate_runtime_config()
    click.echo(output)


if __name__ == "__main__":
    cli()
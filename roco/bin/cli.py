import click

from roco.main import generate_runtime_config

@click.command()
@click.option(
    '-o',
    '--output-file',
    default='papermerge_runtime_config.js',
)
def cli(output_file: str):
    generate_runtime_config(
        output_file=output_file
    )


if __name__ == "__main__":
    cli()
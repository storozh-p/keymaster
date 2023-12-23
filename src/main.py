import click
from keymaster import KeyMaster


@click.group()
def cli():
    pass

@click.command()
def init_cmd():
    KeyMaster().init_root_dir()


if __name__ == "__main__":
    cli.add_command(init_cmd, "init")
    
    cli()

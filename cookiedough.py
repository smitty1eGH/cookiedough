import os
import subprocess
import click

@click.group()
def cli():
    pass

@click.command()
def dtls():
    '''Install devtools in ~/.local:
    * black
    * mypy
    * pytest
    * sphynx
    '''
    CMD="pip install --upgrade --user black mypy pytest sphinx"
    subprocess.run(CMD.split(),env=os.environ)

cli.add_command(dtls)

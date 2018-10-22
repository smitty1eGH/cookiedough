import os
import json
from pathlib import Path
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

@click.command()
def cc():
    '''Run the cookie cutter.
    '''
    #TODO: need to verify the directory doesn't exist and provide an override.
    ccj=None
    with open('cookiecutter.json','r') as f:
        ccj=json.loads(f.read())
    p = Path('/home/smitty/proj/%s' % ccj["project_slug"])
    if p.exists():
        print("need to blow this away if desired")
    else:
        print("building %s" % p)
        CMD="python -m venv %s" % p
        subprocess.run(CMD.split(),env=os.environ)
        os.chdir(p)
        CMD="cookiecutter /home/smitty/cookiedough/cookiedough"
        subprocess.run(CMD.split(),env=os.environ)


cli.add_command(dtls)
cli.add_command(cc)

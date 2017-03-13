import os
import click
import virtualenv
from scrim import get_scrim
scrim = get_scrim()


def get_activate_script(path, shell):
    '''Get virtualenv activate script from path'''

    activate_script = {
        'powershell.exe': os.path.join(path, 'Scripts', 'activate.ps1'),
        'cmd.exe': os.path.join(path, 'Scripts', 'activate.bat'),
    }.get(shell, None)

    if not activate_script:
        raise click.UsageError('Unable to find activate script for: ' + shell)

    if not os.path.exists(activate_script):
        raise click.UsageError(path + ' is not a valid virtualenv')

    return activate_script


@click.group()
def cli():
    '''Virtualenv Wrapper written in python using scrim'''


@cli.command()
@click.argument('path')
def create(path):
    '''Create virtualenv'''

    click.echo('Creating ' + path)
    virtualenv.create_environment(path)
    activate_script = get_activate_script(path, scrim.shell)
    click.echo('Activating ' + path)
    scrim.append(activate_script)


@cli.command()
@click.argument('path')
def activate(path):
    '''Activate virtualenv'''

    activate_script = get_activate_script(path, scrim.shell)
    click.echo('Activating ' + path)
    scrim.append(activate_script)


@cli.command()
def deactivate(path):
    '''Deactivate virtualenv'''

    click.echo('Deactivating')
    scrim.append('deactivate')


@cli.command()
@click.argument('path')
@click.argument('command')
def run_in(path, command):
    '''Run a command in a virtualenv'''

    virtual_env = os.environ.get('VIRTUAL_ENV', None)
    if virtualenv:
        old_activate_script = get_activate_script(virtual_env, scrim.shell)
    activate_script = get_activate_script(path, scrim.shell)
    if scrim.shell == 'cmd.exe':
        scrim.append('call ' + activate_script)
    else:
        scrim.append(activate_script)
    scrim.append(command)
    scrim.append('deactivate')

    if not os.path.samefile(old_activate_script, activate_script):
        scrim.append(old_activate_script)


if __name__ == '__main__':
    cli()

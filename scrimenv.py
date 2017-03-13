import os
import click
import virtualenv
from scrim import get_scrim
scrim = get_scrim()


def is_same_file(a, b):
    return os.stat(a) == os.stat(b)


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
    if scrim.shell is None:
        raise UsageError('CLI invoked through python, not Scrim Script...')


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
def deactivate():
    '''Deactivate virtualenv'''

    click.echo('Deactivating')
    scrim.append('deactivate')


@cli.command()
@click.argument('path')
@click.argument('command')
def run_in(path, command):
    '''Run a command in a virtualenv'''

    activate_script = get_activate_script(path, scrim.shell)
    active_env = os.environ.get('VIRTUAL_ENV', None)
    if active_env:
        old_activate_script = get_activate_script(active_env, scrim.shell)
        do_reactivate = not is_same_file(old_activate_script, activate_script)

    if scrim.shell == 'cmd.exe':
        call = 'call {}'

    elif scrim.shell == 'powershell.exe':
        call = 'Invoke-Expression "{}"'

    scrim.append(call.format(activate_script))
    scrim.append(command)
    scrim.append(call.format('deactivate'))
    if active_env and do_reactivate:
        scrim.append(call.format(old_activate_script))


if __name__ == '__main__':
    cli()

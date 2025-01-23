import json
from packaging.version import Version
from subprocess import Popen, PIPE
import sys
import os
import re
from pathlib import Path


OTTER_HOME = Path(os.environ['HOME']) / '.otter'
OTTER_PYTHON = str(OTTER_HOME / 'venv' / 'bin' / 'python3')
OTTER_PIP = str(OTTER_HOME / 'venv' / 'bin' / 'pip')


def run(command):
    print("  ~> Running:", ' '.join(command))
    process = Popen(' '.join(command), stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        yield line.decode('utf-8')


def get_installed_version():
    for path in (OTTER_HOME / 'venv' / 'lib').rglob('*/*'):
        if path.name.startswith('otter') and path.name.endswith('.dist-info'):
            version_match = re.match(r'otter-(.*)\.dist-info', path.name)
            version_string = version_match.groups()[0]
            return Version(version_string)


def get_latest_version():
    cmd = f"""curl --silent -L -H "Accept:application/vnd.github+json" -H "X-GitHub-Api-Version:2022-11-28" --output {OTTER_HOME / 'otter_version.json'} https://api.github.com/repos/tjwaterman99/otter/releases/latest""".split()
    for l in run(cmd):
        pass
    data = json.loads((OTTER_HOME / 'otter_version.json').read_text())
    return Version(data['tag_name'])


def needs_install():
    if not OTTER_HOME.exists():
        return True
    if not (OTTER_HOME / 'venv').exists():
        return True
    return False


def install():
    os.makedirs(OTTER_HOME, exist_ok=True)
    for l in run(['/usr/bin/python3', '-m', 'venv', str(OTTER_HOME / 'venv')]):
        print(l)
    version = get_latest_version()
    upgrade(version=version)


def upgrade(version):
    cmd = f"""curl --silent -L -H "Accept:application/vnd.github+json" -H "X-GitHub-Api-Version:2022-11-28" --output {OTTER_HOME / 'otter.zip'} https://api.github.com/repos/tjwaterman99/otter/zipball/v{version}""".split()
    for l in run(cmd):
        print(l)
    cmd = f"{OTTER_PIP} install {OTTER_HOME  / 'otter.zip'}".split()
    for l in run(cmd):
        print(l)


def start():
    cmd = f"{OTTER_PYTHON} -m otter".split()
    for l in run(cmd):
        print(l)


if __name__ == "__main__":
    print("Python version:", sys.version)
    print("Python executable:", sys.executable)

    if needs_install():
        print("Installing otter virtual environment at", OTTER_HOME)
        install()
    else:
        print("Found existing otter virtual environment at", OTTER_HOME)

    print("Checking latest version")
    latest_version = get_latest_version()
    current_version = get_installed_version()

    print("Current otter version:", current_version)
    print("Latest otter version", latest_version)

    if latest_version > current_version:
        print("Upgrading to version", latest_version)
        upgrade(latest_version)
    else:
        print("Already on the latest version", f"({current_version})")

    start()

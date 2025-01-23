from packaging.version import Version
import subprocess
import os
import sys
import re
from pathlib import Path


OTTER_HOME = Path(os.environ['HOME']) / '.otter'
OTTER_PYTHON = str(OTTER_HOME / 'venv' / 'bin' / 'python3')
OTTER_PIP = str(OTTER_HOME / 'venv' / 'bin' / 'pip')


def get_installed_version():
    for path in (OTTER_HOME / 'venv' / 'lib').rglob('*/*'):
        if path.name.startswith('otter') and path.name.endswith('.dist-info'):
            version_match = re.match(r'otter-(.*)\.dist-info', path.name)
            version_string = version_match.groups()[0]
            print("Found installed version", version_string)
            return Version(version_string)


def needs_install():
    if not OTTER_HOME.exists():
        return True
    if not (OTTER_HOME / 'venv').exists():
        return True
    return False


def install():
    os.makedirs(OTTER_HOME, exist_ok=True)
    subprocess.run(['/usr/local/bin/python3', '-m', 'venv', str(OTTER_HOME / 'venv')], stdout=sys.stdout, stderr=sys.stderr)


if __name__ == "__main__":
    if needs_install():
        print("Installing otter virtual environment at", OTTER_HOME)
        install()
    else:
        print("Found existing installation at", OTTER_HOME)

    print(get_installed_version())

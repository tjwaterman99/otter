echo "Upgrading pip..."
/usr/bin/python3 -m pip install --upgrade pip
/usr/bin/python3 -m pip install packaging
curl --silent https://raw.githubusercontent.com/tjwaterman99/otter/refs/heads/main/start.py | /usr/bin/python3

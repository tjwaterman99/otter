if [ ! -f /usr/local/bin/python3 ];
then
    echo "No python version installed!"
    echo "You must download and install Python"
    echo "https://www.python.org/downloads/"
    exit 1
fi

echo "Upgrading pip..."
/usr/local/bin/python3 -m pip install --upgrade pip
curl --silent https://raw.githubusercontent.com/tjwaterman99/otter/refs/heads/main/start.py | /usr/local/bin/python3

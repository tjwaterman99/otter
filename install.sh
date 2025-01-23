if [ ! -f /usr/local/bin/python3.12 ];
then
    echo "No python version installed!"
    echo "You must download and install Python 3.12"
    echo "Paste the following link into your web browser to start the download"
    echo "https://www.python.org/ftp/python/3.12.8/python-3.12.8-macos11.pkg"
    exit 1
fi

echo "Upgrading pip..."
/usr/local/bin/python3.12 -m pip install --upgrade pip
curl --silent https://raw.githubusercontent.com/tjwaterman99/otter/refs/heads/main/start.py | /usr/local/bin/python3.12

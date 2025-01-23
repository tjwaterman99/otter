from time import sleep
from otter import app
from uvicorn import run
from threading import Thread
import webbrowser


def start():
    run(app=app.app)


Thread(target=start, daemon=True).start()

print("Waiting 3 seconds for webserver to start...")
sleep(3)

print("Opening app")
webbrowser.open(url="http://127.0.0.1:8000")

while True:
    pass

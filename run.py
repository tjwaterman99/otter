print("Starting app. This usually takes about 30 seconds. Please hold.")

from app import app
from uvicorn import run
from threading import Thread
import webbrowser


def start():
    run(app=app.app)


Thread(target=start, daemon=True).start()
webbrowser.open(url="http://127.0.0.1:8000")

while True:
    pass

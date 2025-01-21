from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from otter.models import Gradebook


app = FastAPI()


@app.route('/')
def root(request):
    return HTMLResponse("Hello, world")

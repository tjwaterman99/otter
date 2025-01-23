from typing import Optional
from fastapi import FastAPI, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from otter.models import Gradebook
from otter import config


app = FastAPI()
app.mount("/static", StaticFiles(directory=config.static_files_directory), name="static")
templates = Jinja2Templates(directory=config.templates_path)


@app.get('/')
async def index_get(request: Request, file_upload: Optional[str]=None):
    return templates.TemplateResponse(request=request, name='index.html', context={'file_upload': file_upload})


@app.post('/')
async def index_post(request: Request, file_upload: UploadFile):
    raw = await file_upload.read()
    gb = Gradebook(original_path=file_upload.filename, workbook_bytes=raw)
    return {'filename': gb.original_path, 'sheets': gb.workbook.sheetnames}

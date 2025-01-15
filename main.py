from pathlib import Path

from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
import web.explorer
import web.creature
import web.user
from fake.creature import _creatures as fake_creature
from fake.explorer import _explorers as fake_explorer
import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()
top = Path(__file__).resolve().parent
template_obj = Jinja2Templates(directory=f"{top}/template")
app.include_router(web.explorer.router)
app.include_router(web.creature.router)
app.include_router(web.user.router)


@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")

@app.get("/list")
def explorer_list(request: Request):
    return template_obj.TemplateResponse("list.html",
        {"request": request,
         "explorers": fake_explorer,
         "creatures": fake_creature}
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload = True)
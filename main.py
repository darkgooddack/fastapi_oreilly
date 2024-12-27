from fastapi import FastAPI
from starlette.responses import RedirectResponse

import web.explorer
import web.creature

app = FastAPI()

app.include_router(web.explorer.router)
app.include_router(web.creature.router)


@app.get("/")
def redirect_to_docs():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload = True)
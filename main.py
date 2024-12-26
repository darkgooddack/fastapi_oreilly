from fastapi import FastAPI
import web.explorer
import web.creature

import asyncio
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

app = FastAPI()

app.include_router(web.explorer.router)
app.include_router(web.creature.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload = True)
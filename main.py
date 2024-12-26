from fastapi import FastAPI
import web.explorer
import web.creature

app = FastAPI()

app.include_router(web.explorer.router)
app.include_router(web.creature.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload = True)
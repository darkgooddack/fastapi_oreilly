import os
from fastapi import APIRouter
from model.creature import Creature
import fake.creature as service

from fastapi import Response
import plotly.express as px

if os.getenv("CRYPTIC_UNIT_TEST"):
    from fake import creature as service
else:
    from service import creature as service


router = APIRouter(
    prefix="/creature",
    tags=["Creature"],
)

@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()

@router.get("/{name}")
def get_one (name) -> Creature:
    return service.get_one(name)

@router.get("/test")
def test():
    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    fig_bytes = fig.to_image(format="png")
    return Response(content=fig_bytes, media_type="image/png")

# все остальные конечные точки пока ничего не делают:

@router.post("/")
def create(creature: Creature) -> Creature:
    return service.create(creature)

@router.patch("/")
def modify(creature: Creature) -> Creature:
    return service.modify(creature)

@router.put("/")
def replace(creature: Creature) -> Creature:
    return service.replace(creature)

@router.delete("/{name}")
def delete(name: str):
    return service.delete(name)
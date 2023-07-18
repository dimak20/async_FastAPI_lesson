from fastapi import FastAPI

from cheese import router as cheese_router

app = FastAPI()

app.include_router(cheese_router.router)


@app.get("/")
def root() -> dict:
    return {"message": "Hello World"}

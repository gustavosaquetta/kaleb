from fastapi import FastAPI

from app.server.routes.user import router as userRouter
from app.server.routes.auth import router as authRouter


app = FastAPI()

app.include_router(authRouter, tags=["auth"], prefix="/auth")
app.include_router(userRouter, tags=["user"], prefix="/user")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Katalogos! The stack are online..."}

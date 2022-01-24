from fastapi import FastAPI

from app.server.routes.user import router as userRouter
from app.server.routes.auth import router as authRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(authRouter, tags=["auth"], prefix="/auth")
app.include_router(userRouter, tags=["user"], prefix="/user")

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to Katalogos! The stack are online..."}

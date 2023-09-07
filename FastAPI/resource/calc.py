from fastapi import APIRouter
from fastapi import Depends

from typing import Any
from time import sleep

def fake_db():
    try:
        print("Criando conexão com o banco...")
        sleep(1)
    finally:
        print("Fechando conexão com o banco...")
        sleep(1)

class Calc:
    router = APIRouter()

    @router.get('/calc')
    async def calc(a:int, b:int, c:int, db: Any = Depends(fake_db)):

        return {"resultado": a+b+c}

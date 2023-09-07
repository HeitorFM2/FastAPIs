from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi import Depends

from time import sleep
from models import Model
from typing import Any


cursos = {
        1: {
            "titulo": "birulaibe",
            "aulas": 112,
            "horas": 52
        },
        2: {
            "titulo": "asd",
            "aulas": 112,
            "horas": 52
        }
    }


def fake_db():
    try:
        print("Criando conexão com o banco...")
        sleep(1)
    finally:
        print("Fechando conexão com o banco...")
        sleep(1)

class Teste:
    router = APIRouter()


    @router.get('/teste')
    async def get_cursos(db : Any = Depends(fake_db)):
        return cursos

    @router.get('/teste/{testado}')
    async def get_curso(testado: int, db : Any = Depends(fake_db)):
        try:
            curso = cursos[testado]
            return curso
        except KeyError:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="AA")
        
    @router.post('/teste')
    async def post_curso(teste: Model, db : Any = Depends(fake_db)):
        next_id: int = len(cursos) + 1
        cursos[next_id] = teste
        del teste.id
        return teste

    @router.put('/teste/{curso_id}')
    async def put_curso(curso_id: int, teste: Model, db : Any = Depends(fake_db)):
        if curso_id in cursos:
            cursos[curso_id] = teste
            del teste.id
            return teste
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nao achou")
        
    @router.delete('/teste/{curso_id}')
    async def del_curso(curso_id: int, db : Any = Depends(fake_db)):
        if curso_id in cursos:
            del cursos[curso_id]
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Nao achou")
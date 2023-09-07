from fastapi import FastAPI
from resource.teste import Teste
from resource.calc import Calc

app = FastAPI()
app.include_router(Teste.router, tags=['Teste'])
app.include_router(Calc.router, tags=['Calc'])

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
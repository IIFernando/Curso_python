from fastapi import FastAPI

app = FastAPI(title="API de Teste com Swagger")

@app.get("/")
def read_root():
    return {"mensagem": "Bem-vindo à API!"}

@app.get("/api/hello")
def say_hello():
    return {"mensagem": "Olá do endpoint /api/hello"}

@app.post("/api/somar")
def somar(a: int, b: int):
    return {"resultado": a + b}

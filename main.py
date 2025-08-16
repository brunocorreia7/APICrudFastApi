from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crud import get_all_users, get_user_by_id, create_user, update_user, delete_user

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

@app.get("/")
def root():
    return {"message": "API de Cadastro de Usuários"}

@app.get("/users")
def read_users():
    return get_all_users()

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user = get_user_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuária não encontrada")
    return user

@app.post("/users")
def add_user(user: User):
    create_user(user.name, user.email)
    return {"message": "Usuária criada com sucesso"}

@app.put("/users/{user_id}")
def edit_user(user_id: int, user: User):
    update_user(user_id, user.name, user.email)
    return {"message": "Usuária atualizada com sucesso"}

@app.delete("/users/{user_id}")
def remove_user(user_id: int):
    delete_user(user_id)
    return {"message": "Usuária removida com sucesso"}

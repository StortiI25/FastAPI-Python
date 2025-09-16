from fastapi import APIRouter, HTTPException ,Depends
from models import Usuario
from dependecies import pegar_sessao
from main import bcrypt_context
from schemas import Usuarioschema

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    '''
    Essa é a rota padrão de autentificação do sistema.
    '''
    return{"mensagem": "Você acessou a rota padrão de autentificação"}

@auth_router.post("/criar_usuario")
async def criar_usuario(usuario_schemas: Usuarioschema, session =  Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schemas.email).first()
    if usuario:
        return HTTPException(status_code=400, detail="E-mail já cadastrado")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schemas.senha)
        novo_usuario = Usuario(usuario_schemas.nome, senha_criptografada, usuario_schemas.email)
        session.add(novo_usuario)
        session.commit()
        return {"Mensagem": f"Usúario cadastrado com sucesso {usuario_schemas.email}"}



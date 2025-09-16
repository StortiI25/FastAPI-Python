from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependecies import pegar_sessao
from schemas import Pedido_schema
from models import Pedido

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def pedidos():
    '''
    Essa é a rota padrão de pedidos do sistema. Todas as rotas dos pedidos precisam ser autentificação
    '''
    return {"mensagem": "Você acessou a rota de pedidos"} 

@order_router.post("/pedido")
async def criar_pedido(pedidoschema: Pedido_schema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usario=pedidoschema.usuario)
    session.add(novo_pedido)
    session.commit()
    return {"Mensagem": f"Pedido criado com sucesso. ID do pedido {novo_pedido.id}"}
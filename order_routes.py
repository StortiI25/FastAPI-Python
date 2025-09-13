from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.get("/")
async def pedidos():
    '''
    Essa é a rota padrão de pedidos do sistema. Todas as rotas dos pedidos precisam ser autentificação
    '''
    return {"mensagem": "Você acessou a rota de pedidos"} 

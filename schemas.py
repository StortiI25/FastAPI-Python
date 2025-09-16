from pydantic import BaseModel
from typing import Optional

class Usuarioschema(BaseModel):
    nome: str
    email: str
    senha: str
    ativo: Optional[bool]
    admin: Optional[bool]

    class Config:
        from_attributes = True
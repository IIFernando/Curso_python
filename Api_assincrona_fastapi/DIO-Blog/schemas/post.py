#Classe para definir o modelo do body da API
from datetime import UTC, datetime

from pydantic import BaseModel

class PostIn (BaseModel):
    title: str
    date: datetime = datetime.now(UTC)
    published: bool = False
    author: str
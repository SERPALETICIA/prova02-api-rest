from datetime import datetime
from typing import List

from sqlmodel import Field, Relationship, SQLModel


class Voo(SQLModel, table=True):
    __tablename__ = "voos"
    id: int = Field(default=None, primary_key=True)
    data_saida: datetime
    nome_piloto: str
    nome_copiloto: str
    poltrona_1: str = Field(default=None)
    poltrona_2: str = Field(default=None)
    poltrona_3: str = Field(default=None)
    poltrona_4: str = Field(default=None)
    poltrona_5: str = Field(default=None)
    poltrona_6: str = Field(default=None)
    poltrona_7: str = Field(default=None)
    poltrona_8: str = Field(default=None)
    poltrona_9: str = Field(default=None)
    reservas: List["reservas"] = Relationship(back_populates="voos")

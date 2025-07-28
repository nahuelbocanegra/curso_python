from sqlalchemy.orm import Mapped,mapped_column 
from sqlalchemy import String
from db import db


class Frases(db.Model):

    id:Mapped[int]=mapped_column(primary_key=True)
    autor:Mapped[str]=mapped_column(String(100))
    frase:Mapped[str]=mapped_column(String(500))
    

    def __str__(self):
        return f"{self.id} {self.autor} {self.frase}"


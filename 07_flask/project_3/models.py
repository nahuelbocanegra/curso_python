from database import db
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String

class Mensaje(db.Model):
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    titulo:Mapped[str]=mapped_column(String(100))
    mensaje:Mapped[str]=mapped_column(String(400))

    def __str__(self):
        return f"""
            id:{self.id}
            titulo:{self.titulo}
            mensaje:{self.mensaje}
        """
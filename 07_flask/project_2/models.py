from app import db
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String



#modelo de datos
class Cursos(db.Model):
    id: Mapped[int]=mapped_column(String(100),primary_key=True)
    nombre:Mapped[str]=mapped_column(String(100),unique=True)
    instructor:Mapped[str]=mapped_column(String(100))
    topico:Mapped[str]=mapped_column(String(100))

    def __str__(self):
        return f"""
            id:{self.id}
            nombre:{self.nombre}
            instructor:{self.instructor}
            topico:{self.topico}
        """
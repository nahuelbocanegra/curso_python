
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String

class Contacto():
    id:Mapped[int]=mapped_column(primary_key=True)
    nombre:Mapped[str]=mapped_column(String(100))
    telefono:Mapped[str]=mapped_column(String(100))
    email:Mapped[str]=mapped_column(String(100))
    direccion:Mapped[str]=mapped_column(String(100))
    comentario:Mapped[str]=mapped_column(String(100))
    
    def __str__(self):
        return f"""
            nombre:{self.nombre}
            telefono:{self.direccion}
            email:{self.email}
        """
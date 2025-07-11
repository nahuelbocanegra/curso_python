import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1997',
    database='demo',
)

cursor=conn.cursor()
# cursor.execute(
#     """
#         CREATE TABLE cursos(
#         curso_id INT AUTO_INCREMENT PRIMARY KEY,
#         cursor_name VARCHAR(50) UNIQUE NOT NULL,
#         curso_instructor VARCHAR(100) NOT NULL,
#         curso_topico VARCHAR(20) NOT NULL);
#     """
# )
# cursor.execute("""
#         INSERT INTO cursos(cursor_name,curso_instructor,curso_topico)
#         VALUES('introducion a sql','nahuel','SQL')""")
# cursor.execute("""
#         INSERT INTO cursos(cursor_name,curso_instructor,curso_topico)
#         VALUES('introducion a python','juan','PYTHON')""")

cursor.execute("SELECT * FROM cursos")
filas= cursor.fetchall()

for fila in filas:
    print(fila)


conn.commit()
cursor.close()
conn.close()
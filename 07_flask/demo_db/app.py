import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1997',
    database='demo',
)

cursor=conn.cursor()
cursor.execute(
    """
        CREATE TABLE cursos(
        curso_id INT AUTO_INCREMENT PRIMARY KEY,
        cursor_name VARCHAR(50) UNIQUE NOT NULL,
        curso_instructor VARCHAR(100) NOT NULL,
        curso_topico VARCHAR(20) NOT NULL);
    """
)

conn.commit()
cursor.close()
conn.close()
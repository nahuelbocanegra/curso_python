import mysql.connector
from variables_entorno import USER,USER_HOST,USER_PASSWORD,DATABASE


con= mysql.connector.connect(
    host=USER_HOST,
    user=USER,
    password=USER_PASSWORD,
    database=DATABASE
)


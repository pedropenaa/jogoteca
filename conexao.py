import mysql.connector
from mysql.connector import errorcode



print("Conectando...")



try:
    conn = mysql.connector.connect(

        host = 'localhost',
        user = 'root',
        password ='root'

)
    print( "CONECTADO COM SUCESSO !!!" )


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Existe algo errado no nome de usuario ou na senha")
    else:
        print(err)




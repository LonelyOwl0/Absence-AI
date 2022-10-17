import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host='localhost',
                                         database='absence',
                                         user='root',
                                         password='')




test = """ INSERT INTO absence 
    SELECT 'Fouad', 'Mohammed', '17/10/2022','10h -> 12'
        FROM dual
        WHERE NOT EXISTS (SELECT * FROM absence
                             WHERE  
                               Nom='Fouad' and Prenom='Mohammed' and Date = '17/10/2022')"""

newtest = """INSERT INTO absence 
SELECT 'fouad' as instance, 'mohammed' as prenom, '17/10/2022' as item
FROM absence
WHERE (nom='fouad' and prenom='mohammed' and date ='17/10/2022')
HAVING COUNT(*) = 0;"""

cursor = connection.cursor()
cursor.execute(newtest)
connection.commit()
print(cursor.rowcount, "Record inserted successfully into Laptop table")
cursor.close()

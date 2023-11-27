import sqlite3 as sql 

DATABASE = "./database/DataProteus.db"

def createTable():
    con = sql.connect(DATABASE)
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE Datos(
            Dato_ID INTEGER PRIMARY KEY,
            tem1 float,
            hum1 float,
            tem2 float,
            hum2 float,
            tem3 float,
            hum3 float,
            temlm float
        )
        """
    )
    con.commit()
    con.close()
    
def dropTable():
    con = sql.connect(DATABASE)
    cursor = con.cursor()
    cursor.execute("DROP TABLE Datos")
    con.commit()
    con.close()
    
def insertData(num,DHT1,HUM1,DHT2,HUM2,DHT3,HUM3,LM75):
    con = sql.connect(DATABASE)
    cursor = con.cursor()
    try:
        cursor.execute("INSERT INTO Datos VALUES (?,?,?,?,?,?,?,?)",
                       (num,DHT1,HUM1,DHT2,HUM2,DHT3,HUM3,LM75))
        con.commit()
        print("Se enviaron los datos de manera exitosa")
    except Exception as e:
        print(f"Error al insertar los registros {e}")

def get_sensor():
    con = sql.connect(DATABASE)
    cursor = con.cursor()
    query = "SELECT tem1, hum1, tem2, hum2, tem3, hum3, temlm FROM Datos"
    cursor.execute(query)
    return cursor.fetchall()

def updateData(num, DHT1, HUM1, DHT2, HUM2, DHT3, HUM3, LM75):
    con = sql.connect(DATABASE)
    cursor = con.cursor()
    try:
        cursor.execute("""
            UPDATE Datos 
            SET tem1=?, hum1=?, tem2=?, hum2=?, tem3=?, hum3=?, temlm=? 
            WHERE Dato_ID=?
        """, (DHT1, HUM1, DHT2, HUM2, DHT3, HUM3, LM75, num))
        con.commit()
        print("Se actualizaron los datos de manera exitosa")
    except Exception as e:
        print(f"Error al actualizar los registros {e}")
    finally:
        con.close()
def readData():
    con = sql.connect(DATABASE)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Datos")
    datos = cursor.fetchall()
    print(datos)
    con.commit()
    con.close()
    
def cleanData():
    con = sql.connect(DATABASE)
    cursor = con.cursor()
    try:
        cursor.execute("DELETE FROM Datos")
        con.commit()
        print("se borraron los registros")
    except Exception as e:
        print(f"Error {e}")
    con.close()
    
        
#Funcion para saber si hay registros
def hasRecords():
    con = sql.connect(DATABASE)
    cursor = con.cursor()
    cursor.execute("SELECT COUNT(*) FROM Datos")
    count = cursor.fetchone()[0]
    con.close()
    return count > 0
    
if __name__ == "__main__":
    createTable()
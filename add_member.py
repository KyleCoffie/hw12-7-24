from connect_mysql import connect_database

def add_member(id, name, age):
    query = "INSERT INTO Members(id, name, age)VALUES (%s,%s,%s)"
    cursor.execute(query, (id,name,age))
    
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        add_member(4,"Jennifer Coffie", 39)
        
        conn.commit()
        print("New member added successfully. ")
        
    except Exception as e:
        print(f"Error {e}")
    finally:
        cursor.close()
        conn.close()
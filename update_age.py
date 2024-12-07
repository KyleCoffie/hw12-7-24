from connect_mysql import connect_database


def update_member_age(new_age,member_id):
    query = "UPDATE members SET age = %s WHERE id = %s"
    cursor.execute(query, (new_age,member_id))

conn= connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        update_member_age(41,1)
        
        
        conn.commit()
        print("Customer details updated successfully.")
        
    finally:
        cursor.close()
        conn.close()
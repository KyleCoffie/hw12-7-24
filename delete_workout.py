from connect_mysql import connect_database

# This function will delete which ever session id when called
def delete_workout_session(session_id):
    query = "DELETE from workoutsessions WHERE session_id = %s "
    cursor.execute(query, (session_id,))
    #When only passing one parameter,you must include a coma so reads it as a tuple.
    

conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        delete_workout_session(2)
        #This is where the session you want to delete will be entered
        
        conn.commit()
        print("Workoutsession deleted successfully.")
        
        
    except Exception as e:
        print(f"Error {e}")
    finally:
        cursor.close()
        conn.close()
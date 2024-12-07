from connect_mysql import connect_database

def add_workout_session(members_id, date, duration_minutes, calories_burned):
    query = "INSERT INTO workoutsessions(members_id, date, duration_minutes, calories_burned)VALUES (%s,%s,%s,%s)"
    cursor.execute(query, (members_id, date, duration_minutes, calories_burned))
    
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        
        add_workout_session(4,"2024-10-10", 30, 150)
        add_workout_session(3,"2024-10-11", 60, 350)
        add_workout_session(2,"2024-10-01", 30, 150)
        add_workout_session(1,"2024-11-10", 60, 250)
        
        conn.commit()
        print("New workout sessions added successfully. ")
        
    except Exception as e:
        print(f"Error {e}")
    finally:
        cursor.close()
        conn.close()
from mysql.connector.errors import InternalError
from connect_mysql import connect_database

def get_members_in_age_range(cursor,start_age, end_age):
    #passing cursor as a parameter so that it can becalled inside of the function.
    query = "SELECT id, name, age FROM members WHERE age BETWEEN %s AND %s"
    #query is a variablethat istelling the database to select the id, name, aeg from the 
    # members column where the ages are between 25 and 30
    cursor.execute(query,(start_age,end_age))
    #this is tell the cursor to execute the query
conn = connect_database()
if conn is not None:
    try:
        cursor = conn.cursor()
        #cursor is created to allow the manipulation of the db
        
        #created variables so that I can use them in my print statement as well
        start_age = 25
        end_age = 30
        get_members_in_age_range(cursor,start_age,end_age) 
        
            
        print(f"Members listed between {start_age} and {end_age}:")
    # telling the cursor to loop thru all members and fetch all members that fall between 25 - 30
        for member in cursor.fetchall():
            print(member)
    except InternalError as f:
        print (f"There was an error inside mysql {f}") 
           
    except Exception as e:
        print(f"Error {e}")
    
    finally:
        cursor.close()
        conn.close()
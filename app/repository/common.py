import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from app.core.database import url_object as db_credential

class CommonDto:
    def __init__(self, value, label):
        self.value = value
        self.label = label

def get_dropdown_common_dto(function_name):
    try:
        # Establish a database connection                
        conn = psycopg2.connect(dbname='drugdbdev', host='localhost', port=5433, user='postgres', password='1234')
        print(db_credential)
        #conn = psycopg2.connect(db_credential)
        

        # Begin a transaction
        conn.autocommit = False
        cur = conn.cursor()
        
        # Execute the function and retrieve the cursor
        result1_cursor_name = "ref1"
        cur.execute(f"SELECT * FROM {function_name}()")
        cur.execute(f"FETCH ALL IN \"{result1_cursor_name}\"")
        
        # Fetch all results from the cursor
        result_list1 = []
        rows = cur.fetchall()
        
        # Process each row and create CommonDto objects
        for row in rows:
            value = row[0] if row[0] is not None else 0
            label = row[1] if row[1] is not None else ""
            result_list1.append(CommonDto(value, label))
        
        # Commit the transaction
        conn.commit()
        
        # Close the cursor and connection
        cur.close()
        conn.close()
        
        return result_list1
    
    except Exception as ex:
        print(f"An error occurred: {ex}")
        if conn:
            conn.rollback()
        raise


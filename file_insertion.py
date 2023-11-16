from database import generate_path

def file_insertion(connection, number): 
    cur = connection.cursor()
    
    for _ in range(number):
        
        cur.execute(
            f"INSERT INTO file (file_path) "
            f"VALUES ('{generate_path()}')"
        )


    connection.commit()
    print("Files were added successfully!")
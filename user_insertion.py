from database import generate_password, generate_login, generate_mail, generate_personality


def user_insertion(connection, number):
    table_name = "User"
    cur = connection.cursor()
    
    for _ in range(number):
        login = generate_login()
        password = generate_password()
        mail = generate_mail()
        personality = generate_personality()
        
        cur.execute(
            f"INSERT INTO \"{table_name}\" (login, password, mail, personality) "
            f"VALUES (\'{login}\', \'{password}\', \'{mail}\', \'{personality}\')"
        )
        
        

    connection.commit()
    print("Users were added successfully!")
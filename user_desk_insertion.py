def user_desk_insertion(connection, number_desks): # number_workplaces - количество worklaces, привязанные к user'у
    cur = connection.cursor()   # копируем записи из desk
    
    cur.execute(
        f"SELECT desk_id, admin_id FROM Desk;"
    )
    all_desks = list(cur.fetchall())
    
    for desk_id, admin_id in all_desks:
        cur.execute(
            f"INSERT INTO User_Desk (user_id, desk_id) "
            f"VALUES ({admin_id}, {desk_id})"
        )

    connection.commit()
    print("User_desks were added successfully!")
def user_desk_insertion(connection):
    cur = connection.cursor() 
    
    cur.execute(
        f"SELECT desk_id, admin_id, work_place_id FROM Desk;"
    )
    all_desks_admins_workplaces = list(cur.fetchall())
    
    
    cur.execute(
        f"SELECT user_id, work_place_id FROM User_work_place;"
    )
    all_users_workplaces = list(cur.fetchall())
    
    for desk_id, admin_id, workplace_id1 in all_desks_admins_workplaces:
        cur.execute(
            f"INSERT INTO User_Desk (user_id, desk_id) "
            f"VALUES ({admin_id}, {desk_id})"
        )
        for user_id, workplace_id2 in all_users_workplaces:
            if workplace_id1 == workplace_id2:
                 cur.execute(
                    f"INSERT INTO User_Desk (user_id, desk_id) "
                    f"VALUES ({user_id}, {desk_id})"
                )

    connection.commit()
    print("User_desks were added successfully!")
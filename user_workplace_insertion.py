import random


def user_workplace_insertion(connection, number_workplaces): # number_workplaces - количество worklaces, привязанные к user'у
    cur = connection.cursor()
    
    cur.execute(
        f"SELECT admin_id FROM Work_place "
        f"ORDER BY admin_id"
    )
    all_admins = list(map(lambda item: item[0], cur.fetchall()))
    
    cur.execute(
        f"SELECT work_place_id FROM Work_place "
        f"ORDER BY admin_id"
    )
    all_workplaces = list(map(lambda item: item[0], cur.fetchall()))
    
    count_workplaces = 0 # для того,чтобы каждый user, который admin workplace'а, был привязан к этой workplace
    for user_id in all_admins:
        available_user_workplaces = set(all_workplaces)
        cur.execute(
            f"INSERT INTO User_Work_place (user_id, work_place_id) "
            f"VALUES ({user_id}, {all_workplaces[count_workplaces]})"
        )
        available_user_workplaces.remove(all_workplaces[count_workplaces])
        count_workplaces += 1
        for _ in range(number_workplaces - 1):
            workplace_to_add = random.choice(list(available_user_workplaces))
            cur.execute(
                f"INSERT INTO User_Work_place (user_id, work_place_id) "
                f"VALUES ({user_id}, {workplace_to_add})"
            )
            available_user_workplaces.remove(workplace_to_add)
            
        
        

    connection.commit()
    print("User_workplaces were added successfully!")
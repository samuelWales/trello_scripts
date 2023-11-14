import random

from database import DESK_NAME_LIST, DESK_ACCESS_LIST, DESK_BACKGROUND_LIST


def desk_insertion(connection, number_desks): # в одном workplace могут быть разные доски
    cur = connection.cursor()
    
    cur.execute(
        f"SELECT user_id FROM \"User\" "
        f"ORDER BY user_id"
    )
    all_users = list(map(lambda item: item[0], cur.fetchall()))
    
    cur.execute(
        f"SELECT work_place_id FROM Work_place"
    )
    all_workplaces = list(map(lambda item: item[0], cur.fetchall()))
    
    for admin_id in all_users: # один user - один admin одной доски
        name = random.choice(DESK_NAME_LIST)
        access = random.choice(DESK_ACCESS_LIST)
        background = random.choice(DESK_BACKGROUND_LIST)

        available_workplaces = set(all_workplaces) # чтобы для одной доски не повторялись рабочие пространства
        for _ in range(number_desks):
            to_what_workplace = random.choice(list(available_workplaces))
            available_workplaces.remove(to_what_workplace)
            cur.execute(
                f"INSERT INTO Desk (name, access, background, admin_id, work_place_id) "
                f"VALUES (\'{name}\', \'{access}\', \'{background}\', {admin_id}, {to_what_workplace})"
            )    
        
    connection.commit()
    print("Desks were added successfully!")
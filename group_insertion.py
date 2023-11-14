import random

from database import GROUP_NAME_LIST


def group_insertion(connection):
    cur = connection.cursor()
    
    cur.execute(
        f"SELECT work_place_id FROM Desk;"
    )
    all_workplaces = list(map(lambda item: item[0], cur.fetchall()))
    
    for workplace_id in all_workplaces:
        cur.execute(
            f"SELECT desk_id FROM Desk "
            f"WHERE work_place_id = {workplace_id};"
        )
        current_desks = list(map(lambda item: item[0], cur.fetchall()))
        name = random.choice(GROUP_NAME_LIST)
        
        for desk_id in current_desks:
            cur.execute(
                f"INSERT INTO \"Group\" (name, desk_id) "
                f"VALUES (\'{name}\', {desk_id})"
            )

    connection.commit()
    print("Groups were added successfully!")
import random

from database import WORKPLACE_NAME_LIST, WORKPLACE_TYPE_LIST, WORKPLACE_DESCRIPTION_LIST


def workplace_insertion(connection):
    cur = connection.cursor()
    
    cur.execute(
        f"SELECT user_id FROM \"User\""
    )
    all_users = list(map(lambda item: item[0], cur.fetchall()))
    
    for admin_id in all_users:
        name = random.choice(WORKPLACE_NAME_LIST)
        type = random.choice(WORKPLACE_TYPE_LIST)
        description = random.choice(WORKPLACE_DESCRIPTION_LIST)
        
        cur.execute(
            f"INSERT INTO Work_place (name, type, description, admin_id) "
            f"VALUES (\'{name}\', \'{type}\', \'{description}\', {admin_id})"
        )
        
        

    connection.commit()
    print("Workplaces were added successfully!")
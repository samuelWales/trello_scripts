import random
import string
from datetime import datetime as DT
from datetime import timedelta
from database import CARD_NAME_DESCRIPTION_LIST

def get_random_date(start, end):
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))

def card_insertion(connection, number): # в одном workplace могут быть разные доски
    cur = connection.cursor()
    
    cur.execute(
        f"SELECT group_id FROM \"Group\""
    )
    all_groups = list(map(lambda item: item[0], cur.fetchall()))
    

    for _ in range(number):
        name, description = random.choice(CARD_NAME_DESCRIPTION_LIST)
        
        start_dt = DT.strptime('01-01-2010', '%d-%m-%Y')
        end_dt = DT.strptime('01-01-2030', '%d-%m-%Y')
        deadlines = get_random_date(start_dt, end_dt)

        progress_bar = random.randint(0, 100)
        for group_id in all_groups:
            cur.execute(
                f"INSERT INTO card (name, description, deadlines, progress_bar, group_id) "
                f"VALUES (\'{name}\', \'{description}\', \'{deadlines}\', {progress_bar}, {group_id})"
            )  
        
    connection.commit()
    print("Cards were added successfully!")
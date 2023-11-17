import random
import string

from database import DESK_BACKGROUND_LIST
from database import LABEL_TEXT_LIST

def label_insertion(connection, number):
    cur = connection.cursor()
    
    cur.execute(
        f"SELECT work_place_id FROM Work_place"
    )
    all_workplaces = list(map(lambda item: item[0], cur.fetchall()))
    
    available_workplaces = set(all_workplaces)
    for _ in range(number):
        colour = random.choice(DESK_BACKGROUND_LIST)
        text = random.choice(LABEL_TEXT_LIST)
        to_what_workplace = random.choice(list(available_workplaces))
        available_workplaces.remove(to_what_workplace)
        cur.execute(
            f"INSERT INTO label (colour, text, work_place_id) "
            f"VALUES (\'{colour}\', \'{text}\', {to_what_workplace})"
        )    
        
    connection.commit()
    print("Labels were added successfully!")
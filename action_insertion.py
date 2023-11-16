import random
import string
from datetime import datetime as DT
from datetime import timedelta
from database import COMMENT_LIST, ACTION_NAME_LIST

def get_random_date(start, end):
    delta = end - start
    return start + timedelta(random.randint(0, delta.days))

def action_insertion(connection, number):
    cur = connection.cursor()
    
    cur.execute(
        f"SELECT user_id FROM \"User\""
    )
    all_users = list(map(lambda item: item[0], cur.fetchall()))

    cur.execute(
        f"SELECT card_id FROM card"
    )
    all_cards = list(map(lambda item: item[0], cur.fetchall()))

    for _ in range(number):
        for card_id in all_cards:
            users_to_add = random.sample(all_users, random.randint(1, 10))
            for user_id in users_to_add:
                is_comment = random.choice([True, False])
                if is_comment:
                    data = random.choice(COMMENT_LIST)
                else:
                    data = random.choice(ACTION_NAME_LIST)

                start_dt = DT.strptime('01-01-2010', '%d-%m-%Y')
                end_dt = DT.strptime('01-01-2030', '%d-%m-%Y')
                date = get_random_date(start_dt, end_dt)
                cur.execute(
                    f"INSERT INTO action (data, date, is_comment, user_id, card_id) "
                    f"VALUES (\'{data}\', \'{date}\', {is_comment}, {user_id}, {card_id})"
                ) 
        
    connection.commit()
    print("Actions were added successfully!")
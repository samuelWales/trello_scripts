import random

def card_file_insertion(connection):
    cur = connection.cursor()  
    
    cur.execute(
        f"SELECT card_id FROM card"
    )
    all_cards = list(map(lambda item: item[0], cur.fetchall()))
    
    cur.execute(
        f"SELECT file_id FROM file"
    )
    all_files = list(map(lambda item: item[0], cur.fetchall()))


    for card_id in all_cards:
        for file_id in all_files:
            cur.execute(
                f"INSERT INTO card_file (card_id, file_id) "
                f"VALUES ({card_id}, {file_id})"
            )

    



    connection.commit()
    print("Card files were added successfully!")
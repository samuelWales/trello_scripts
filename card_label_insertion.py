import random

def card_label_insertion(connection):
    cur = connection.cursor()
    
    cur.execute(
        f"SELECT card_id FROM card;"
    )
    all_cards = list(map(lambda item: item[0], cur.fetchall()))
    
    cur.execute(
        f"SELECT label_id FROM label;"
    )
    all_labels = list(map(lambda item: item[0], cur.fetchall()))

    for card_id in all_cards:
        for label_id in all_labels:
            cur.execute(
                f"INSERT INTO card_label (card_id, label_id) "
                f"VALUES ({card_id}, {label_id})"
            )

    connection.commit()
    print("Card labels were added successfully!")
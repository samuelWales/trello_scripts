import psycopg2
import random

from user_insertion import user_insertion
from workplace_insertion import workplace_insertion
from user_workplace_insertion import user_workplace_insertion
from desk_insertion import desk_insertion
from user_desk_insertion import user_desk_insertion
from group_insertion import group_insertion
from action_insertion import action_insertion
from card_insertion import card_insertion
from card_file_insertion import card_file_insertion
from card_label_insertion import card_label_insertion
from file_insertion import file_insertion
from label_insertion import label_insertion

con = psycopg2.connect(
    database = "trello",
    user = "arthur",
    password = "qwertyz",
    host = "localhost",
    port = 5432
)

print("Connection created successfully!")

user_insertion(connection = con, number = 200)
file_insertion(connection = con, number = 10)
workplace_insertion(connection = con)
label_insertion(connection = con, number = 10)
user_workplace_insertion(connection = con, number_workplaces = 3)
desk_insertion(connection = con, number_desks = 3)
user_desk_insertion(connection = con)
group_insertion(connection = con)
card_insertion(connection = con, number = 10)
label_insertion(connection = con, number = 3)
card_label_insertion(connection = con)
file_insertion(connection = con, number = 3)
card_file_insertion(connection = con)
action_insertion(connection = con, number = 5)


print('Everything is all right!')
con.close()
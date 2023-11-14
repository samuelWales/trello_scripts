import psycopg2
import random

from user_insertion import user_insertion
from workplace_insertion import workplace_insertion
from user_workplace_insertion import user_workplace_insertion
from desk_insertion import desk_insertion
from user_desk_insertion import user_desk_insertion

con = psycopg2.connect(
    database = "trello",
    user = "arthur",
    password = "qwertyz",
    host = "localhost",
    port = 5432
)

print("Connection created successfully!")
# user_insertion(connection = con, number = 200)
# workplace_insertion(connection = con)
# user_workplace_insertion(connection = con, number_workplaces = 3)
# desk_insertion(connection = con, number_desks = 3)
user_desk_insertion(connection = con, number_desks = 3)

print('Everything is all right!')
con.close()
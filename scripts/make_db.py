import sqlite3

con = sqlite3.connect('test.db')

cur = con.cursor()

cur.execute('''DROP TABLE IF EXISTS brain''')

cur.execute('''CREATE TABLE IF NOT EXISTS brain (
    user_id int,
    discord_id int,
    name varchar(100),
    machiavellianism double(2,1),
    narcissism double(2,1),
    psychopathy double(2,1),
    protestant_work_ethic int)''')


import sqlite3

con = sqlite3.connect('test.db')

cur = con.cursor()

cur.execute('''INSERT INTO brain (user_id, discord_id, name, machiavellianism, narcissism, psychopathy, protestant_work_ethic)
VALUES (0, 545011450159169577, "Mayank", 4.3, 3.7, 2, 44);''')

cur.execute('''INSERT INTO brain (user_id, discord_id, name, machiavellianism, narcissism, psychopathy, protestant_work_ethic)
VALUES (1, 454503286616096774, "Achint", 5, 3.4, 4.4, -1);''')

cur.execute('''INSERT INTO brain (user_id, discord_id, name, machiavellianism, narcissism, psychopathy, protestant_work_ethic)
VALUES (2, 694438526485397555, "Lia", 4.1, 2.4, 1.6, -1);''')

cur.execute('''INSERT INTO brain (user_id, discord_id, name, machiavellianism, narcissism, psychopathy, protestant_work_ethic)
VALUES (3, 690662977288011858, "Rishabh", 2.8, 2, 1.6, 46);''')
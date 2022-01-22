class BrainClient:

    def __init__(self):
        self.con = sqlite3.connect('test.db')
        self.cur = self.con.cursor()

    def renew_table(self):
        self.empty_table()
        self.populate_table()
    
    def empty_table(self):
        self.delete_table()
        self.create_table()

    def populate_table(self):
        self.cur.execute('''INSERT INTO brain (user_id, discord_id, name, machiavellianism, narcissism, psychopathy, protestant_work_ethic)
        VALUES (0, 545011450159169577, "Mayank", 4.3, 3.7, 2, 44);''')

        self.cur.execute('''INSERT INTO brain (user_id, discord_id, name, machiavellianism, narcissism, psychopathy, protestant_work_ethic)
        VALUES (1, 454503286616096774, "Achint", 5, 3.4, 4.4, -1);''')

        self.cur.execute('''INSERT INTO brain (user_id, discord_id, name, machiavellianism, narcissism, psychopathy, protestant_work_ethic)
        VALUES (2, 694438526485397555, "Lia", 4.1, 2.4, 1.6, -1);''')

        self.cur.execute('''INSERT INTO brain (user_id, discord_id, name, machiavellianism, narcissism, psychopathy, protestant_work_ethic)
        VALUES (3, 690662977288011858, "Rishabh", 2.8, 2, 1.6, 46);''')

    def read_table(self):
        self.cur.execute('''SELECT * FROM brain''')
        rows = self.cur.fetchall()
        return [row for row in rows]

    def delete_table(self):
        self.cur.execute('''DROP TABLE IF EXISTS brain''')

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS brain (
            user_id int,
            discord_id int,
            name varchar(100),
            machiavellianism double(2,1),
            narcissism double(2,1),
            psychopathy double(2,1),
            protestant_work_ethic int)''')




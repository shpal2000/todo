import sqlite3

def create_tables(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute (''' DROP TABLE IF EXISTS user''')

    c.execute (''' CREATE TABLE user
                        (user_name text PRIMARY KEY, 
                        user_pass text NOT NULL,
                        full_name text NOT NULL,
                        primary_email text NOT NULL,
                        primary_phone text NOT NULL
                        )''')
                        
    conn.commit()
    conn.close()

def add_user(db_file, 
                user_name_param,
                user_pass_param,
                full_name_param,
                primary_email_param,
                primary_phone_param):

    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute( '''INSERT INTO user (user_name, 
                                    user_pass, 
                                    full_name, 
                                    primary_email, 
                                    primary_phone)
                        VALUES (?, ?, ?, ?, ?)''',  
                                    (user_name_param, 
                                    user_pass_param,
                                    full_name_param,
                                    primary_email_param,
                                    primary_phone_param) )
                        
    conn.commit()
    conn.close()


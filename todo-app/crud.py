import sqlite3

def create_tables(db_file):
    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    # c.execute (''' DROP TABLE IF EXISTS user''')

    # c.execute (''' CREATE TABLE user
    #                     (user_name text PRIMARY KEY, 
    #                     user_pass text NOT NULL,
    #                     full_name text,
    #                     primary_email text NOT NULL,
    #                     primary_phone text
    #                     )''')
                        
    conn.commit()
    conn.close()

def add_user(db_file
                , user_name_value
                , user_pass_value
                , primary_email_value
                , full_name_value = ''
                , primary_phone_value = ''):

    conn = sqlite3.connect(db_file)
    c = conn.cursor()

    c.execute( '''INSERT INTO user (user_name, 
                                    user_pass, 
                                    full_name, 
                                    primary_email, 
                                    primary_phone)
                        VALUES (?, ?, ?, ?, ?)''',  
                                    (user_name_value, 
                                    user_pass_value,
                                    full_name_value,
                                    primary_email_value,
                                    primary_phone_value) )
                        
    conn.commit()
    conn.close()


import pytest
import sqlite3

import crud

def test_create_table():
    crud.create_tables('crud_test.db')

    conn = sqlite3.connect('crud_test.db')
    c = conn.cursor()
    c.execute ('''
                SELECT COUNT(name) 
                FROM sqlite_master 
                WHERE type="table" AND name="user" 
                ''' )
    count = c.fetchone()[0]
    conn.close()
    assert count == 1


def test_add_user():

    conn = sqlite3.connect('crud_test.db')
    c = conn.cursor()

    c.execute ('''
                SELECT COUNT(user_name) 
                FROM user 
                WHERE user_name="fake_user1"
                ''' )
    count = c.fetchone()[0]
    assert count == 0

    crud.add_user('crud_test.db', 
                    'fake_user1',
                    'fake_pass1',
                    'fake_name1',
                    'fake_email1@test.com',
                    '(111)111-1111')    

    c.execute ('''
                SELECT COUNT(user_name) 
                FROM user 
                WHERE user_name="fake_user1"
                ''' )
    count = c.fetchone()[0]
    conn.close()
    assert count == 1



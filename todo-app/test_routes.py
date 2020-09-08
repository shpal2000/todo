from functools import lru_cache
from fastapi.testclient import TestClient

import main, config, crud

import pdb

client = TestClient(main.app)

@lru_cache
def get_settings():
    settings = config.Settings(db_file='todo_test.db')
    crud.create_tables (settings.db_file)
    return settings

main.app.dependency_overrides[main.get_settings] = get_settings 

def test_add_user():
    response = client.post('/add_user',
                            json={"user_name" : "user_name1",
                                    "user_pass" : "password",
                                    "full_name" : "jakie chan",
                                    "primary_email" : "jakie@test.com",
                                    "primary_phone" : "(111)111-1111"})

    assert response.status_code == 200
    
    assert response.json() == {"user_name" : "user_name1",
                                    "user_pass" : "password",
                                    "full_name" : "jakie chan",
                                    "primary_email" : "jakie@test.com",
                                    "primary_phone" : "(111)111-1111"}



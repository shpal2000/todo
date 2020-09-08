from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = 'todo admin'
    db_file: str = 'todo.db'
    class Config:
        env_file = '.env_todo'
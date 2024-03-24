from typing import List
from src.domain.models.users import Users


class UsersRepositorySpy:

    def __init__(self):
        self.select_user_attributes = {}
        self.insert_user_attributes = {}
        self.delete_user_attributes = {}

    def insert_user(self, first_name: str, last_name: str, age: str) -> int:
        self.insert_user_attributes["first_name"] = first_name
        self.insert_user_attributes["last_name"] = last_name
        self.insert_user_attributes["age"] = age

    def select_user(self, first_name: str) -> List[Users]:
        self.select_user_attributes["first_name"] = first_name
        return [
            Users(id=1, first_name=first_name, last_name='last_name', age=42),
            Users(id=2, first_name=first_name, last_name='last_name_2', age=41)
        ]

    def delete_user(self, user_id: int) -> None:
        self.delete_user_attributes['user_id'] = user_id
        return None

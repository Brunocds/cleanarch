from abc import ABC, abstractmethod
from typing import List
from src.domain.models.users import Users


class UsersRepository(ABC):

    @abstractmethod
    def insert_user(self, first_name: str, last_name: str, age: str) -> int:
        pass

    @abstractmethod
    def select_user(self, first_name: str) -> List[Users]:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        pass

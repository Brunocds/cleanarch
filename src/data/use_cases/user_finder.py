# pylint: disable=broad-exception-raised
from typing import Dict, List
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users


class UserFinder(UserFinderInterface):

    def __init__(self, users_repository: UsersRepositoryInterface):
        self.__users_repository = users_repository

    def find(self, first_name: str) -> Dict:

        self.__validate_name(first_name)
        users = self.__search_users(first_name)
        response = self.__format_response(users)

        return response

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise Exception('Nome invalido para a busca')

        if len(first_name) > 18:
            raise Exception('Nome muito grande para busca')

    def __search_users(self, first_name: str) -> List[Users]:
        users = self.__users_repository.select_user(first_name)
        if users == []:
            raise Exception('Usuario nao encontrado')
        return users

    @classmethod
    def __format_response(cls, users: List[Users]) -> Dict:
        attributes = []
        for user in users:
            attributes.append(
                {"first_name": user.first_name, "age": user.age}
            )

        response = {
            'type': 'Users',
            'count': len(users),
            'attributes': attributes
        }

        return response


# validar que só tem caracteres alfanuméricos
# validar que não tem comprimento maior que 18
# retornar erro caso não encontre o usuário
# formatar a resposta de volta

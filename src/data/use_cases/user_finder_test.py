from src.data.use_cases.user_finder import UserFinder
from src.infra.db.tests.users_repository import UsersRepositorySpy


def test_find():
    first_name = 'John'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    response = user_finder.find(first_name)

    assert repo.select_user_attributes['first_name'] == 'John'

    assert response['type'] == 'Users'
    assert response['count'] == len(response['attributes'])
    assert response['attributes']


def test_error_invalid_name():
    first_name = 'John_'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as e:
        assert str(e) == 'Nome invalido para a busca'


def test_error_long_name():
    first_name = 'JohnJohnJohnJohnJohn'

    repo = UsersRepositorySpy()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as e:
        assert str(e) == 'Nome muito grande para busca'


def test_error_user_not_found():
    class UsersRepositoryError(UsersRepositorySpy):
        def select_user(self, first_name: str):
            return []

    first_name = 'John'

    repo = UsersRepositoryError()
    user_finder = UserFinder(repo)

    try:
        user_finder.find(first_name)
        assert False
    except Exception as e:
        assert str(e) == 'Usuario nao encontrado'

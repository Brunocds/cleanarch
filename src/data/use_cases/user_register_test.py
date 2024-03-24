from src.data.use_cases.user_register import UserRegister
from src.infra.db.tests.users_repository import UsersRepositorySpy


def test_register():

    first_name = "Bruno"
    last_name = "Costa"
    age = 24

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    response = user_register.register(first_name, last_name, age)

    assert repo.insert_user_attributes["first_name"] == first_name
    assert repo.insert_user_attributes["last_name"] == last_name
    assert repo.insert_user_attributes["age"] == age

    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]


def test_register_first_name_error():

    first_name = "Bruno123"
    last_name = "Costa"
    age = 24

    repo = UsersRepositorySpy()
    user_register = UserRegister(repo)

    try:
        user_register.register(first_name, last_name, age)
        assert False
    except Exception as exception:
        assert str(exception) == 'Nome invalido para o cadastro'

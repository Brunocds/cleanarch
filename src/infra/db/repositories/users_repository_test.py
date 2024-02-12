from sqlalchemy import select
from sqlalchemy import text
import pytest
from src.infra.db.repositories.users_repository import UsersRepository
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity


@pytest.mark.skip(reason="Sensive test")
def test_insert_user():
    mocked_first_name = "first"
    mocked_last_name = "last"
    mocked_age = 34

    users = UsersRepository()
    id_user_inserted = users.insert_user(
        first_name=mocked_first_name, last_name=mocked_last_name, age=mocked_age
    )

    with DBConnectionHandler() as database:
        stmt = select(UsersEntity).where(UsersEntity.id == id_user_inserted)
        user = database.session.execute(stmt).all()[0][0]

    assert (
        (user.first_name == mocked_first_name)
        & (user.last_name == mocked_last_name)
        & (user.age == mocked_age)
    )

    users.delete_user(user_id=id_user_inserted)


# The insert function below is redundant but is the one from the course. Keeping it here just for historic
@pytest.mark.skip(reason="Sensive test")
def test_insert_user_2():
    mocked_first_name = "first"
    mocked_last_name = "last"
    mocked_age = 51

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)

    sql = f"""
        SELECT 
            * 
        FROM 
            clean_arch.users 
        WHERE 
            first_name = '{mocked_first_name}'
            and last_name = '{mocked_last_name}'
            and age = '{mocked_age}'
    """
    db_connection_handler = DBConnectionHandler()
    connection = db_connection_handler.get_engine().connect()
    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.first_name == mocked_first_name
    assert registry.last_name == mocked_last_name
    assert registry.age == mocked_age

    connection.execute(text(f"DELETE FROM clean_arch.users WHERE id = {registry.id}"))
    connection.commit()
    connection.close()


def test_select_user():
    mocked_first_name = "firstname"
    mocked_last_name = "lastname"
    mocked_age = 10

    db_connection_handler = DBConnectionHandler()
    connection = db_connection_handler.get_engine().connect()
    sql = f"""
        INSERT INTO clean_arch.users (first_name, last_name, age)
        VALUES ('{mocked_first_name}', '{mocked_last_name}', '{mocked_age}')
    """
    connection.execute(text(sql))
    connection.commit()

    users = UsersRepository()
    list_of_users = users.select_user(first_name=mocked_first_name)

    assert list_of_users[0].first_name == mocked_first_name
    assert list_of_users[0].last_name == mocked_last_name
    assert list_of_users[0].age == mocked_age

    sql = f"""
        DELETE FROM clean_arch.users 
        WHERE id = '{list_of_users[0].id}'
    """
    connection.execute(text(sql))
    connection.commit()
    connection.close()


if __name__ == "__main__":
    # test_insert_user()
    # test_insert_user_2()
    test_select_user()

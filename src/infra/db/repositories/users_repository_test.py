from sqlalchemy import select
from sqlalchemy import text
from src.infra.db.repositories.users_repository import UsersRepository
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity


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


# Código do curso
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
    registry = response.fetchall()
    print(registry)


if __name__ == "__main__":
    test_insert_user_2()

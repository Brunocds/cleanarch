from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UsersEntity


class UsersRepository:

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: str) -> int:
        with DBConnectionHandler() as database:
            try:
                new_registry = UsersEntity(
                    first_name=first_name, last_name=last_name, age=age
                )
                database.session.add(new_registry)
                database.session.commit()
                return new_registry.id
            except Exception as e:
                database.session.rollback()
                raise e

    @classmethod
    def delete_user(cls, user_id: int) -> None:
        with DBConnectionHandler() as database:
            try:
                database.session.query(UsersEntity).where(
                    UsersEntity.id == user_id
                ).delete()
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e

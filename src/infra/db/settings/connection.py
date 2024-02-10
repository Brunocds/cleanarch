from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = (
            "postgresql://{user}:{password}@{server}/{database}".format(
                user="swfjmtxl",
                password="gn8-nFkwwSiNDxWmzrjwqbB6oibKVzA7",
                server="jelani.db.elephantsql.com",
                database="swfjmtxl",
            )
        )
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        # The NullPool makes the session.close() really close the connection. Without this config, even running the
        # session.close() the connection was kept open. See
        # https://stackoverflow.com/questions/21738944/how-to-close-a-sqlalchemy-session for more information
        engine = create_engine(self.__connection_string, poolclass=NullPool)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

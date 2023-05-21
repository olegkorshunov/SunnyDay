class DBException(Exception):
    pass


class DBDontExist(DBException):
    def __init__(self, *args: object) -> None:
        if args:
            self.db_name = f"{args[0]} "
        else:
            self.db_name = ""

    def __str__(self) -> str:
        return f"{self.db_name}DB don't exist"


class DBAlredyExist(DBException):
    def __init__(self, *args: object) -> None:
        if args:
            self.db_name = f"{args[0]} "
        else:
            self.db_name = ""

    def __str__(self) -> str:
        return f"{self.db_name}DB alredy exist"


raise DBDontExist(123)

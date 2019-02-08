from clcrypto import password_hash


class DatabaseObject:
    pass


class User(DatabaseObject):
    table_name = 'User'

    def __init__(self, username=None, password=None, email=None):
        self.__id = None
        self.username = username
        self.password = password_hash(password)
        self.email = email



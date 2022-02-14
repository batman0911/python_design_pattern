class DatabaseConnection:
    __instance = None

    def __init__(self):
        if DatabaseConnection.__instance is not None:
            raise Exception("Singleton class")
        else:
            DatabaseConnection.__instance = self

    @staticmethod
    def get_instance():
        if DatabaseConnection.__instance is None:
            DatabaseConnection()
        return DatabaseConnection.__instance


if __name__ == "__main__":
    s1 = DatabaseConnection()
    s2 = DatabaseConnection.get_instance()
    s3 = DatabaseConnection.get_instance()

    print(s1, s2, s3)

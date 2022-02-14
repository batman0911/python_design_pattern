import threading


class Singleton(object):
    _instance = None
    _lock = threading.Lock()
    company = "GHTK"

    def __init__(self):
        if Singleton._instance is not None:
            raise Exception("Singleton class")
        else:
            Singleton._instance = self

    @staticmethod
    def get_instance():
        if Singleton._instance is None:
            with Singleton._lock:
                if Singleton._instance is None:
                    Singleton()
        return Singleton._instance

    def greeting(self, name: str):
        print(f'hello {name} of {self.company}')


def test_singleton(name: str) -> None:
    singleton = Singleton.get_instance()
    print(singleton)
    singleton.greeting(name)


if __name__ == "__main__":
    process1 = threading.Thread(target=test_singleton("Linh Nguyen"), name="Thread-1")
    process2 = threading.Thread(target=test_singleton("Mai Tran"), name="Thread-2")

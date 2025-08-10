class Singleton:
    _instance = None  # keeps the only object we ever make.

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # First call → None → create it.
        return cls._instance  # Later calls → return existing _instance.


a = Singleton()
b = Singleton()

print(a is b)

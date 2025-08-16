class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=MetaSingleton):
    pass


log1 = Singleton()
print(f'Log1: {id(log1)}')

log2 = Singleton()
print(f'Log2: {id(log2)}')
class Singleton(type):
    _initialize = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._initialize:
            cls._initialize[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._initialize[cls]

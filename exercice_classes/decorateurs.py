# en param ==> fonction
# combien de return ==> 2 : un pour le wrapper, 
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Temps d'exécution de {func.__name__}: {end_time - start_time: .2f} secondes")
        return result
    return wrapper

def log_activity(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} - args: {args} - kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

def instance_counter(cls):
    # objectif ==> classe
    # __init__ déclenché à l'instanciation ==> combien de fois __init__ a été appelé
    cls._instances = 0
    
    init_origin = cls.__init__
    
    def new_init(self, *args, **kwargs):
        cls._instances += 1
        init_origin(self, *args, **kwargs)
    
    cls.__init__ = new_init
    cls.get_instances_count = lambda: cls._instances
    return cls
        
        


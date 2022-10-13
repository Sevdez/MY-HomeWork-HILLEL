from functools import wraps


def expected(expected_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func()
            if type(result) not in expected_types:
                print("unexpected type")
        return wrapper
    return decorator

@expected((str, int))
def a ():
    return None

a()
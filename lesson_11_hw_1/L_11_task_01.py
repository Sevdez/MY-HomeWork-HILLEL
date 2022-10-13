from functools import wraps


def expected(expected_types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if type(result) not in expected_types:
                raise Exception("тут шото не тот тип =)")
        return wrapper
    return decorator

@expected((str, int))
def examination(value):
    return value

examination()

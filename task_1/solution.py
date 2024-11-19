def strict(func):
    def wrapper(*args, **kwargs):
        annotations = func.__annotations__
        for arg_name, arg_value in zip(annotations.keys(), args):
            expected_type = annotations.get(arg_name)
            if expected_type and not isinstance(arg_value, expected_type):
                raise TypeError(
                    f"Argument '{arg_name}' must be of type {expected_type.__name__}, "
                    f"but got {type(arg_value).__name__}"
                )
        return func(*args, **kwargs)
    return wrapper


@strict
def sum_two(a: int, b: int) -> int:
    return a + b

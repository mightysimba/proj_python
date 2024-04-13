# 1

def is_admin(user_id):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_type = kwargs.get('user_type')
            if user_type == user_id:
                return func(*args, **kwargs)
            else:
                raise ValueError(f"Permission denied. Required role: {user_id}")
        return wrapper
    return decorator


@is_admin('admin')
def delete_user(*args, **kwargs):
    user_type = kwargs.get('user_type')
    print(f"User with type {user_type} is allowed to delete a user.")


delete_user(user_type='admin')
#delete_user(user_type='guest')

# 2


def catch_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Found 1 error during execution of your function: KeyError no such key as {e}")
    return wrapper


@catch_errors
def some_function_with_risky_operation(data):
    print(data['foo'])


some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})

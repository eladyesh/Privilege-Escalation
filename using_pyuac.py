import pyuac
from functools import wraps

def run_as_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not pyuac.isUserAdmin():
            print("Re-launching as admin!")
            pyuac.runAsAdmin()
        else:
            func(*args, **kwargs)  # Already an admin here.
    return wrapper

@run_as_admin
def my_function():
    # Your code here
    pass

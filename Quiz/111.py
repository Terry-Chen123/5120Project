from functools import wraps


def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)

    return decorated

@decorator_name
def func():
    return ("Function is running")

can_run = True


input_list = []
while True:
    try:
        line = input()
        input_list.append(line.split())
    except:
        break
print(ord('a') - ord('a'))

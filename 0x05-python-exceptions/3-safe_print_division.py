#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except Exception:
        return None
    finally:
        if result > 0:
            print("Inside result: {}".format(result))
        else:
            print("Inside result: None")
    return result

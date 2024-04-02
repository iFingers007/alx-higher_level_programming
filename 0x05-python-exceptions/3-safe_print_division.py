#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0;
    try:
        result = a / b
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(result) if result > 0 else "Inside result: None")
    return result

#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b
    except ZerDivisionError:
        print("Error: Division by Zero is not allowed.")
    finally:
        print("Inside result: {}".format(result))
        return result

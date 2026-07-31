def DivExp(a, b):
    assert a > 0, "Value of 'a' must be greater than 0"
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    c = a / b
    return c
try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    result = DivExp(a, b)
    print("Result (a/b) =", result)
except AssertionError as e:
    print("Assertion Error:", e)
except ZeroDivisionError as e:
    print("Exception:", e)
except ValueError:
    print("Please enter valid integers.")

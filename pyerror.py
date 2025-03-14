try:
    name = input("what is your name: ")
    a = int(input("input number a: "))
    b = int(input("input number b: "))
    print(name, a/b)
except ValueError:
    print("invalid input")
except ZeroDivisionError as k:
    print(k, "cannot divide by Zero")
else:
    print(f'{name}, your answer is {a/b}')
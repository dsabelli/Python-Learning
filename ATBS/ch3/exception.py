def spam(div):
    try:
        return 42 / div
    except ZeroDivisionError:
        print("Error: Invalid Arg.")


print(spam(2))
print(spam(20))
print(spam(0))
print(spam(1))

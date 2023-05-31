def zigzag(num):
    for i in range(num):
        for i in range(5, 0, -1):
            print(" " * i, end="")
            print("********")
        for i in range(1, 5):
            print(" " * i, end="")
            print("********")


zigzag(20)

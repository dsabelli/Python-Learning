def hello():
    print("Hello")
    print("How are you?")


hello()

test = "global"
test2 = "asd"


def scope():
    test = "local"
    global test2
    test2 = "mod"
    print(test)
    print(test2)


scope()

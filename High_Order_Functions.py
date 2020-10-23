def foo(k):  # This is a higher order function
    global g
    i = 27

    def bar():
        nonlocal i
        i = 25
        print("entering inner function")
        # change outer scope's i

        print(i)
        print("leaving inner function")

    print("entering foo")
    print(g)
    g = "changed in foo ;-)"
    print(g)
    bar()
    print(".. leaving foo")
    print(i)


g = "wow this is pretty cool"
foo(7)


def greet(name, msg):  # Another higher order function (maybe)
    """
    this function greets to the person with the provided message,
    Where name defaults to "Tom and message defaults to "Good Morning!"
    :param name: str: name of person
    :param msg: str: what you want it to say
    :return: message
    """
    print("Hello",name + ', ' + msg)


greet("Andrew", "Good Morning!")

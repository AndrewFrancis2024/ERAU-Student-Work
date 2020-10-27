# High Order Function Examples
# putting a function inside a variable
def whisper(t):
    return t.lower()


lower = whisper
print(lower("I didn't understand anything he was saying about Python... \n"))

# Putting a function inside of another function


def action(k):
    global a
    a = "I am the action in the first level of the function"

    def sub():
        print("Now inside inner function")
        k = "Something happening in the inner function."
        print(k)
        print("Now exiting inner function")
    sub()
    print("Back in the first level of the function")
    print(a)
    print(f"You entered '{k}' into the action, congrats, it did nothing. \n")


a = "I am outside the function "
action("wow")  # Because variable 'a' is assigned in the function and it is a global, I have to reassign 'a'
print(a, '\n')

a = "I am outside the function \n "
print(a)

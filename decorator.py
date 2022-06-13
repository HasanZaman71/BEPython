


def second_func(func):
    def inside_func():
        print("This is second function")
        func()

#my_func = second_func(first_func)
#my_func()

@second_func
def first_func():
    print("this is my first function")

first_func()
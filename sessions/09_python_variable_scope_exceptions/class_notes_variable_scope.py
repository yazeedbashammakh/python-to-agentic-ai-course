

# Function

# def func_1():
#     x = 10.  # --> Local variable
#     print("Inside func_1, x =", x)


# func_1()
# print("Outside func_1, x =", x)

# def func_1():
#     x = 10  # --> Local variable
#     print("Inside func_1, x =", x)

# x = 20 # --> Global Variable 
# print("Before func_1 call, x =", x)
# func_1()
# print("After func_1, x =", x)


# def func_1():
#     print("Inside func_1, x =", x)

# x = 20 # --> Global Variable 
# print("Before func_1 call, x =", x)
# func_1()
# print("After func_1, x =", x)


def func_1():
    global x
    x = 10
    print("Inside func_1, x =", x)


x = 20 # --> Global Variable 
print("Before func_1 call, x =", x)
func_1()
print("After func_1, x =", x)



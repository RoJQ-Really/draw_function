from matplotlib import pyplot as plt
import numpy as np
import setting_method
from setting_method import setting_menu


# -- linear draw method start
def linear_function_draw(k_arg, b_arg):  # take arg  k and b in linear function
    x_cords = []
    y = []
    for x in range(2):  # find function coord ._.
        x_cords.append(x)
        y_cords = k_arg * x + b_arg
        y.append(y_cords)
    plt.plot(x_cords, y)
    plt.title('График линейной функции')
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def linear_arg_input():  # filtered and transmits argument to linear_function_draw
    b_arg = input('b = ')
    k_arg = input('k = ')
    b = None
    k = None
    if '-' in k_arg:
        k = -float(k_arg.replace('-', ''))
    elif k_arg.isdigit():
        k = float(k_arg)
    else:
        print("Error : k_arg is bad syntax. Pls use number")
        exit()

    if '-' in b_arg:
        b = -float(b_arg.replace('-', ''))
    elif b_arg.isdigit():
        b = float(b_arg)
    else:
        print("Error : b_arg is bad syntax. Pls use number")

    linear_function_draw(k, b)


# -- linear drawing method end


# -- parabola draw method start


def parabola_function_draw(a_arg, b_arg, c_arg, extreme_left_point, extreme_right_point):  # drawing parabola
    print('parabola_function_draw : start')
    x_cords = np.linspace(-100, 100, 100)
    y_cords = a_arg * x_cords ** 2 + b_arg * x_cords + c_arg
    fig, ax = plt.subplots()
    ax.plot(x_cords, y_cords)
    plt.title("График парабола")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


def parabola_arg_input():  # transmit value in parabola_function_draw
    a = b = c = 0
    a_arg = input('a - arg = ')
    b_arg = input('b - arg = ')
    c_arg = input('c - arg = ')
    if '-' in a_arg:
        a = -float(a_arg.replace('-', ''))  # if negative int
    elif a_arg.isdigit():  # check on number value
        a = float(a_arg)
    else:  # Bad Syntax Error
        print('Error : a_arg is bad syntax. Pls use number')
        exit()
    if '-' in b_arg:
        b = -float(b_arg.replace('-', ''))  # if negative int
    elif b_arg.isdigit():
        b = float(b_arg)
    else:  # Bad Syntax Error
        print('Error : b_arg is bad syntax. Pls use number')
        exit()
    if '-' in c_arg:
        c = -float(c_arg.replace('-', ''))  # if negative int
    elif c_arg.isdigit():  # check on number value
        c = float(c_arg)
    else:  # Bad Syntax Error
        print('Error : c_arg is bad syntax. Pls use number')
        exit()
    print(a, b, c)
    parabola_function_draw(a, b, c, None, None)


# -- parabola drawing method end


def start_menu(int_arg: int, str_arg: str, bool_arg: bool, list_arg: list):  # main menu
    check_input = True
    while check_input is True:
        print('1. График прямая \n2. График параболла')
        check_input = input('Select :')
        if check_input == '1':  # checking the entered information
            linear_arg_input()
        elif check_input == '2':
            parabola_arg_input()
        elif check_input == '3':
            setting_method.setting_menu()  # call setting menu p.s. I export this func in separate new file because it's more convenient
        else:
            print('Error : Input entered value is bad syntax')
            exit()


start_menu(0, 'default', False, 0)

from menu_creator_lib import console_menu as crem
def parabola_setting_menu():
    crem.create(input_separator='')


def linear_setting_menu():
    pass


# -- setting method start here --
def setting_menu():  # setting of the program
    setting_input_check = True  # Param for input values
    while setting_input_check is True:
        print('Настройки: \n1.Настройки линейной функции\n2.Настройки параболы')
        setting_input_check = input("Введите цифру")  # Input
        if setting_input_check == '1':
            linear_setting_menu()
        elif setting_input_check == '2':
            parabola_setting_menu()
        else:
            print('Error : Input entered value is bad syntax')
            exit()

# -- setting method stop here --

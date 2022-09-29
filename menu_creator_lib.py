import re


class ConsoleMenu():
    def __init__(self):
        pass

    def create(self=0, menu_title: str = 'Menu Choise', input_separator: str = '-->', setting_menu_creator: list = []):
        """

        :param menu_title: Message in main str menu
        :param input_separator: Separator input are    p.s. yes my En is Great
        :param setting_menu_creator: Parameters of menu  p.s Check example

        Example :
        from menu_creator_lib import console_menu as crem  # export method create at crem
        def MyMethod1():
            print('You chose first par')
        def MyMethod2():
            print('You chose second par')

        MyVar = crem.create(menu_title = 'MyMessage at main menu: ',input_separator = '--> ', setting_menu_creator = [['first par', 'MyMethod1()'],['second par', 'MyMethod2()']],)
        MyVar.crem.show()

        Out :
        >> MyTitle at main menu:
        >> 1.first par
        >> 2.second par
        >> --> [input area]  # for example i input '1'
        >> You chose first par

        """
        create_checker = True
        quantity = len(setting_menu_creator)
        while create_checker is True:
            print(menu_title)
            dictionary = {}  # set dictionary..
            for i in range(quantity):  # print menu with your arg (text_parameter) and litle filter
                print(f"{i + 1}.{str(setting_menu_creator[i][0])}")  # print menu colum
                dictionary[str(i + 1)] = str(setting_menu_creator[i][1])  # add to dict method
            create_checker = input(input_separator)  # input chose
            if not create_checker.isdigit():  # if not int
                print('Error : bad syntax in input. Please input number')
                exit()
            else:  # execution of the received argument begins
                eval(dictionary.get(create_checker))  # Выполняет код! ! !

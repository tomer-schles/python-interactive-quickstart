"""

Exercise #1 - Basic Restaurant Order Management System

Tomer's Interactive python quickstart guide

"""


class OrderManagementSystem:
    def __init__(self):
        print OrderManagementSystem.welcome_message

    welcome_message = NotImplemented

    # __orders is an internal variable representing the systems state
    __orders = NotImplemented

    # TIP: __orders should be a dictionary - http://www.tutorialspoint.com/python/python_dictionary.htm

    def start(self):
        """ reads input from the user and passes input to handle_command """

        # Check this out for reading input - http://www.python-course.eu/input.php

        raise NotImplementedError

    def handle_command(self, command, *args):
        """ Executes the correct command according to the command chosen by the user """

        # Some Tips for implementation:
        # see https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/

        raise NotImplementedError

    def add(self, *dishes): raise NotImplementedError

    def remove(self, *dishes): raise NotImplementedError

    def order(self, *dishes_amount): raise NotImplementedError

    def status(self): raise NotImplementedError

    def reset(self): raise NotImplementedError


if __name__ == '__main__':
    order_management_system = OrderManagementSystem()

    order_management_system.start()

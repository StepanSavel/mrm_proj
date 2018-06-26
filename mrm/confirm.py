"""
this is confirm module, it contains function which returns variable confirm == True or False
"""


def ask_for_confirm():
    """this function returns variable confirm == True/False"""
    confirm = False
    yn = raw_input("Are you sure? [y/n] ")
    if yn == "n":
        print("operation canceled")
        return confirm
    elif yn != "y" and yn != "n":
        print("y to confirm /n n to exit")
        ask_for_confirm()
    elif yn == "y":
        confirm = True
        return confirm

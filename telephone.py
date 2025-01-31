def get_contact():
    name = input("please enter your name: ")
    number = int(input("please enter your number: "))

    information = {"name": name, "number": number}

    return information


get_contact()

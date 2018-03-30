""""Phonebook"""

phonebook = dict()

def add(name: str) -> None:
    """A function to add a number in phonebook.
    """
    number = input("Введите номер телефона: ")
    if number.isdigit():
        number = int(number)
        if name not in phonebook:
            phonebook[name] = set()
            phonebook[name].add(number)
        else:
            phonebook[name].add(number)
    else:
        print("Номер введен некорректно!")

def display(person_on_display: str) -> None:
    """A function to display numbers by input name.
    """
    print("Имя".ljust(12), end=' ')
    print("Телефон".ljust(12))
    for i in phonebook[person_on_display]:
        print(f"{person_on_display}".ljust(12), end=' ')
        print(f"{i}".ljust(12))

def delete(person_on_delete: str) -> None:
    """A function to delete numbers by input name.
    """
    del phonebook[person_on_delete]

def check_phonebook(func):
    """A function to check a input name in phonebook and return function.
    """
    def inner(name: str):
        """Function of action"""
        if name in phonebook:
            return func(name)
        else:
            print("Такого человека нет в справочнике.")
    return inner

def act(action: int)-> None:
    """A function to get a number of action and call action.
    """
    if int(action) == 1:
        name = input("Введите имя: ")
        add(name)
    elif int(action) == 2 and phonebook:
        name = input("Введите имя: ")
        show(name)
    elif int(action) == 3 and phonebook:
        name = input("Введите имя: ")
        remove(name)
    elif not phonebook:
        print("Справочник пуст.")

def interface() -> None:
    """A function to show the main interface and ask a number of action.
    """
    print("Главное меню")
    print("1.Добавить номер и имя человека")
    print("2.Вывести номер человека")
    print("3.Удалить человека")
    print("4.Выйти")
    print()

    action = 0
    while action != 4:
        action = input("Введите номер действия: ")
        if action.isdigit():
            action = int(action)
            act(action)
        else:
            print("Введите циФру от 1 до 4.")

show = check_phonebook(display)
remove = check_phonebook(delete)

interface()

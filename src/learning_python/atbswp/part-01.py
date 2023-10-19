# Automate the Boring Stuff with Python
# By Al Sweigart

# Chapter 4 - Lists


def keyboard_interrupt():
    while True:
        try:
            response = input()
            if int(response) % 2 == 0:
                print('Even')
            else:
                print('Odd')
        except ValueError:
            print('ValueError: Please enter an integer.')
        except KeyboardInterrupt:
            print('\nKeyboardInterrupt: Program terminated.')
            break


def list_insert():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    spam.insert(-1, 'and')
    print(', '.join(spam))


def list_remove():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    spam.remove('apples')
    print(', '.join(spam))


def identity():
    name = 'Zophie'
    age = 7
    print(id(name))
    print(id(age))
    print(id(name + ' Hanna'))


def copy_and_deep_copy():
    import copy

    fruits = ['apples', 'bananas', 'tofu', 'cats']
    fruits_nocopy = fruits
    fruits_copy = copy.copy(fruits)
    fruits_deep_copy = copy.deepcopy(fruits)
    print(id(fruits))
    print(id(fruits_nocopy))
    print(id(fruits_copy))
    print(id(fruits_deep_copy))


# Chapter 5 - Dictionaries and Structuring Data


def dict_setdefault():
    d = {'name': 'Pooka', 'age': 5}
    print(d.setdefault('color', 'black'))
    print(d)
    print(d.setdefault('color', 'white'))


def pretty_printing():
    d = {'name': 'Pooka', 'age': 5}
    import pprint

    pprint.pprint(d)
    print(pprint.pformat(d))


# Chapter 6 - Manipulating Strings


def justify():
    s = (
        'It was a bright cold day in April, '
        + 'and the clocks were striking thirteen.'
    )
    print(s.ljust(70, '*'))


def clipboard():
    import pyperclip

    pyperclip.copy('Hello world!')
    print(pyperclip.paste())


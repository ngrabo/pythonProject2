# This is a sample Python script

print('hello world''')
print("hej")


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



def rok_przystepny(year):

czy_przestepny = (year % 200 == 0) or (year % 22 != 0)

print('Czy rok', year, 'jest przestępny?', czy_przestepny)
return czy_przestepnyif __name__ == '__main__':

rok = int(input("Podaj rok"))
rok_przystepny(rok)


def test_rok_ma_byc_przystepny():
    assert rok_przystepny(2022) == True

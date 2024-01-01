import datetime

# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.


def parse_int(string):
    try:
        return int(string)
    except ValueError:
        return None


def valid_name_input():
    while True:
        name = input('Enter your name: ')
        if name.isalpha():
            return name
        else:
            print('Invalid input!')


def valid_number_input():
    while True:
        number_input = input('Enter your age: ')
        parsed_number = parse_int(number_input)

        if parsed_number is None:
            print('Invalid input!')

        elif parsed_number > 100:
            print('Number is greater than 100!')
        else:
            return parsed_number


def check_year(age):
    one_hundred = 100
    date = datetime.date.today()
    year = date.year

    year_calculation = (year + one_hundred) - age
    return year_calculation


def main():
    user_name = valid_name_input()
    user_number = valid_number_input()
    year_age = check_year(user_number)

    if user_number == 100:
        print(f'Hello {user_name}, you already are 100 years old!')
    else:
        print(f'Hello {user_name}, you will turn 100 in the year {year_age}')


if __name__ == '__main__':
    main()


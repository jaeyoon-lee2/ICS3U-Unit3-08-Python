#!/user/bin/env python3

# Created by: Jaeyoon
# Created on: Oct 2019
# This program display a leap year


def main():
    # this function display a leap year

    # input
    year_as_string = input("Enter the year (integer): ")

    # process
    try:
        year_as_number = int(year_as_string)
        if year_as_number % 4 == 0:
            if year_as_number % 100 == 0:
                if year_as_number % 400 == 0:
                    print("This year is a leap year!")
                else:
                    print("This year isn't a leap year.")
            else:
                print("This year is a leap year!")
        else:
            print("This year isn't a leap year.")
    except Exception:
        print("It is not an integer")
    finally:
        print("Thanks for playing")


if __name__ == "__main__":
    main()

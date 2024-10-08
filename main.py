"""
Pat S 8/26/24
CIS410 Data Analytics
This is a small program to convert between celcius and fahrenheit, and vice-versa
"""

import os
from time import sleep

import conversion_functions as converters

from art import text2art


def clear_screen(delay: float = 0) -> None:
    sleep(delay)
    os.system("cls" if os.name == "nt" else "clear")


def display_title() -> None:
    print(text2art("Temperature Unit Converter"))


def display_menu() -> None:
    clear_screen()

    display_title()

    print()
    print("1. Fahrenheit to Celcius")
    print("2. Celcius to Fahrenheit")


def main() -> None:
    run = True

    while run:
        display_menu()

        choice = int(input("\nWhich conversion would you like to do?\n"))
        clear_screen()

        temperature = int(input("What is the temperature to be converted?\n"))
        clear_screen()

        if choice == 1:
            converted = converters.fahrenheit_to_celcius(temperature)
            print(f"{temperature} Fahrenheit is {converted} Celcius")

        if choice == 2:
            converted = converters.celcius_to_fahrenheit(temperature)
            print(f"{temperature} Celcius is {converted} Fahrenheit")

        if input('\nContinue? ("y" or "n"\n') != "y":
            run = False
            clear_screen()


if __name__ == "__main__":
    main()

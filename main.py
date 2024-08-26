import os
from time import sleep

import conversion_functions as converters


def clear_screen(delay: float = 0) -> None:
    sleep(delay)
    os.system("cls" if os.name == "nt" else "clear")


def display_title():
    print("Temperature Unit Converter")


def display_menu():
    clear_screen()

    display_title()

    print()
    print("1. Fahrenheit to Celcius")
    print("2. Celcius to Fahrenheit")


def main():
    run = True

    while run:
        display_menu()

        choice = int(input("Which conversion would you like to do?\n"))
        clear_screen()

        temperature = int(input("What is the temperature to be converted?\n"))
        clear_screen()

        if choice == 1:
            converted = round(converters.fahrenheit_to_celcius(temperature))
            print(f"{temperature} Fahrenheit is {converted} Celcius")

        if choice == 2:
            converted = round(converters.celcius_to_fahrenheit(temperature))
            print(f"{temperature} Celcius is {converted} Fahrenheit")

        if input("\nContinue?\n") != "y":
            run = False
            clear_screen()


main()

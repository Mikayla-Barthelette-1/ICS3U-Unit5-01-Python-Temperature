#!/usr/bin/env python3

# Created by: Mikayla Barthelette
# Created on: Oct 2021
# This program converts from celsius to fahrenheit


def calculate_fahrenheit():
    # calculate fahrenheit

    # input
    user_input = input("Enter a temperature (°C): ")

    # process & output
    try:
        celsius = float(user_input)
        fahrenheit = celsius * (9 / 5) + 32
        print("{0}°C is equal to {1}°F.".format(celsius, fahrenheit))
    except Exception:
        print("Invalid input")
    finally:
        print("\nDone.")


def main():
    # this function just calls other functions

    # call functions
    calculate_fahrenheit()


if __name__ == "__main__":
    main()

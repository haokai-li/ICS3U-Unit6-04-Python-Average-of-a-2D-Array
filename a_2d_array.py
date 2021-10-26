#!/usr/bin/env python3

# Created by: Haokai Li
# Created on: Oct 2021
# This Program calculate average of 2d array
import random


def calculated_average(calculate_2d_array):
    # This function calculate average of 2d array
    total_number = 0

    # process
    for calculate_row_number in calculate_2d_array:
        for calculate_columns_number in calculate_row_number:
            total_number += calculate_columns_number
    total_number = total_number / (len(calculate_2d_array) * len(calculate_2d_array[0]))

    return total_number


def main():
    # This function calculate average
    a_2d_array = []
    loop_number_first = 0
    loop_number_second = 0

    # input
    user_row_string = input("How many row would you like: ")
    user_columns_string = input("How many columns would you like: ")
    print("")

    try:
        user_row_number = int(user_row_string)
        user_columns_number = int(user_columns_string)

        # process
        for loop_number_first in range(0, user_row_number):
            columns_numbers = []
            for loop_number_second in range(0, user_columns_number):
                random_number = random.randint(1, 50)
                columns_numbers.append(random_number)
                # output
                print("{} ".format(random_number), end="")
            a_2d_array.append(columns_numbers)
            print("")

        # call functions
        average_number = calculated_average(a_2d_array)
        # output
        print("")
        print("The average of all the number is: {:.2f}".format(average_number))

    except Exception:
        # output
        print("You didn't enter an integer.")


if __name__ == "__main__":
    main()

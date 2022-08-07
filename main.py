# Colby Enbody student #001483980

from trucks import *
from hashtable import *


# Space-Time Complexity: O(N^2)
def time_check():
    print('\nEnter a time in 24 hour format, ie business hours 0800-1700')
    userInputTime = input()
    # checks for valid time input
    # Space-Time Complexity: O(N)
    if 4 > len(userInputTime) > 4:
        print('Please enter a valid time, ie business hours 0800-1700')
        time_check()
    # checks for valid time input
    # Space-Time Complexity: O(N)
    if userInputTime >= '2400' or '-' in userInputTime:
        print('Please enter a valid time, ie business hours 0800-1700')
        time_check()

    # initializes all trucks based on the time specified by the user
    # Space-Time Complexity: O(N^2)
    load_trucks()
    package9_update(userInputTime)
    # Space-Time Complexity: O(N^2)
    set_en_route_truck1(userInputTime)
    # Space-Time Complexity: O(N^2)
    get_delivery_status_at_time_truck1(userInputTime)
    # Space-Time Complexity: O(N^2)
    set_en_route_truck2(userInputTime)
    # Space-Time Complexity: O(N^2)
    get_delivery_status_at_time_truck2(userInputTime)
    # Space-Time Complexity: O(N^2)
    set_en_route_truck3(userInputTime)
    # Space-Time Complexity: O(N^2)
    get_delivery_status_at_time_truck3(userInputTime)
    # Space-Time Complexity: O(N)
    print_all_truck_miles()
    # Space-Time Complexity: O(N)
    all_miles()

    print('\nSelect an option:')
    print('1: Lookup specific package at time specified')
    print('2: Exit Program/Rerun with different time')
    userInput = input()

    # checks user input
    # Space-Time Complexity: O(N)
    if userInput == '2':
        quit()
    # checks user input
    # Space-Time Complexity: O(N)
    elif userInput == '1':
        search_prompt = input("Enter the ID of the package you would like to search for: ")
    try:
        # Searches for package using input
        # Space-time complexity = O(N)
        search_int = int(search_prompt)
        package_lookup_print(search_int)
    except ValueError:
        print("You did not enter an integer for the ID")


time_check()

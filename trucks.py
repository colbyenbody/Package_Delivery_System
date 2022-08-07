from graph import graph
from hashtable import self_adjusting_algorithm
from hashtable import ChainingHashTable, package_hashtable


# Truck class creates objects that will hold the packages on a route
class Truck:

    # initializes truck packages, route, and speed
    def __init__(self):
        self.truck_packages = []
        self.route = []
        self.speed = 0.3

    # Puts package on truck
    # Space-Time Complexity: O(N)
    def insert(self, package):
        self.truck_packages.append(package)
        self.route.append(package[1])

    # Removes package from truck
    # Space-Time Complexity: O(N)
    def remove(self, package):
        self.truck_packages.remove(package)
        self.route.remove(package[1])


# Initialize trucks and addresses
# Space-Time Complexity: O(N)
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()
all_addresses = []
graph.translate_address(package_hashtable)


# load packages onto trucks
# Space-Time Complexity: O(N^2)
def load_trucks():
    for location in graph.adj_list:
        all_addresses.append(location)
    # Manually load trucks
    for address in all_addresses:
        for package in graph.adj_list[address]:
            if package[0] == 1:
                truck1.insert(package)
            if package[0] == 7:
                truck1.insert(package)
            if package[0] == 13:
                truck1.insert(package)
            if package[0] == 14:
                truck1.insert(package)
            if package[0] == 15:
                truck1.insert(package)
            if package[0] == 16:
                truck1.insert(package)
            if package[0] == 19:
                truck1.insert(package)
            if package[0] == 20:
                truck1.insert(package)
            if package[0] == 27:
                truck1.insert(package)
            if package[0] == 29:
                truck1.insert(package)
            if package[0] == 30:
                truck1.insert(package)
            if package[0] == 31:
                truck1.insert(package)
            if package[0] == 34:
                truck1.insert(package)
            if package[0] == 35:
                truck1.insert(package)
            if package[0] == 37:
                truck1.insert(package)
            if package[0] == 40:
                truck1.insert(package)

            if package[0] == 2:
                truck2.insert(package)
            if package[0] == 3:
                truck2.insert(package)
            # test
            if package[0] == 6:
                truck3.insert(package)
            if package[0] == 8:
                truck2.insert(package)
            if package[0] == 11:
                truck2.insert(package)
            if package[0] == 12:
                truck2.insert(package)
            if package[0] == 17:
                truck2.insert(package)
            if package[0] == 18:
                truck2.insert(package)
            # test
            if package[0] == 25:
                truck3.insert(package)
            # test
            if package[0] == 28:
                truck3.insert(package)
            # test
            if package[0] == 32:
                truck3.insert(package)
            if package[0] == 33:
                truck2.insert(package)
            if package[0] == 36:
                truck2.insert(package)
            if package[0] == 38:
                truck2.insert(package)
            if package[0] == 39:
                truck2.insert(package)

            if package[0] == 4:
                truck3.insert(package)
            # test
            if package[0] == 5:
                truck2.insert(package)
            #test
            if package[0] == 9:
                truck2.insert(package)
            if package[0] == 10:
                truck3.insert(package)
            if package[0] == 21:
                truck3.insert(package)
            if package[0] == 22:
                truck3.insert(package)
            if package[0] == 23:
                truck3.insert(package)
            if package[0] == 24:
                truck3.insert(package)
            if package[0] == 26:
                truck3.insert(package)

    # run truck routes through algorithm
    # Space-Time Complexity: O(N^2)
    truck1.route = self_adjusting_algorithm(truck1.route)
    truck1.route.append("4001 South 700 East")
    # Space-Time Complexity: O(N^2)
    truck2.route = self_adjusting_algorithm(truck2.route)
    truck2.route.append("4001 South 700 East")
    # Space-Time Complexity: O(N^2)
    truck3.route = self_adjusting_algorithm(truck3.route)
    truck3.route.append("4001 South 700 East")


# Gets and prints total milage of all trucks
# Space-Time Complexity: O(N)
def print_all_truck_miles():
    print("Truck 1 loaded with", len(truck1.truck_packages), "packages:")
    print(*truck1.truck_packages, sep="\n")
    print("Truck 2 loaded with", len(truck2.truck_packages), "packages:")
    print(*truck2.truck_packages, sep="\n")
    print("Truck 3 loaded with", len(truck3.truck_packages), "packages:")
    print(*truck3.truck_packages, sep="\n")


# Gets the miles traveled for an individual truck
# Space-Time Complexity: O(N)
def miles_traveled(truck_route):
    miles_list = graph.edge_miles
    miles = 0
    for i in range(0, len(truck_route) - 1):
        miles = miles + miles_list[truck_route[i], truck_route[i + 1]]
    return miles


# Gets the total miles traveled by all trucks
# Space-Time Complexity: O(N)
def all_miles():
    miles1 = miles_traveled(truck1.route)
    miles2 = miles_traveled(truck2.route)
    miles3 = miles_traveled(truck3.route)
    total = miles1 + miles2 + miles3
    print("\nTruck 1:    ", round(miles1, 2), "\nTruck 2:    ", round(miles2, 2),
          "\nTruck 3:    ", round(miles3, 2), " \nTotal miles:", round(total, 2))


# Calculates the time it takes to deliver each package on truck 1
# Space-Time Complexity: O(N^2)
def time_tracker():
    miles_between = graph.edge_miles
    distance = 0
    for i in range(0, len(truck1.route) - 1):
        distance = distance + miles_between[truck1.route[i], truck1.route[i + 1]]
        speed = truck1.speed
        minutes = round(distance / speed)
        total_minutes = minutes + 480
        formatted_delivery_time = 'delivered at: ' "%d:%02d" % (divmod(total_minutes, 60))
        time_compare = "%d%02d" % (divmod(total_minutes, 60))
        for package in truck1.truck_packages:
            if truck1.route[i + 1] == package[1]:
                package[8] = formatted_delivery_time


# Calculates the time it takes to deliver each package on truck 2
# Space-Time Complexity: O(N^2)
def time_tracker2():
    miles_between = graph.edge_miles
    distance = 0
    for i in range(0, len(truck2.route) - 1):
        distance = distance + miles_between[truck2.route[i], truck2.route[i + 1]]
        speed = truck2.speed
        minutes = round(distance / speed)
        total_minutes = minutes + 480
        formatted_delivery_time = 'delivered at: ' "%d:%02d" % (divmod(total_minutes, 60))
        for package in truck2.truck_packages:
            if truck2.route[i + 1] == package[1]:
                package[8] = formatted_delivery_time


# Calculates the time it takes to deliver each package on truck 3
# Space-Time Complexity: O(N^2)
def time_tracker3():
    miles_between = graph.edge_miles
    distance = 0
    for i in range(0, len(truck3.route) - 1):
        distance = distance + miles_between[truck3.route[i], truck3.route[i + 1]]
        speed = truck3.speed
        minutes = round(distance / speed)
        total_minutes = minutes + 600
        formatted_delivery_time = 'delivered at: ' "%d:%02d" % (divmod(total_minutes, 60))
        for package in truck3.truck_packages:
            if truck3.route[i + 1] == package[1]:
                package[8] = formatted_delivery_time


# Checks where package is at on truck 1 and changes status to en route if applicable
# Space-Time Complexity: O(N^2)
def set_en_route_truck1(userInputTime):
    miles_between = graph.edge_miles
    distance = 0
    for i in range(0, len(truck1.route) - 1):
        distance = distance + miles_between[truck1.route[i], truck1.route[i + 1]]
        speed = truck1.speed
        minutes = round(distance / speed)
        total_minutes = minutes + 480
        formatted_delivery_time = 'delivered at: ' "%d:%02d" % (divmod(total_minutes, 60))
        time_compare = "0%d%02d" % (divmod(total_minutes, 60))
        dispatch_time = '0800'
        time_input = str(userInputTime)
        test_compare = "{:0>4}".format(time_compare)
        if dispatch_time <= userInputTime <= test_compare:
            status = 'en route'
            for package in truck1.truck_packages:
                if truck1.route[i + 1] == package[1]:
                    package[9] = status


# Gets the time a package was delivered at on truck 1
# Space-Time Complexity: O(N^2)
def get_delivery_status_at_time_truck1(userInputTime):
    miles_between = graph.edge_miles
    distance = 0
    for i in range(0, len(truck1.route) - 1):
        distance = distance + miles_between[truck1.route[i], truck1.route[i + 1]]
        speed = truck1.speed
        minutes = round(distance / speed)
        total_minutes = minutes + 480
        formatted_delivery_time = 'delivered at: ' "%d:%02d" % (divmod(total_minutes, 60))
        time_compare = "0%d%02d" % (divmod(total_minutes, 60))
        dispatch_time = '0800'
        time_input = str(userInputTime)
        test_compare = "{:0>4}".format(time_compare)
        if test_compare <= time_input:
            status = formatted_delivery_time
            for package in truck1.truck_packages:
                if truck1.route[i + 1] == package[1]:
                    package[9] = status


# Checks where package is at on truck 2 and changes status to en route if applicable
# Space-Time Complexity: O(N^2)
def set_en_route_truck2(userInputTime):
    miles_between = graph.edge_miles
    distance = 0
    for i in range(0, len(truck2.route) - 1):
        distance = distance + miles_between[truck2.route[i], truck2.route[i + 1]]
        speed = truck2.speed
        minutes = round(distance / speed)
        total_minutes = minutes + 518
        formatted_delivery_time = 'delivered at: ' "%d:%02d" % (divmod(total_minutes, 60))
        time_compare = "%d%02d" % (divmod(total_minutes, 60))
        dispatch_time = '0800'
        test_compare = "{:0>4}".format(time_compare)
        time_input = str(userInputTime)
        if dispatch_time <= userInputTime <= test_compare:
            status = 'en route'
            for package in truck2.truck_packages:
                if truck2.route[i + 1] == package[1]:
                    package[9] = status


# Gets the time a package was delivered at on truck 2
# Space-Time Complexity: O(N^2)
def get_delivery_status_at_time_truck2(userInputTime):
    miles_between = graph.edge_miles
    distance = 0
    for i in range(0, len(truck2.route) - 1):
        distance = distance + miles_between[truck2.route[i], truck2.route[i + 1]]
        speed = truck2.speed
        minutes = round(distance / speed)
        total_minutes = minutes + 518
        formatted_delivery_time = 'delivered at: ' "%d:%02d" % (divmod(total_minutes, 60))
        time_compare = "%d%02d" % (divmod(total_minutes, 60))
        test_compare = "{:0>4}".format(time_compare)
        dispatch_time = '0800'
        time_input = str(userInputTime)
        if test_compare <= time_input:
            status = formatted_delivery_time
            for package in truck2.truck_packages:
                if truck2.route[i + 1] == package[1]:
                    package[9] = status


# Checks where package is at on truck 3 and changes status to en route if applicable
# Space-Time Complexity: O(N^2)
def set_en_route_truck3(userInputTime):
    miles_between = graph.edge_miles
    distance = 0
    for i in range(0, len(truck3.route) - 1):
        distance = distance + miles_between[truck3.route[i], truck3.route[i + 1]]
        speed = truck3.speed
        minutes = round(distance / speed)
        total_minutes = minutes + 570
        formatted_delivery_time = 'delivered at: ' "%d:%02d" % (divmod(total_minutes, 60))
        time_compare = "%d%02d" % (divmod(total_minutes, 60))
        dispatch_time = '1000'
        time_input = str(userInputTime)
        test_compare = "{:0>4}".format(time_compare)
        if dispatch_time <= userInputTime <= test_compare:
            status = 'en route'
            for package in truck3.truck_packages:
                if truck3.route[i + 1] == package[1]:
                    package[9] = status


# Gets the time a package was delivered at on truck 3
# Space-Time Complexity: O(N^2)
def get_delivery_status_at_time_truck3(userInputTime):
    miles_between = graph.edge_miles
    distance = 0
    for i in range(0, len(truck3.route) - 1):
        distance = distance + miles_between[truck3.route[i], truck3.route[i + 1]]
        speed = truck3.speed
        minutes = round(distance / speed)
        total_minutes = minutes + 570
        formatted_delivery_time = 'delivered at: ' "%d:%02d" % (divmod(total_minutes, 60))
        time_compare = "%d%02d" % (divmod(total_minutes, 60))
        dispatch_time = '1000'
        time_input = str(userInputTime)
        test_compare = "{:0>4}".format(time_compare)
        if test_compare <= time_input:
            status = formatted_delivery_time
            for package in truck3.truck_packages:
                if truck3.route[i + 1] == package[1]:
                    package[9] = status


# Updates package #9 if the user inputs a time at or later than 10:20 am
# Space-Time Complexity: O(N)
def package9_update(userInputTime):
    if str(userInputTime) >= '1020':
        print("\nNew information received on package #9 at 10:20 am, updating package info now")
        for package in truck2.truck_packages:
            if package[7] == "wrong":
                package[1] = '410 S State St'
                package[2] = 'Salt Lake City'
                package[3] = 'UT'
                package[4] = '84111'
                package[5] = '17:00'
                package[6] = '2'
                package[7] = 'wrong'
                package[8] = ''
                package[9] = 'enroute'

                truck2.route = self_adjusting_algorithm(truck2.route)
                truck2.route.append("4001 South 700 East")

        print("Package #9 was updated\n")

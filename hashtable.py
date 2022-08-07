import csv
from graph import graph


# The Chaining Hash Table self adjusts and stores all relevant package data
class ChainingHashTable:

    # Initializes table
    # Space-time complexity = O(1)
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts package into hashtable
    # Space-time complexity = O(N)
    def insert(self, key, package):
        package[0] = int(package[0])
        bucket = key % len(self.table)
        self.table[bucket].append(package)
        if package[7] != "delayed":
            package.append("at hub")
        if package[7] == "delayed":
            package.append("delayed")

    # Search for package via package id
    # Space-time complexity = O(N)
    def search(self, key):
        bucket = key % len(self.table)
        bucket_list = self.table[bucket]

        for package in bucket_list:
            if package[0] == key:
                return package
        return None

    # Removes package via package id
    # Space-time complexity = O(N)
    def remove(self, key):

        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for package in bucket_list:
            if package[0] == key:
                bucket_list.remove(key)


# Extracts data from the csv file that contains packages
# Enters the package data into the hashtable
# Space-time complexity = O(N)
def get_packages(filename):
    hash_pkgs = ChainingHashTable()
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)  # skips the header
        for row in csv_reader:
            hash_pkgs.insert(int(row[0]), row)  # row[0] is the package ID, row is all package information
    return hash_pkgs


package_hashtable = get_packages("packages.csv")


# Prints search result when using package lookup in main
# Space-time complexity = O(N)
def package_lookup_print(id):
    result = package_hashtable.search(id)
    print(result)

    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])

    # Load packages onto truck 1
    # Space-time complexity = O(N)
    def load_truck_one(self):

        truck_1 = [1, 2, 4, 6, 7, 8, 10, 17, 22, 24, 25, 26, 28, 29, 32, 33, 40]

        packages = []
        for package_id in truck_1:
            packages.append(self.search(package_id))
        return packages

    # Load packages onto truck 2
    # Space-time complexity = O(N)
    def load_truck_two(self):

        truck_2 = [3, 13, 14, 15, 16, 18, 19, 20, 30, 34, 36, 37, 38, 39]

        packages = []
        for package_id in truck_2:
            packages.append(self.search(package_id))
        return packages

    # Load packages onto truck 3
    # Space-time complexity = O(N)
    def load_truck_three(self):

        truck_3 = [5, 9, 11, 12, 21, 23, 27, 31, 35]

        packages = []
        for package_id in truck_3:
            packages.append(self.search(package_id))
        return packages


class HashTableEntry:
    def __init__(self, key, item):
        self.key = key
        self.item = item


# Gets list of all packages
# Space-time complexity = O(1)
def get_hash_table():
    return package_hashtable


# I used the greedy algorithm to find the shortest path
# the algorithm find the shortest distance between two points on the route
# Space-time complexity = O(N^2)
def self_adjusting_algorithm(route):
    # this address is the hub trucks start at
    start = "4001 South 700 East"
    graph_edges = graph.edge_miles
    original_route = route
    shortest_path = [start]

    # while loop removes packages as they are added to the shortest_path
    while len(original_route) > 0:
        short = [0, start]
        for location in original_route:
            distance = graph_edges[shortest_path[-1], location]
            if short[0] == 0:
                short = [distance, location]
            if short[0] > distance > 0:
                short = [distance, location]
        # checks if multiple packages at same address
        if short[1] not in shortest_path:
            shortest_path.append(short[1])
        # removes from route and loops
        original_route.remove(short[1])

    # returns optimized path
    return shortest_path

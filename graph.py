import csv


# Creates of graph via the distances csv file
# Contains the distances between all locations
class Graph:

    def __init__(self):
        self.edge_miles = {}
        self.adj_list = {}

    # Add points to graph
    def add_point(self, point):
        self.adj_list[point] = []

    # adds miles between points
    def add_edge(self, point_one, point_two, miles=1.0):
        self.edge_miles[(point_one, point_two)] = miles

    # Match addresses with points on graph
    # Space-Time Complexity: O(N^2)
    def translate_address(self, ht):
        for bucket in ht.table:
            for item in bucket:
                self.adj_list[item[1]].append(item)


# Gets graph data from distance csv file
# Space-Time Complexity: O(N)
def load_distance_csv(filename):
    csv_data = []
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader, None)
        for row in csv_reader:
            csv_data.append(row)
    return csv_data


# Creates graph
# Space-Time Complexity: O(N^2)
def get_graph(filename):
    data = load_distance_csv(filename)
    graph_distances = Graph()
    for row in data:
        graph_distances.add_point(row[1])
    for row in data:
        for i in range(3, len(row)):
            graph_distances.add_edge(row[1], data[i-3][1], float(row[i]))
    return graph_distances

# csv for get graph
graph = get_graph("distances.csv")
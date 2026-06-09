from Station import Station
from heapq import heapify, heappush, heappop

class Graph:
    def __init__(self):
        self.stations = {}  # name -> Station
        self.adj = {}  # name -> list of (neighbor_name, travel_time, line_name)

    def add_station(self, station: Station):
        if station.name not in self.stations:
            self.stations[station.name] = station
            self.adj[station.name] = []

    def add_edge(self, startStation: Station, destStation: Station, travel_time: float, line_name: str = None):
        if startStation.name not in self.stations or destStation.name not in self.stations:
            raise KeyError("Both stations must be added to graph before connecting them")
        self.adj[startStation.name].append((destStation.name, travel_time, line_name))
        self.adj[destStation.name].append((startStation.name, travel_time, line_name)) 

    def get_graph(self):
        for station, neighbors in self.adj.items():
            print(f"{station}: {neighbors}")

    def find_shortest_path(self, start: str, end: str):
        #Initialize the values of all nodes to infinity
        costs = {station: float("inf") for station in self.stations}
        predecessors = {station: None for station in self.stations} # "targetstation" : ("previous station", "Should it need to change line?")
        #set the start station distance to 0
        costs[start] = 0

        current_line = self.adj[start][0][2] if self.adj[start] else None
        print("Current line:", current_line)
        #Initialize the priority queue with the start station
        priority_queue = [(0, start, current_line)]
        heapify(priority_queue)

        #Create a set to hold the visited stations
        visited = set()

        
        while priority_queue:
            current_cost, current_station, current_station_line = heappop(priority_queue)
            # print("\n\nVisiting station:", current_station, "with current cost:", current_cost)
            if current_station == end:
                break
            if current_station in visited:
                continue
            visited.add(current_station)
            
            if current_station_line != current_line:
                # print("Line change detected from", current_line, "to", current_station_line)
                current_line = current_station_line
            
            for neighbor_station, travel_time, line_name in self.adj[current_station]:
                if neighbor_station in visited:
                    continue
                new_cost = current_cost + travel_time
                if new_cost < costs[neighbor_station]:
                    # print("Updating cost for station:", neighbor_station, " ", costs[neighbor_station], "->", new_cost)
                    costs[neighbor_station] = new_cost
                    if line_name != current_line:
                        # print("Line change detected from", current_line, "to", line_name)
                        predecessors[neighbor_station] = (current_station, "Transfer to " + line_name)
                    else:
                        predecessors[neighbor_station] = (current_station, False)                    
                    heappush(priority_queue, (new_cost, neighbor_station, line_name))
        path = []
        current = end
        while current != start and current is not None:
            # print("Current station in path reconstruction:", current)
            path.append(current) 
            if predecessors[current][1] != False: # check if there is a line change between current station and its predecessor
                path.append(predecessors[current][1])  # Add transfer info to path
            current = predecessors[current][0]
        path.append(start)
        path.reverse()
        return {'path':path, 'total_time':costs[end]}
    

    def neighbors(self, station_name: str):
        return list(self.adj.get(station_name, []))

    def get_station(self, name: str):
        return self.stations.get(name)

    def all_station_names(self):
        return list(self.stations.keys())

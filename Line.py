from Station import Station


class Line:
    def __init__(self, name, color=None):
        self.name = name
        self.color = color
        self.stations = []

    def add_station(self, station: Station):
        if station not in self.stations:
            self.stations.append(station)
            station.add_line(self.name)

    def __repr__(self):
        return f"Line(name={self.name}, stations={[s.name for s in self.stations]})"

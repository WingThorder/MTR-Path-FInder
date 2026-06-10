from Exit import Exit
from Platform import Platform
from Floor import Floor
from WalkwaySystem import WalkwaySystem
class Station:
    # def __init__(self, name: str, location: set, platforms: Platform, exits: Exist,walkwaySystems: WalkwaySystem, floorNumber: int):
    #     self.name = name
    #     self.location = location
        
    #     self.floors = [Floor() for _ in range(floorNumber)]

    def __init__(self, name: str, location: set,):
        self.name = name
        self.location = location
        


        
    def __str__(self):
        return f"Station(name={self.name}, location={self.location})"



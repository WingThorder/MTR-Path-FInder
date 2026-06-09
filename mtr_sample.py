from Station import Station
from Graph import Graph


def build_sample_graph():
    g = Graph()

    # Create some sample stations
    AirportExpressLine = [
        Station('AsiaWorld-Expo', (22.32082688360554, 113.94186106137217)),
        Station('Airport', (22.315884174516, 113.93655028747013)),
        Station('Tsing Yi', (22.35852822539444, 114.10760966491186)),
        Station('Kowloon', (22.304288852271057, 114.16140330531891)),
        Station('Hong Kong', (22.28470124515792, 114.15819864115622))
    ]
    
    TungChungLine = [
        Station('Tung Chung', (22.289198595222064, 113.9414390045151)),
        Station('Sunny Bay', (22.33181687377047, 114.02886275729976)),
        Station('Tsing Yi', (22.35852822539444, 114.10760966491186)),
        Station('Lai King', (22.348625405342982, 114.12601715278771)),
        Station('Nam Cheong', (22.326835637738213, 114.15356224822372)),
        Station('Olympic', (22.317807232011607, 114.16009770873396)),
        Station('Kowloon', (22.304288852271057, 114.16140330531891)),
        Station('Hong Kong', (22.28470124515792, 114.15819864115622))
    ]

    DisneylandResortLine = [
        Station('Sunny Bay', (22.33181687377047, 114.02886275729976)),
        Station('Disneyland Resort', (22.31535283756459, 114.04521287222157))
    ]

    TsuenWanLine = [
        Station('Tsuen Wan', (22.3737011094873, 114.11770084777758)),
        Station('Tai Wo Hau', (22.370605667467704, 114.12491062600651)),
        Station('Kwai Hing', (22.36306519998304, 114.13113335160524)),
        Station('Kwai Fong', (22.35699284270759, 114.12821510839846)),
        Station('Lai King', (22.348625405342982, 114.12601715278771)),
        Station('Mei Foo', (22.337583337520243, 114.13808563708463)),
        Station('Lai Chi Kok', (22.337424557266868, 114.14821365861215)),
        Station('Cheung Sha Wan', (22.335598573122883, 114.15572384333552)),
        Station('Sham Shui Po', (22.330835023688547, 114.16220405986829)),
        Station('Prince Edward', (22.32523764508035, 114.16825512355396)),
        Station('Mong Kok', (22.319203339997568, 114.16932800740874)),
        Station('Yau Ma Tei', (22.313049668189127, 114.17057255230576)),
        Station('Jordan', (22.305188454238085, 114.17160252049638)),
        Station('Tsim Sha Tsui', (22.29776356805765, 114.17211750459168)),
        Station('Admiralty', (22.27957688611198, 114.16473606585662)),
        Station('Central', (22.282118398688436, 114.15864208739536))
    ]
    
    
    
    # Add stations to graph
    for station in AirportExpressLine:
        g.add_station(station)
    for station in TungChungLine:
        g.add_station(station)
    for station in DisneylandResortLine:
        g.add_station(station)
    for station in TsuenWanLine:
        g.add_station(station)
    # Add edges (airportExpressLine) with travel times in minutes
    g.add_edge(AirportExpressLine[0], AirportExpressLine[1], 2, "AirportExpressLine")
    g.add_edge(AirportExpressLine[1], AirportExpressLine[2], 13, "AirportExpressLine")
    g.add_edge(AirportExpressLine[2], AirportExpressLine[3], 8, "AirportExpressLine")
    g.add_edge(AirportExpressLine[3], AirportExpressLine[4], 5, "AirportExpressLine")

    # Add edges (TungChungLine) with travel times in minutes
    g.add_edge(TungChungLine[0], TungChungLine[1], 7, "TungChungLine")
    g.add_edge(TungChungLine[1], TungChungLine[2], 6, "TungChungLine")
    g.add_edge(TungChungLine[2], TungChungLine[3], 3, "TungChungLine")
    g.add_edge(TungChungLine[3], TungChungLine[4], 2, "TungChungLine")
    g.add_edge(TungChungLine[4], TungChungLine[5], 2, "TungChungLine")
    g.add_edge(TungChungLine[5], TungChungLine[6], 2, "TungChungLine")
    g.add_edge(TungChungLine[6], TungChungLine[7], 3, "TungChungLine")

    # Add edges (DisneylandResortLine) with travel times in minutes
    g.add_edge(DisneylandResortLine[0], DisneylandResortLine[1], 4, "DisneylandResortLine")

    # Add edges (TsuenWanLine) with travel times in minutes
    g.add_edge(TsuenWanLine[0], TsuenWanLine[1], 2, "TsuenWanLine")
    g.add_edge(TsuenWanLine[1], TsuenWanLine[2], 2, "TsuenWanLine")
    g.add_edge(TsuenWanLine[2], TsuenWanLine[3], 1, "TsuenWanLine")
    g.add_edge(TsuenWanLine[3], TsuenWanLine[4], 1, "TsuenWanLine")
    g.add_edge(TsuenWanLine[4], TsuenWanLine[5], 3, "TsuenWanLine")
    g.add_edge(TsuenWanLine[5], TsuenWanLine[6], 1, "TsuenWanLine")
    g.add_edge(TsuenWanLine[6], TsuenWanLine[7], 2, "TsuenWanLine")
    g.add_edge(TsuenWanLine[7], TsuenWanLine[8], 1, "TsuenWanLine")
    g.add_edge(TsuenWanLine[8], TsuenWanLine[9], 2, "TsuenWanLine")
    g.add_edge(TsuenWanLine[9], TsuenWanLine[10], 1, "TsuenWanLine")
    g.add_edge(TsuenWanLine[10], TsuenWanLine[11], 1, "TsuenWanLine")
    g.add_edge(TsuenWanLine[11], TsuenWanLine[12], 1, "TsuenWanLine")
    g.add_edge(TsuenWanLine[12], TsuenWanLine[13], 2, "TsuenWanLine")
    g.add_edge(TsuenWanLine[13], TsuenWanLine[14], 3, "TsuenWanLine")
    g.add_edge(TsuenWanLine[14], TsuenWanLine[15], 2, "TsuenWanLine")
    return g

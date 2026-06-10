from Station import Station
from Graph import Graph
from Exit import Exit
from Platform import Platform
from WalkwaySystem import WalkwaySystem
def build_sample_graph():
    g = Graph()


    #Stations
    stations = {
        'AWE': Station('AsiaWorld-Expo', (22.32082688360554, 113.94186106137217)),
        'AIR': Station('Airport', (22.315884174516, 113.93655028747013)),
        'TSY': Station('Tsing Yi', (22.35852822539444, 114.10760966491186)),
        'KOW': Station('Kowloon', (22.304288852271057, 114.16140330531891)),
        'HOK': Station('Hong Kong', (22.28470124515792, 114.15819864115622)),
        'TUC': Station('Tung Chung', (22.289198595222064, 113.9414390045151)),
        'SUN': Station('Sunny Bay', (22.33181687377047, 114.02886275729976)),
        'LAK': Station('Lai King', (22.348625405342982, 114.12601715278771)),
        'NAC': Station('Nam Cheong', (22.326835637738213, 114.15356224822372)),
        'OLY': Station('Olympic', (22.317807232011607, 114.16009770873396)),
        'TUM': Station('Tuen Mun', (22.396, 113.973)),
        'SIH': Station('Siu Hong', (22.394, 113.980)),
        'TIS': Station('Tin Shui Wai', (22.385, 114.000)),
        'LOP': Station('Long Ping', (22.380, 114.010)),
        'YUL': Station('Yuen Long', (22.375, 114.020)),
        'KSR': Station('Kam Sheung Road', (22.370, 114.030)),
        'TWW': Station('Tsuen Wan West', (22.365, 114.040)),
        'MEF': Station('Mei Foo', (22.337583337520243, 114.13808563708463)),
        'AUS': Station('Austin', (22.310, 114.160)),
        'ETS': Station('East Tsim Sha Tsui', (22.299, 114.170)),
        'HUH': Station('Hung Hom', (22.337141736784947, 114.17595782666517)),
        'HOM': Station('Ho Man Tin', (22.332092049432852, 114.1686887329794)),
        'TKW': Station('To Kwa Wan', (22.320, 114.170)),
        'SUW': Station('Sung Wong Toi', (22.303, 114.175)),
        'KAT': Station('Kai Tak', (22.290, 114.180)),
        'DIH': Station('Diamond Hill', (22.339990252126178, 114.20180985977402)),
        'HIK': Station('Hin Keng', (22.280, 114.190)),
        'TAW': Station('Tai Wai', (22.373, 114.188)),
        'CKT': Station('Che Kung Temple', (22.385, 114.200)),
        'STW': Station('Sha Tin Wai', (22.382, 114.194)),
        'CIO': Station('City One', (22.380, 114.220)),
        'SHM': Station('Shek Mun', (22.375, 114.225)),
        'TSH': Station('Tai Shui Hang', (22.370, 114.230)),
        'HEO': Station('Heng On', (22.365, 114.235)),
        'MOS': Station('Ma On Shan', (22.360, 114.240)),
        'WKS': Station('Wu Kai Sha', (22.360, 114.240)),
        'TKO': Station('Tseung Kwan O', (22.280, 114.220)),
        'LHP': Station('LOHAS Park', (22.300, 114.256)),
        'HAH': Station("Hang Hau", (22.312, 114.256)),
        'POA': Station("Po Lam", (22.306, 114.256)),
        'LMC': Station('Lok Ma Chau', (22.360, 114.240)),
        'LOW': Station('Lo Wu', (22.365, 114.235)),
        'SHS': Station('Sheung Shui', (22.270, 114.240)),
        'FAN': Station('Fanling', (22.375, 114.225)),
        'TWO': Station('Tai Wo', (22.380, 114.220)),
        'TAP': Station('Tai Po Market', (22.385, 114.215)),
        'UNI': Station('University', (22.386, 114.210)),
        'RAC': Station('Racecourse', (22.388, 114.205)),
        'FOT': Station('Fo Tan', (22.385, 114.200)),
        'SHT': Station('Sha Tin', (22.382, 114.194)),
        'KOT': Station('Kowloon Tong', (22.337141736784947, 114.17595782666517)),
        'MKK': Station('Mong Kok East', (22.320, 114.170)),
        'EXC': Station('Exhibition Centre', (22.280, 114.170)),
        'ADM': Station('Admiralty', (22.27957688611198, 114.16473606585662)),
        'OCP': Station('Ocean Park', (22.246, 114.170)),
        'WCH': Station('Wong Chuk Hang', (22.245, 114.180)),
        'LET': Station('Lei Tung', (22.240, 114.190)),
        'SOH': Station('South Horizons', (22.235, 114.200)),
        'CEN': Station('Central', (22.282118398688436, 114.15864208739536)),
        'TST': Station('Tsim Sha Tsui', (22.29776356805765, 114.17211750459168)),
        'JOR': Station('Jordan', (22.305188454238085, 114.17160252049638)),
        'YMT': Station('Yau Ma Tei', (22.313049668189127, 114.17057255230576)),
        'MOK': Station('Mong Kok', (22.319203339997568, 114.16932800740874)),
        'PRE': Station('Prince Edward', (22.32523764508035, 114.16825512355396)),
        'SSP': Station('Sham Shui Po', (22.288, 114.154)),
        'CSW': Station('Cheung Sha Wan', (22.335598573122883, 114.15572384333552)),
        'LCK': Station('Lai Chi Kok', (22.337424557266868, 114.14821365861215)),
        'MEF': Station('Mei Foo', (22.337583337520243, 114.13808563708463)),
        'KWF': Station('Kwai Fong', (22.35699284270759, 114.12821510839846)),
        'KWH': Station('Kwai Hing', (22.36306519998304, 114.13113335160524)),
        'TWH': Station('Tai Wo Hau', (22.370605667467704, 114.12491062600651)),
        'TSW': Station('Tsuen Wan', (22.3737011094873, 114.11770084777758)),
        'KET': Station('Kennedy Town', (22.283, 114.128)),
        'HKU': Station('HKU', (22.281, 114.137)),
        'SYP': Station('Sai Ying Pun', (22.280, 114.143)),
        'SHW': Station('Sheung Wan', (22.288, 114.154)),
        'WAC': Station('Wan Chai', (22.276, 114.173)),
        'CAB': Station('Causeway Bay', (22.280, 114.180)),
        'TIH': Station('Tin Hau', (22.285, 114.190)),
        'FOH': Station('Fortress Hill', (22.290, 114.200)),
        'NOP': Station('North Point', (22.29127599974312, 114.20148952983655)),
        'QUB': Station('Quarry Bay', (22.287881317735025, 114.2097037926071)),
        'TAK': Station('Tai Koo', (22.280, 114.220)),
        'SWH': Station('Sai Wan Ho', (22.275, 114.230)),
        'SKW': Station('Shau Kei Wan', (22.270, 114.240)),
        'HFC': Station("Heng Fa Chuen", (22.265, 114.250)),
        'CHW': Station("Chai Wan", (22.260, 114.260)),
        'WHA': Station('Whampoa', (22.305093332965345, 114.18981190508516)),
        'SKM': Station('Shek Kip Mei', (22.332092049432852, 114.1686887329794)),
        'LOF': Station('Lok Fu', (22.337968108529115, 114.18705772210006)),
        'WTS': Station('Wong Tai Sin', (22.341707647735852, 114.19398854971472)),
        'DIH': Station('Diamond Hill', (22.339990252126178, 114.20180985977402)),
        'CHH': Station('Choi Hung', (22.33485933452732, 114.20866103406256)),
        'KOB': Station('Kowloon Bay', (22.32322095110888, 114.21394060947887)),
        'NTK': Station('Ngau Tau Kok', (22.315640053454803, 114.21887089715223)),
        'KWT': Station('Kwun Tong', (22.31228735587624, 114.22693567702943)),
        'LAT': Station('Lam Tin', (22.30693548290764, 114.232612949915)),
        'YAT': Station('Yau Tong', (22.29815663245042, 114.2368477026105)),
        'TIK': Station('Tiu Keng Leng', (22.30436458938343, 114.25271551075089)),
        'DIS': Station('Disneyland Resort', (22.312, 114.041)),
    }

    # stations = {
    #     'AWE': Station('AsiaWorld-Expo', (22.32082688360554, 113.94186106137217), [Platform()],[Exist('Exit A', (1,2), None), Exist('Exit B', (6,2), 2)]),
    #     'AIR': Station('Airport', (22.315884174516, 113.93655028747013)),
    #     'TSY': Station('Tsing Yi', (22.35852822539444, 114.10760966491186)),
    #     'KOW': Station('Kowloon', (22.304288852271057, 114.16140330531891)),
    #     'HOK': Station('Hong Kong', (22.28470124515792, 114.15819864115622)),
    #     'TUC': Station('Tung Chung', (22.289198595222064, 113.9414390045151)),
    #     'SUN': Station('Sunny Bay', (22.33181687377047, 114.02886275729976)),
    #     'LAK': Station('Lai King', (22.348625405342982, 114.12601715278771)),
    #     'NAC': Station('Nam Cheong', (22.326835637738213, 114.15356224822372)),
    #     'OLY': Station('Olympic', (22.317807232011607, 114.16009770873396)),
    #     'TUM': Station('Tuen Mun', (22.396, 113.973)),
    #     'SIH': Station('Siu Hong', (22.394, 113.980)),
    #     'TIS': Station('Tin Shui Wai', (22.385, 114.000)),
    #     'LOP': Station('Long Ping', (22.380, 114.010)),
    #     'YUL': Station('Yuen Long', (22.375, 114.020)),
    #     'KSR': Station('Kam Sheung Road', (22.370, 114.030)),
    #     'TWW': Station('Tsuen Wan West', (22.365, 114.040)),
    #     'MEF': Station('Mei Foo', (22.337583337520243, 114.13808563708463)),
    #     'AUS': Station('Austin', (22.310, 114.160)),
    #     'ETS': Station('East Tsim Sha Tsui', (22.299, 114.170)),
    #     'HUH': Station('Hung Hom', (22.337141736784947, 114.17595782666517)),
    #     'HOM': Station('Ho Man Tin', (22.332092049432852, 114.1686887329794)),
    #     'TKW': Station('To Kwa Wan', (22.320, 114.170)),
    #     'SUW': Station('Sung Wong Toi', (22.303, 114.175)),
    #     'KAT': Station('Kai Tak', (22.290, 114.180)),
    #     'DIH': Station('Diamond Hill', (22.339990252126178, 114.20180985977402)),
    #     'HIK': Station('Hin Keng', (22.280, 114.190)),
    #     'TAW': Station('Tai Wai', (22.373, 114.188)),
    #     'CKT': Station('Che Kung Temple', (22.385, 114.200)),
    #     'STW': Station('Sha Tin Wai', (22.382, 114.194)),
    #     'CIO': Station('City One', (22.380, 114.220)),
    #     'SHM': Station('Shek Mun', (22.375, 114.225)),
    #     'TSH': Station('Tai Shui Hang', (22.370, 114.230)),
    #     'HEO': Station('Heng On', (22.365, 114.235)),
    #     'MOS': Station('Ma On Shan', (22.360, 114.240)),
    #     'WKS': Station('Wu Kai Sha', (22.360, 114.240)),
    #     'TKO': Station('Tseung Kwan O', (22.280, 114.220)),
    #     'LHP': Station('LOHAS Park', (22.300, 114.256)),
    #     'HAH': Station("Hang Hau", (22.312, 114.256)),
    #     'POA': Station("Po Lam", (22.306, 114.256)),
    #     'LMC': Station('Lok Ma Chau', (22.360, 114.240)),
    #     'LOW': Station('Lo Wu', (22.365, 114.235)),
    #     'SHS': Station('Sheung Shui', (22.270, 114.240)),
    #     'FAN': Station('Fanling', (22.375, 114.225)),
    #     'TWO': Station('Tai Wo', (22.380, 114.220)),
    #     'TAP': Station('Tai Po Market', (22.385, 114.215)),
    #     'UNI': Station('University', (22.386, 114.210)),
    #     'RAC': Station('Racecourse', (22.388, 114.205)),
    #     'FOT': Station('Fo Tan', (22.385, 114.200)),
    #     'SHT': Station('Sha Tin', (22.382, 114.194)),
    #     'KOT': Station('Kowloon Tong', (22.337141736784947, 114.17595782666517)),
    #     'MKK': Station('Mong Kok East', (22.320, 114.170)),
    #     'EXC': Station('Exhibition Centre', (22.280, 114.170)),
    #     'ADM': Station('Admiralty', (22.27957688611198, 114.16473606585662)
    #             [Platform('Platform 1', 2, 'UP'), Platform('Platform 2', 2, 'DOWN')],
    #             [Exit('A', (1,1,5)),Exit('B', (10,1,5)) ,Exit('C', (20,0,1))],
    #             [WalkwaySystem('E1', (11,1,5), (1,1), None), WalkwaySystem('E2', (12,1,1),None ,(2,5)), WalkwaySystem('L1', (20,1,5), (3,4), None), WalkwaySystem('L2', (20,1,1), None, (1,2))],
    #             5),

    #     'OCP': Station('Ocean Park', (22.246, 114.170)
    #             [Platform('Platform 1', 2, 'UP'), Platform('Platform 2', 2, 'DOWN')],
    #             [Exit('A', (1,1,5)),Exit('B', (10,1,5)) ,Exit('C', (20,0,1))],
    #             [WalkwaySystem('E1', (11,1,5), (1,1), None), WalkwaySystem('E2', (12,1,1),None ,(2,5)), WalkwaySystem('L1', (20,1,5), (3,4), None), WalkwaySystem('L2', (20,1,1), None, (1,2))],
    #             3),
    #     'WCH': Station('Wong Chuk Hang', (22.245, 114.180),
    #             [Platform('Platform 1', 1, 'UP'), Platform('Platform 2', 1, 'DOWN')],
    #             [Exit('A1', (20,0,1)),Exit('A2', (20,0,1)) ,Exit('B', (1,0,10)), Exit('C', (20,0,20))],
    #             [WalkwaySystem('E1', (5,0,5), (1,1), (3,5)), WalkwaySystem('E2', (15,0,5), (3,1),(1,5)), WalkwaySystem('L1', (10,0,5), (2,4), (2,2))],
    #             2),
    #     'LET': Station('Lei Tung', (22.240, 114.190),
    #             [Platform('Platform 1', 0, 'UP'), Platform('Platform 2', 0, 'DOWN')],
    #             [Exit('A1', (10,1,2)),Exit('A2', (10,1,2)) ,Exit('B', (2,1,18))],
    #             [WalkwaySystem('S1', (2,1,3), (1,5), (3,1)), WalkwaySystem('E1', (8,1,3), (3,4),(1,2)), WalkwaySystem('L1', (1,1,1), (1,1), (3,5))],
    #             2),
    #     'SOH': Station('South Horizons', (22.235, 114.200),
    #             [Platform('Platform 1', 0, 'DOWN'), Platform('Platform 2', 0, 'DOWN')],
    #             [Exit('A', (2,1,2)), Exit('B', (2,1,18)), Exit('C', (5,1,5))],
    #             [WalkwaySystem('E1', (3,1,10), (1,1), (1,1)), WalkwaySystem('E2', (4,1,10), (1,1),(1,1)), WalkwaySystem('L1', (2.5,1,10), (1,1), (1,1))],
    #             2),
    #     'CEN': Station('Central', (22.282118398688436, 114.15864208739536)),
    #     'TST': Station('Tsim Sha Tsui', (22.29776356805765, 114.17211750459168)),
    #     'JOR': Station('Jordan', (22.305188454238085, 114.17160252049638)),
    #     'YMT': Station('Yau Ma Tei', (22.313049668189127, 114.17057255230576)),
    #     'MKG': Station('Mong Kok', (22.319203339997568, 114.16932800740874)),
    #     'PED': Station('Prince Edward', (22.32523764508035, 114.16825512355396)),
    #     'SSP': Station('Sham Shui Po', (22.288, 114.154)),
    #     'CSW': Station('Cheung Sha Wan', (22.335598573122883, 114.15572384333552)),
    #     'LCK': Station('Lai Chi Kok', (22.337424557266868, 114.14821365861215)),
    #     'MEF': Station('Mei Foo', (22.337583337520243, 114.13808563708463)),
    #     'KWF': Station('Kwai Fong', (22.35699284270759, 114.12821510839846)),
    #     'KWH': Station('Kwai Hing', (22.36306519998304, 114.13113335160524)),
    #     'TWH': Station('Tai Wo Hau', (22.370605667467704, 114.12491062600651)),
    #     'TSW': Station('Tsuen Wan', (22.3737011094873, 114.11770084777758)),
    #     'KET': Station('Kennedy Town', (22.283, 114.128)),
    #     'HKU': Station('HKU', (22.281, 114.137)),
    #     'SYP': Station('Sai Ying Pun', (22.280, 114.143)),
    #     'SHW': Station('Sheung Wan', (22.288, 114.154)),
    #     'WAC': Station('Wan Chai', (22.276, 114.173)),
    #     'CAB': Station('Causeway Bay', (22.280, 114.180)),
    #     'TIH': Station('Tin Hau', (22.285, 114.190)),
    #     'FOH': Station('Fortress Hill', (22.290, 114.200)),
    #     'NOP': Station('North Point', (22.29127599974312, 114.20148952983655)),
    #     'QUB': Station('Quarry Bay', (22.287881317735025, 114.2097037926071)),
    #     'TAK': Station('Tai Koo', (22.280, 114.220)),
    #     'SWH': Station('Sai Wan Ho', (22.275, 114.230)),
    #     'SKW': Station('Shau Kei Wan', (22.270, 114.240)),
    #     'HFC': Station("Heng Fa Chuen", (22.265, 114.250)),
    #     'CHW': Station("Chai Wan", (22.260, 114.260)),
    #     'WHA': Station('Whampoa', (22.305093332965345, 114.18981190508516)),
    #     'SKM': Station('Shek Kip Mei', (22.332092049432852, 114.1686887329794)),
    #     'LOF': Station('Lok Fu', (22.337968108529115, 114.18705772210006)),
    #     'WTS': Station('Wong Tai Sin', (22.341707647735852, 114.19398854971472)),
    #     'DIH': Station('Diamond Hill', (22.339990252126178, 114.20180985977402)),
    #     'CHH': Station('Choi Hung', (22.33485933452732, 114.20866103406256)),
    #     'KOB': Station('Kowloon Bay', (22.32322095110888, 114.21394060947887)),
    #     'NTK': Station('Ngau Tau Kok', (22.315640053454803, 114.21887089715223)),
    #     'KWT': Station('Kwun Tong', (22.31228735587624, 114.22693567702943)),
    #     'LAT': Station('Lam Tin', (22.30693548290764, 114.232612949915)),
    #     'YAT': Station('Yau Tong', (22.29815663245042, 114.2368477026105)),
    #     'TIK': Station('Tiu Keng Leng', (22.30436458938343, 114.25271551075089)),



    # }
   
   
    # Add stations to graph
    # for station in AirportExpressLine:
    #     g.add_station(station)
    # for station in TungChungLine:
    #     g.add_station(station)
    # for station in DisneylandResortLine:
    #     g.add_station(station)
    # for station in TsuenWanLine:
    #     g.add_station(station)
    # for station in KwunTongLine:
    #     g.add_station(station)
    # for station in TseungKwanOLine:
    #     g.add_station(station)
    # for station in EastRailLine:
    #     g.add_station(station)
    # for station in TuenMaLine:
    #     g.add_station(station)
    # for station in IslandLine:
    #     g.add_station(station)
    for station in stations.values():
        g.add_station(station)
    
    #Add edges (SounthIslandLine) with travel times in minutes
    g.add_edge(stations['ADM'], stations['OCP'], 3, "SIL")
    g.add_edge(stations['OCP'], stations['WCH'], 1, "SIL")
    g.add_edge(stations['WCH'], stations['LET'], 2, "SIL")
    g.add_edge(stations['LET'], stations['SOH'], 1, "SIL")

    # #Add edges (IslandLine) with travel times in minutes
    g.add_edge(stations['KET'], stations['HKU'], 1, "ISL")
    g.add_edge(stations['HKU'], stations['SYP'], 1, "ISL")
    g.add_edge(stations['SYP'], stations['SHW'], 1, "ISL")
    g.add_edge(stations['SHW'], stations['CEN'], 2, "ISL")
    g.add_edge(stations['CEN'], stations['ADM'], 2, "ISL")
    g.add_edge(stations['ADM'], stations['WAC'], 1, "ISL")
    g.add_edge(stations['WAC'], stations['CAB'], 2, "ISL")
    g.add_edge(stations['CAB'], stations['TIH'], 2, "ISL")
    g.add_edge(stations['TIH'], stations['FOH'], 1, "ISL")
    g.add_edge(stations['FOH'], stations['NOP'], 2, "ISL")
    g.add_edge(stations['NOP'], stations['QUB'], 2, "ISL")
    g.add_edge(stations['QUB'], stations['TAK'], 1, "ISL")
    g.add_edge(stations['TAK'], stations['SWH'], 1, "ISL")
    g.add_edge(stations['SWH'], stations['SKW'], 2, "ISL")
    g.add_edge(stations['SKW'], stations['HFC'], 2, "ISL")
    g.add_edge(stations['HFC'], stations['CHW'], 2, "ISL")

    # #Add edges (TuenMaLine) with travel times in minutes
    g.add_edge(stations['TUM'], stations['SIH'], 2, "TML")
    g.add_edge(stations['SIH'], stations['TIS'], 4, "TML")
    g.add_edge(stations['TIS'], stations['LOP'], 3, "TML")
    g.add_edge(stations['LOP'], stations['YUL'], 2, "TML")
    g.add_edge(stations['YUL'], stations['KSR'], 3, "TML")
    g.add_edge(stations['KSR'], stations['TWW'], 6, "TML")
    g.add_edge(stations['TWW'], stations['MEF'], 4, "TML")
    g.add_edge(stations['MEF'], stations['NAC'], 3, "TML")
    g.add_edge(stations['NAC'], stations['AUS'], 2, "TML")
    g.add_edge(stations['AUS'], stations['ETS'], 2, "TML")
    g.add_edge(stations['ETS'], stations['HUH'], 3, "TML")
    g.add_edge(stations['HUH'], stations['HOM'], 1, "TML")
    g.add_edge(stations['HOM'], stations['TKW'], 2, "TML")
    g.add_edge(stations['TKW'], stations['SUW'], 1, "TML")
    g.add_edge(stations['SUW'], stations['KAT'], 1, "TML")
    g.add_edge(stations['KAT'], stations['DIH'], 2, "TML")
    g.add_edge(stations['DIH'], stations['HIK'], 4, "TML")
    g.add_edge(stations['HIK'], stations['TAW'], 2, "TML")
    g.add_edge(stations['TAW'], stations['CKT'], 2, "TML")
    g.add_edge(stations['CKT'], stations['STW'], 2, "TML")
    g.add_edge(stations['STW'], stations['CIO'], 2, "TML")
    g.add_edge(stations['CIO'], stations['SHM'], 1, "TML")
    g.add_edge(stations['SHM'], stations['TSH'], 3, "TML")
    g.add_edge(stations['TSH'], stations['HEO'], 1, "TML")
    g.add_edge(stations['HEO'], stations['MOS'], 2, "TML")
    g.add_edge(stations['MOS'], stations['WKS'], 3, "TML")
    

    # #Add edges (EastRailLine) with travel times in minutes
    g.add_edge(stations['ADM'], stations['EXC'], 1, "EAL")
    g.add_edge(stations['EXC'], stations['HUH'], 3, "EAL")
    g.add_edge(stations['HUH'], stations['MKK'], 4, "EAL")
    g.add_edge(stations['MKK'], stations['KOT'], 2, "EAL")
    g.add_edge(stations['KOT'], stations['TAW'], 3, "EAL")
    g.add_edge(stations['TAW'], stations['SHT'], 1, "EAL")
    g.add_edge(stations['SHT'], stations['FOT'], 2, "EAL")
    g.add_edge(stations['SHT'], stations['RAC'], 8, "EAL")
    g.add_edge(stations['FOT'], stations['UNI'], 3, "EAL")
    g.add_edge(stations['RAC'], stations['UNI'], 8, "EAL")
    g.add_edge(stations['UNI'], stations['TAP'], 5, "EAL")
    g.add_edge(stations['TAP'], stations['TWO'], 2, "EAL")
    g.add_edge(stations['TWO'], stations['FAN'], 5, "EAL")
    g.add_edge(stations['FAN'], stations['SHS'], 2, "EAL")
    g.add_edge(stations['SHS'], stations['LOW'], 3, "EAL")
    g.add_edge(stations['SHS'], stations['LMC'], 7, "EAL")

    # Add edges (airportExpressLine) with travel times in minutes
    g.add_edge(stations['AWE'], stations['AIR'], 2, "AEL")
    g.add_edge(stations['AIR'], stations['TSY'], 13, "AEL")
    g.add_edge(stations['TSY'], stations['KOW'], 8, "AEL")
    g.add_edge(stations['KOW'], stations['HOK'], 5, "AEL")

    # # Add edges (TungChungLine) with travel times in minutes
    g.add_edge(stations['TUC'], stations['SUN'], 7, "TCL")
    g.add_edge(stations['SUN'], stations['TSY'], 6, "TCL")
    g.add_edge(stations['TSY'], stations['LAK'], 3, "TCL")
    g.add_edge(stations['LAK'], stations['NAC'], 2, "TCL")
    g.add_edge(stations['NAC'], stations['OLY'], 2, "TCL")
    g.add_edge(stations['OLY'], stations['KOW'], 2, "TCL")
    g.add_edge(stations['KOW'], stations['HOK'], 3, "TCL")

    # # Add edges (DisneylandResortLine) with travel times in minutes
    g.add_edge(stations['SUN'], stations['DIS'], 4, "DRL")

    # # Add edges (TsuenWanLine) with travel times in minutes
    g.add_edge(stations['TSW'], stations['TWH'], 2, "TWL")
    g.add_edge(stations['TWH'], stations['KWH'], 2, "TWL")
    g.add_edge(stations['KWH'], stations['KWF'], 1, "TWL")
    g.add_edge(stations['KWF'], stations['LAK'], 1, "TWL")
    g.add_edge(stations['LAK'], stations['MEF'], 3, "TWL")
    g.add_edge(stations['MEF'], stations['LCK'], 1, "TWL")
    g.add_edge(stations['LCK'], stations['CSW'], 2, "TWL")
    g.add_edge(stations['CSW'], stations['SSP'], 1, "TWL")
    g.add_edge(stations['SSP'], stations['PRE'], 2, "TWL")
    g.add_edge(stations['PRE'], stations['MOK'], 1, "TWL")
    g.add_edge(stations['MOK'], stations['YMT'], 1, "TWL")
    g.add_edge(stations['YMT'], stations['JOR'], 1, "TWL")
    g.add_edge(stations['JOR'], stations['TST'], 2, "TWL")
    g.add_edge(stations['TST'], stations['ADM'], 3, "TWL")
    g.add_edge(stations['ADM'], stations['CEN'], 2, "TWL")


    # # Add edges (KwunTongLine) with travel times in minutes
    g.add_edge(stations['WHA'], stations['HOM'], 2, "KTL")
    g.add_edge(stations['HOM'], stations['YMT'], 2, "KTL")
    g.add_edge(stations['YMT'], stations['MOK'], 1, "KTL")
    g.add_edge(stations['MOK'], stations['PRE'], 1, "KTL")
    g.add_edge(stations['PRE'], stations['SKM'], 2, "KTL")
    g.add_edge(stations['SKM'], stations['KOT'], 2, "KTL")
    g.add_edge(stations['KOT'], stations['LOF'], 2, "KTL")
    g.add_edge(stations['LOF'], stations['WTS'], 1, "KTL")
    g.add_edge(stations['WTS'], stations['DIH'], 1, "KTL")
    g.add_edge(stations['DIH'], stations['CHH'], 2, "KTL")
    g.add_edge(stations['CHH'], stations['KOB'], 2, "KTL")
    g.add_edge(stations['KOB'], stations['NTK'], 2, "KTL")
    g.add_edge(stations['NTK'], stations['KWT'], 1, "KTL")
    g.add_edge(stations['KWT'], stations['LAT'], 2, "KTL")
    g.add_edge(stations['LAT'], stations['YAT'], 3, "KTL")
    g.add_edge(stations['YAT'], stations['TIK'], 3, "KTL")

    # #Add edges (TseungKwanOLine) with travel times in minutes
    g.add_edge(stations['NOP'], stations['QUB'], 1, "TKL")
    g.add_edge(stations['QUB'], stations['YAT'], 4, "TKL")
    g.add_edge(stations['YAT'], stations['TIK'], 3, "TKL")
    g.add_edge(stations['TIK'], stations['TKO'], 2, "TKL")
    g.add_edge(stations['TKO'], stations['HAH'], 1, "TKL")
    g.add_edge(stations['HAH'], stations['POA'], 2, "TKL")
    g.add_edge(stations['TKO'], stations['LHP'], 4, "TKL")


    return g

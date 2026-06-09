from mtr_sample import build_sample_graph



def print_path(total_time, path):
    if total_time is None:
        print("No path found")
        return
    print(f"Total travel time: {total_time} minutes")
    prev_line = None
    for i, (station, line) in enumerate(path):
        if i == 0:
            print(f"Start at: {station}")
        else:
            if line != prev_line:
                print(f"  Take {line} to {station}")
            else:
                print(f"  Continue to {station}")
        prev_line = line


def main():
    g = build_sample_graph()
    start = 'Tai Wo Hau'
    end = 'Airport'
    result = g.find_shortest_path(start, end)
    print(result)
    # print_path(total_time, path)


if __name__ == '__main__':
    main()

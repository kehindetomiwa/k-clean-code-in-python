location = ["south south", "north west", "south west"]


def display_list(list_d, list_type):
    print(f"select you {list_type} from the list")
    print(f"eg you {1} for {list_d[1]}")
    counter = 1
    for x in list_d:
        print(f"({counter}) {x}")
        counter += 1


display_list(location, 'location')

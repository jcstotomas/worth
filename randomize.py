from random import randint


def create_random_list(file_name):
    list_of_items = []
    with open(file_name) as data:
        for line in data.readlines():
            list_of_items.append(line.strip())

    return list_of_items


def randomize_pair(length_of_list):
    random1 = randint(0, length_of_list-1)
    random2 = randint(0, length_of_list-1)
    while random2 == random1:
        random2 = randint(0, length_of_list)
    return (random1, random2)


def get_pair(random_values, random_list):
    print(random_values)
    return (random_list[random_values[0]], random_list[random_values[1]])


def create_pairs(random_list):
    pair = randomize_pair(len(random_list))
    pair = get_pair(pair, random_list)
    return pair


def run_pairs(random_list):
    pair_list = []
    seen = {}
    for i in range(len(random_list)//2):
        current_pair = create_pairs(random_list)
        seen[i] = current_pair
    return seen

def count_leaf_nodes(input_list):
    if len(input_list) == 0:
        return 0
    else: #LISTA DI n elementi
        counter = 0
        for element in input_list:
            if type(element) == list:
                counter += count_leaf_nodes(element)
            else:
                counter += 1
        return counter

if  __name__ == '__main__':
    names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Barb', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
    print(count_leaf_nodes(names))
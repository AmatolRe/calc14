
def copy_array(source, start_position):
    array1 = []

    for i in range(start_position, len(source)):
        array1 += [source[i]]

    return array1

if __name__ == '__main__':
    print(copy_array([1, 2, 3, 4, 5], 2))

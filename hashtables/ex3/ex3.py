def intersection(arrays):
    """
    YOUR CODE HERE
    """
    my_dict = {}
    result = []

    for array in arrays:
        for i in array:
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1

            if my_dict[i] > 1 and i not in result:
                result.append(i)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))

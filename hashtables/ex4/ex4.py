def has_negatives(a):
    """
    YOUR CODE HERE
    """

    my_dict = {}
    result = []

    for num in a:
        my_dict[num] = 0
        # print(my_dict)
    for num in a:
        if num > 0:
            if num*-1 in my_dict:
                result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

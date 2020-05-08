def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    my_dict = {}
    for i in range(length):
        # my_dict[weights[i]] = i
        if limit - weights[i] in my_dict:
            key = limit - weights[i]
            i2 = my_dict[key]
            return [i, i2]
        my_dict[weights[i]] = i
    return None


weights = [4, 6, 10, 15, 16]

get_indices_of_item_weights(weights, 5, 21)

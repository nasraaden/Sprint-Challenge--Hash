def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    my_dict = {}
    for i in range(length):
        my_dict[weights[i]] = i
    if limit - my_dict[weights[i]] in my_dict:
        return 'logic here'
    else:
        return 'logic here'
    return None


weights = [4, 6, 10, 15, 16]

get_indices_of_item_weights(weights, 5, 21)

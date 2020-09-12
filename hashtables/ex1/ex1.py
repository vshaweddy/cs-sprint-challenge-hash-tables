def get_indices_of_item_weights(weights, length, limit):
    # input is the array of the weights, length of the weights items and the limit
    # create an empty lookup_table
    lookup_table = {}

    for i, weight in enumerate(weights):
        complement = limit - weight

        if complement in lookup_table:
            # return a tuple of integers
            return(i, lookup_table[complement])
        else:
            lookup_table[weight] = i
    return None

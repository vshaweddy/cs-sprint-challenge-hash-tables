def has_negatives(a):
    # convert the array to a set
    lookup_table = {}
    for number in a:
        lookup_table[number] = "a"

    # loop through the set, check if the positive has a negative or not 
    # If yes, append the positive to result
    result = []
    for number in lookup_table:
        if number > 0 and -number in lookup_table:
            result.append(number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

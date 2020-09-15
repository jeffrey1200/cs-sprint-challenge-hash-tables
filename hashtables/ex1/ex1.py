def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    data = {}
    for i in range(len(weights)):
        data[weights[i]] = i

    for i in range(len(weights)):
        difference = limit-weights[i]
        
        if difference in data:
            return (max(i, data[difference]), min(i, data[difference]))

    return None




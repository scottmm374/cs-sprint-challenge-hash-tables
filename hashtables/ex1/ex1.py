

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]


def get_indices_of_item_weights(weights, length, limit):
    weight_dict = {}

    for weight in range(length):
        print()
    #     if weight not in weight_dict:
    #         if length <= 1:
    #             return None
    #         weight_dict = weight

    # return weight_dict


print(get_indices_of_item_weights(weights_4, 9, 10))

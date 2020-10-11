

weights_2 = [4, 4]


def get_indices_of_item_weights(weights, length, limit):
    weight_dict = {}

    for (weight, inx) in enumerate(weights):
        weight_dict[weight] = inx
        # print(weight_dict[weight])
        print(weight_dict)

        # if length <= 1:
        #     return None

        for curr_inx, weight in enumerate(weights):
            weight_dict[weight] = curr_inx
            difference = limit - weight
            print("difference", difference, limit, weight)
            if difference in weight_dict:

                # returning indexes in correct order
                if curr_inx > weight_dict[difference]:
                    return(curr_inx, weight_dict[difference])
                else:
                    return (weight_dict[difference], curr_inx)


answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
# answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(answer_2)

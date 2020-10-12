

weights_2 = [4, 4]


def get_indices_of_item_weights(weights, length, limit):
    weight_dict = {weight: index for index, weight in enumerate(weights)}

    for index, weight in enumerate(weights):
        # weight_dict[weight] = curr_inx
        difference = limit - weight
        # print("difference", difference, limit, weight)
        # (4, 8 4) back

        # Determining order of indexes based on weight
        if difference in weight_dict:
            if index > weight_dict[difference]:
                print("curr_indexinx", index, weight_dict[difference])
                return(index, weight_dict[difference])
            else:
                return (weight_dict[difference], index)


answer_2 = get_indices_of_item_weights(weights_2, 2, 8)
# answer_4 = get_indices_of_item_weights(weights_4, 9, 7)
print(answer_2)

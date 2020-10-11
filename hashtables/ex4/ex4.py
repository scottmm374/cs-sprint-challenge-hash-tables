def has_negatives(a):

    # compare_dict = {}
    result = []
    # neg_dict = {}

    for neg in range(len(a)):
        if a[neg] < 0:
            negative_num = abs(a[neg])

        # TODO its not comparing correctly. Put a neg number in that did not have positive comparison.
            if negative_num not in result:
                result.append(negative_num)

        # if neg not in compare_dict:
        #     compare_dict[negative_num] = neg

    # print(compare_dict)
    print(result)
    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    print(has_negatives([1, 2, 3, -4]))

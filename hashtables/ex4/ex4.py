def has_negatives(a):

    result = []
    neg_dict = {}

    for number in a:

        neg_dict[number] = None

    for number in neg_dict:
        if number > 0 and -number in neg_dict:
            result.append(number)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
    # print(has_negatives([1, 2, 3, -4]))

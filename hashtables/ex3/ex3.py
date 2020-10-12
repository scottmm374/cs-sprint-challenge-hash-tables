import time
# result = [
#     [1, 2, 3],
#     [1, 4, 5, 3],
#     [1, 6, 7, 3]
# ]


def intersection(arrays):

    dict = {}

    target_count = len(arrays)
    intersect = []
    # print(target_count)
    flat = sum(arrays, [])
    # print(flat)
    for num in range(len(flat)):

        # print("num: --->", flat[num])
        if flat[num] not in dict:
            counter = flat.count(flat[num])
            dict[flat[num]] = counter

        if counter == target_count and flat[num] not in intersect:
            intersect.append(flat[num])

    print(intersect)
    return intersect


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))


# intersection(result)
start = time.time()
end = time.time()
print(f"Calculating  {(end - start):.20f} seconds")

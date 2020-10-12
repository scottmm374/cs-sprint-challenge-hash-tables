# Your code here


def finder(files, queries):

    # res = []
    # [res.extend(idx.split("/")) for idx in files]
    # print(res)
    result = []
    for i in range(len(queries)):
        for s in range(len(files)):
            if queries[i] in files[s]:
                result.append(f'{files[s]}')
                # print(files[s])
    # print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'

    ]
    queries = [
        "foo",
        "qux",
        "baz"

    ]
    print(finder(files, queries))

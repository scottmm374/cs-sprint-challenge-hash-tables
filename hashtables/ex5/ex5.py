# Your code here


def finder(files, queries):
    res = []
    [res.extend(idx.split("/")) for idx in files]
    print(res)

    for i in range(len(queries)):
        if queries[i] in res:
            print(queries[i])


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

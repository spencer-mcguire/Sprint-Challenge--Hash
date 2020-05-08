def finder(files, queries):

    # hash the queries as the key and the file path as the value for quick look up
    cache = {}
    results = []

    for q in queries:
        for path in files:
            if q in path:
                cache[q] = path
                files.remove(path)
            

    # print(cache)

    # if my querie is in the cache, add the value to a list 

    for q in queries:
        if q in cache:
            results.append(cache[q])
        else:
            continue
    return results

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

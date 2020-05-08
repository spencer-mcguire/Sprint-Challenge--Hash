def finder(files, queries):

    # hash the queries as the key and the file path as the value for quick look up
    cache = {}
    results = []

    # for q in queries:
    #     if 'nofile' in q:
    #         continue
    #     else:
    #         print(q)
    #         for path in files:
                
    #             if q in path:
    #                 print(q, path)
    #                 cache[q] = path
    # add queries to my cache with some value
    # loop the file paths, if the match a query add that path to the value

    for f in files:
        #slice the path and set the last item as the key in the cache and the path as the value
        key = f.split('/')
        cache.setdefault(key[-1], []).append(f)    

    # if my querie is in the cache, add the value to a list 
    for q in queries:
        if 'nofile' in q:
            continue
        
        if q in cache:

            if len(cache[q]) > 1:

                for i in cache[q]:
                    results.append(i)
            else:
                results.append(cache[q][0])
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
        "nofile223",
        "qux",
        "nofile111",
        "baz"
    ]
    print(finder(files, queries))

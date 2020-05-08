def get_indices_of_item_weights(weights, length, limit):
    cache = {}

    # hash weights first for easy lookup 
    # enumerate to pass index as value
    # for loop the subtraction 
    # limit - place in the loop, look to see if that exists in the hash table and spit out that index as the answer
    for index, v in enumerate(weights):
        cache.setdefault(v, []).append(index)
    for i in weights:
        target = limit - i
        if target in cache:
            if cache[target] > cache[i]:
                if len(cache[target]) > 1 and len(cache[i]) > 1:
                    return (cache[target][0], cache[i][1])
                return (cache[target][0], cache[i][0])
            
            else:
                if len(cache[target]) > 1 and len(cache[i]) > 1:
                    return (cache[i][1], cache[target][0])
                return (cache[i][0], cache[target][0])

    return None


weights_3 = [4, 4]
print(get_indices_of_item_weights(weights_3, 2, 8))
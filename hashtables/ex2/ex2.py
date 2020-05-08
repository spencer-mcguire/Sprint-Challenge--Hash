#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    cache = {}
    route = []
    # loop the tickets to store them in the cache 
    for i in tickets:
        cache[i.source] = i.destination
        # print(cache)
    # start of the trip is always none
    current_value = cache['NONE']
    # loop the provided route
    # add the current val to the route and move to the next
    while len(route) < length:
        route.append(current_value)
        current_value = cache[current_value]

    # for t in cache:
    #     current_value = cache[t]
    #     # print(cache[t])
    #     # print(current_value)
    #     route.append(current_value)

    return route

#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):


    # create a look up table where the key is the start and the destination is the value
    lookup_table = {}
    for ticket in tickets:
        lookup_table[ticket.source] = ticket.destination

    # start with key that is none and put the value into the list using the loop
    current = "NONE"

    # create a route array
    route = []

    while current:
        value = lookup_table[current]
        route.append(value)

        current = value
        # stop until the value is none
        if value == "NONE":
            break

    # return an array of the destinations
    return route

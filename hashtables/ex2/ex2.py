#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticket_dict = {}
    route = []

    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination

    current_dest = ticket_dict["NONE"]
    while current_dest != "NONE":
        route.append(current_dest)
        current_dest = ticket_dict[current_dest]

    route.append(current_dest)

    return route

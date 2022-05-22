#Class objects that contain the information about a certain flight: departure time, arrival time, total travel time, and cost

class Flight:
    def __init__(self, depart, arrive, total, cost):
        self.departureTime = depart
        self.arrivalTime = arrive
        self.totalTime = total
        self.totalCost = cost


    def printDetails(self):
        print("Departure time:", self.departureTime, " Arrival Time:", self.arrivalTime, " Total flight time:", self.totalTime, " Cost of the flight:", self.totalCost)
        



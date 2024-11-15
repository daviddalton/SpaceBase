class Rocket:
    def __init__(self, rocket_id, name, description, active, company, first_flight, boosters, stages, mass):
        self.rocket_id = rocket_id
        self.name = name
        self.description = description
        self.active = active
        self.company = company
        self.first_flight = first_flight
        self.boosters = boosters
        self.stages = stages
        self.mass = mass

    def __str__(self):
        return ("Rocket ID: " + str(self.rocket_id) +
                " Name: " + self.name +
                " Description: " + self.description +
                " Active: " + str(self.active) +
                " Company: " + self.company +
                " First Flight: " + self.first_flight +
                " Boosters: " + str(self.boosters) +
                " Stages: " + str(self.stages) +
                " Mass: " + str(self.mass))

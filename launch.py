def deserialize_launches(launches):
    deserialized_launches = []
    for launch in launches:
        deserialized_launches.append(
            Launch(
                launch['flight_number'],
                launch['mission_name'],
                launch['launch_year'],
                launch['rocket']['rocket_name'],
                launch['launch_site']['site_name']
            )
        )

    return deserialized_launches


class Launch:
    def __init__(self, flight_number, mission_name, launch_year, rocket, launch_site):
        self.flight_number = flight_number
        self.mission_name = mission_name
        self.launch_year = launch_year
        self.rocket = rocket
        self.launch_site = launch_site

    def __str__(self):
        return ("Flight Number: " + str(self.flight_number) +
                " Mission Name: " + self.mission_name +
                " Launch Year: " + str(self.launch_year) +
                " Rocket: " + self.rocket +
                " Launch Site: " + self.launch_site)

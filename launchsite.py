def deserialize_launch_sites(launch_sites):
    deserialized_launch_sites = []
    for launch_site in launch_sites:
        deserialized_launch_sites.append(
            LaunchSite(
                launch_site['site_id'],
                launch_site['name'],
                launch_site['status'],
                launch_site['location']['name'],
                launch_site['attempted_launches'],
                launch_site['successful_launches'],
                launch_site['details'],
                launch_site['site_name_long']
            )
        )

    return deserialized_launch_sites


class LaunchSite:
    def __init__(self, site_id, name, status, location, attempted_launches, successful_launches, details, site_name_long):
        self.site_id = site_id
        self.name = name
        self.status = status
        self.location = location
        self.attempted_launches = attempted_launches
        self.successful_launches = successful_launches
        self.details = details
        self.site_name_long = site_name_long

    def __str__(self):
        return ("Site Id: " + str(self.site_id) +
                " Name: " + self.name +
                " Status: " + self.status +
                " Location: " + self.location +
                " Attempted Launches: " + str(self.attempted_launches) +
                " Successful Launches: " + str(self.successful_launches) +
                " Details: " + self.details +
                " Long Name: " + self.site_name_long)

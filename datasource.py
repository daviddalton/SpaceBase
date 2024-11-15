import requests

from launch import Launch
from launchsite import LaunchSite
from rocket import Rocket


def get_launches():
    url = "https://api.spacexdata.com/v3/launches?order=desc"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            launches = response.json()
            return deserialize_launches(launches)
        else:
            print('Error:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


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


def get_rockets():
    url = "https://api.spacexdata.com/v3/rockets"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            rockets = response.json()
            return deserialize_rockets(rockets)
        else:
            print('Error:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


def deserialize_rockets(rockets):
    deserialized_rockets = []
    for rocket in rockets:
        deserialized_rockets.append(
            Rocket(
                rocket['rocket_id'],
                rocket['rocket_name'],
                rocket['description'],
                rocket['active'],
                rocket['company'],
                rocket['first_flight'],
                rocket['boosters'],
                rocket['stages'],
                rocket['mass']['lb']
            )
        )

    return deserialized_rockets


def get_launch_sites():
    url = "https://api.spacexdata.com/v3/launchpads"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            launch_sites = response.json()
            return deserialize_launch_sites(launch_sites)
        else:
            print('Error:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None


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


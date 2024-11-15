import requests

from launch import deserialize_launches
from launchsite import deserialize_launch_sites
from rocket import deserialize_rockets

LAUNCHES_URL = "https://api.spacexdata.com/v3/launches?order=desc"
ROCKETS_URL = "https://api.spacexdata.com/v3/rockets"
LAUNCH_SITES_URL = "https://api.spacexdata.com/v3/launchpads"


def get_data(url):

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if url == LAUNCHES_URL:
                return deserialize_launches(data)
            elif url == ROCKETS_URL:
                return deserialize_rockets(data)
            elif url == LAUNCH_SITES_URL:
                return deserialize_launch_sites(data)
            else:
                print('Error: not a recognized URL')
        else:
            print('Error:', response.status_code)
            return None

    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

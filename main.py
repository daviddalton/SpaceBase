import datasource


def initialize_launch_data():
    launches = datasource.get_data(datasource.LAUNCHES_URL)
    if launches:
        return launches
    else:
        print('Failed to fetch launches')


def initialize_rocket_data():
    rockets = datasource.get_data(datasource.ROCKETS_URL)
    if rockets:
        return rockets
    else:
        print('Failed to fetch rockets')


def initialize_launch_site_data():
    launch_sites = datasource.get_data(datasource.LAUNCH_SITES_URL)
    if launch_sites:
        return launch_sites
    else:
        print('Failed to fetch launch sites')


def interpret_user_input(user_input):
    if user_input.strip() == "help":
        print('launches                  fetch all launches')
        print('launch {flight_number}    fetch one launch')
        print('rockets                   fetch all rockets')
        print('rocket {rocket_id}        fetch one rocket')
        print('launch_sites              fetch all launch sites')
        print('launch_site {site_id}     fetch one launch site')
    elif user_input.strip() == "launches":
        for launch in launch_data:
            print(launch.__str__())
    elif user_input.__contains__("launch "):
        flight_number = user_input.split(" ")[1].strip()
        print(next((x for x in launch_data if str(x.flight_number) == str(flight_number)), "Launch not found.").__str__())
    elif user_input.strip() == "rockets":
        for rocket in rocket_data:
            print(rocket.__str__())
    elif user_input.__contains__("rocket "):
        rocket_id = user_input.split(" ")[1].strip()
        print(next((x for x in rocket_data if str(x.rocket_id) == str(rocket_id)), "Rocket not found.").__str__())
    elif user_input.strip() == "launch_sites":
        for launch_site in launch_site_data:
            print(launch_site.__str__())
    elif user_input.__contains__("launch_site "):
        launch_site_id = user_input.split(" ")[1].strip()
        print(next((x for x in launch_site_data if str(x.site_id) == str(launch_site_id)), "Launch Site not found.").__str__())
    elif user_input.strip() == "exit":
        return False
    else:
        return True
    return True


launch_data = initialize_launch_data()
rocket_data = initialize_rocket_data()
launch_site_data = initialize_launch_site_data()

print('"help" for suggested commands')

while True:
    if not interpret_user_input(input("~ ")):
        break

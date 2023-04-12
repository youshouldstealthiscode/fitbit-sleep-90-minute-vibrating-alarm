import datetime  # Import datetime module to handle date and time operations.
import time      # Import time module to handle time-related tasks, such as pausing the script.
from fitbit import Fitbit  # Import Fitbit class from fitbit module to interact with the Fitbit API.
import fitbit   # Import fitbit module to handle Fitbit API tasks.

# Replace with your own API credentials.
client_id = "your_client_id"
client_secret = "your_client_secret"
access_token = "your_access_token"
refresh_token = "your_refresh_token"

# Set up Fitbit client using the provided API credentials.
authd_client = Fitbit(client_id, client_secret, oauth2=True, access_token=access_token, refresh_token=refresh_token)

def check_sleep_status():
    today = datetime.datetime.now().strftime('%Y-%m-%d')  # Get the current date in the format 'YYYY-MM-DD'.
    sleep_data = authd_client.get_sleep(today)  # Fetch sleep data for the current date using the Fitbit API.

    last_sleep = sleep_data['sleep'][0]  # Get the most recent sleep record from the fetched sleep data.

    if last_sleep['isMainSleep']:  # Check if the fetched sleep record is the main sleep (longest sleep) for the day.
        sleep_start = last_sleep['startTime']  # Get the start time of the sleep session.
        start_time = datetime.datetime.strptime(sleep_start, '%Y-%m-%dT%H:%M:%S.%f%z')  # Convert the sleep start time string to a datetime object.

        current_time = datetime.datetime.now(datetime.timezone.utc)  # Get the current time in UTC timezone.
        sleep_time_diff = (current_time - start_time).total_seconds() / 60  # Calculate the time difference between sleep start time and current time in minutes.

        # We assume the user is asleep if they started sleeping at least 5 minutes ago.
        if 5 <= sleep_time_diff < 10:  
            return True  # Return True if the user is asleep.

    return False  # Return False if the user is not asleep.

def set_alarm_90_min_later():
    current_time = datetime.datetime.now()  # Get the current local time.
    alarm_time = current_time + datetime.timedelta(minutes=90)  # Calculate the time 90 minutes from now.

    alarm_time_formatted = alarm_time.strftime('%H:%M')  # Format the calculated alarm time as 'HH:MM'.

    devices = authd_client.get_devices()  # Get a list of user's Fitbit devices using the Fitbit API.

    # Loop through each device in the list.
    for device in devices:
        if device['type'] == 'WATCH':  # Check if the device is a watch.
            tracker_id = device['id']  # Get the ID of the watch.
            # Set an alarm for the watch 90 minutes later, with a recurring type and a wakeup purpose.
            authd_client.create_alarm(tracker_id, alarm_time_formatted, "recurring", "WAKEUP")

# Continuously check for user sleep status and set an alarm when they're asleep.
while True:
    if check_sleep_status():  # Check if the user is asleep.
        set_alarm_90_min_later()  # Set an alarm for 90 minutes after falling asleep.
        print("Alarm set for 90 minutes after falling asleep.")  # Print a message to indicate an alarm has been set.
        break  # Break the loop once the alarm has been set.
    else:
        time.sleep(300)  # Pause the script for 300 seconds (5 minutes) before checking sleep

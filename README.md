# fitbit sleep 90 minute vibrating alarm

To create a Python program that interacts with the Fitbit API to monitor user sleep and set an alarm for 90 minutes after falling asleep, you will need to use the Python Fitbit package. You can install it with:

`pip install python-fitbit`

Before proceeding, make sure you have the necessary credentials (client_id, client_secret, and access_token). Follow the instructions at https://towardsdatascience.com/collect-your-own-fitbit-data-with-python-ff145fa10873 or https://dev.fitbit.com/getting-started/ to set up your Fitbit API credentials.

This program checks the user's sleep status every 5 minutes. If the user is determined to be asleep, it sets an alarm for 90 minutes later. Note that this code assumes that the user falls asleep at least 5 minutes after the sleep start time returned by the Fitbit API.

Keep in mind that the Fitbit API has rate limits, so be cautious with the frequency of requests. You may want to adjust the sleep interval or check sleep status less frequently.

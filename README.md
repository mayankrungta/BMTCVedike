ABOUT

BTMCVedike is an app to help ease the life of bus commuters in Bangalore. It provides the various bus routes, fairs, schedules, etc.

We also hope to provide live updates for the various buses/stops. It helps to know when the bus next desired bus is going to arrive or where I am on my route.

This is an open source project supported by FIELDSofVIEW(http://fieldsofview.in/).


GET STARTED

# Set the environment
$ pip install -r requirements.txt

###
# Begin the crawls
###

# Fetch all the BMTC data
$ python bmtc_fetch.py TestSuite.test_fetch_bmtc_data

# Fetch only timetable details and selectively download bus routes
$ python bmtc_fetch.py TestSuite.test_fetch_timetable_details 

Note: Logs can be diverted to {REPO_DIR}/logs


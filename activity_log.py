import json
import os
from datetime import datetime
from ctypes import Structure, windll, c_uint, sizeof, byref 

json_file="activity_log.json" # Path to the JSON file

# Get the current time as a string
def current_time_str():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S") 

# Get the current date as a string
def current_day_str():
    return datetime.now().strftime("%Y-%m-%d")

# Categorize the application name into different categories
def categorize(name):
    name=name.lower()
    if "chrome" in name or "firefox" in name or "edge" in name:
        return "browser"
    elif "code" in name or "pycharm" in name:
        return "coding"
    elif "word" in name or "excel" in name:
        return "office"
    elif "zoom" in name or "teams" in name:
        return "meeting"
    elif "spotify" in name or "youtube" in name:
        return "media"
    else:
        return "other"

# Get the active window title
def detect_app_type(name):
    if any(browser in name.lower() for browser in ["chrome", "firefox", "edge"]):
        return "website"
    return "desktop"

# Create the log entry
def log_activity(activity_name,start_time,end_time, duration, window_title,idle_time=0):

    entry={
        "activity_name": activity_name,
        "start_time": start_time,
        "end_time": end_time,
        "seconds": duration,
        "minutes": duration // 60,
        "window_title": window_title,
        "category": categorize(activity_name),
        "app_type": detect_app_type(activity_name),
        #"idle_time": idle_time
    }

    if os.path.exists(json_file): # Check if the JSON file exists
        with open(json_file, "r") as file:# Open the file in read mode
            # Load the existing data from the JSON file
            data=json.load(file)
    else:
        data=[]# Create an empty list if the file doesn't exist

    data.append(entry) # Append the new entry to the existing data

    # Write the updated data back to the JSON file
    with open(json_file,"w") as file: # Open the file in write mode
        json.dump(data, file, indent=4) # Write the data to the file with indentation for readability

    print(f"Activity Logged:{entry["activity_name"]} ({duration}s)")
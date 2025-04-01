import win32gui
import time
import re # Import the required libraries
from datetime import datetime
from activity_log import log_activity, current_time_str

def get_active_window_title():
    window=win32gui.GetForegroundWindow()
    return win32gui.GetWindowText(window)

def extract_website_from_title(title):
    #try to extract the website name from the browser title format
    match=re.search(r'(.+) - (Google Chrome|Mozilla Firefox|Microsoft Edge)', title) # Regular expression to match the title format
    
    # If the title matches the expected format, extract the website name
    # and return it without the browser name
    if match:
        return match.group(1).strip(1)
    return None

# Initial active window title
active_window = get_active_window_title()

start_time=time.time()# Get the current time
start_time_str=current_time_str()

print("Activity tracking started...\n")

try:# Start an infinite loop to track the active window
    while True:
        current_window = get_active_window_title()
        website = extract_website_from_title(current_window)

        if current_window != active_window:
            end_time = time.time()
            duration = int(end_time - start_time)

            activity_name = extract_website_from_title(active_window) or active_window

            log_activity(
                activity_name=activity_name,
                start_time=start_time_str,
                end_time=current_time_str(),
                duration=duration,
                window_title=active_window
            )

            active_window = current_window
            start_time = time.time()
            start_time_str = current_time_str()


        time.sleep(2)

except KeyboardInterrupt:
    print("\n🛑 Tracking stopped.")
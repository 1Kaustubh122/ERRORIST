import pyautogui as pgi
import webbrowser
import time
from Meet_link_gen import meet_link_gen

meet_url = meet_link_gen()

def input_time():
    time_input = input("Enter Your Time with AM/PM: ").upper()

    if "PM" in time_input:
        hrs, min = map(int, (time_input[:-2].split(":")))
        if min < 10:
            min = (f"0{str(min)}")
        opening_time = (f"{hrs + 12}:{min}:00")
    else:
        hrs, min = map(int, (time_input[:-2].split(":")))
        if min < 10:
            min = (f"0{str(min)}")
        opening_time = (f"{hrs}:{min}:00")

    return opening_time

opening_time = input_time()


def Share_Meet_Details():
    return meet_url

print("\nYour Opening Time is set to : ", opening_time)

time.sleep(5)

Current_Time = time.strftime("%H:%M:%S")

while Current_Time != opening_time:
    print(Current_Time)
    Current_Time = time.strftime("%H:%M:%S")
    time.sleep(1)

if Current_Time == opening_time:
    webbrowser.open(meet_url)

time.sleep(5) # # Wait for page to load
pgi.click(1150, 661) # # Will click in join meet
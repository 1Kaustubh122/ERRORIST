import pyautogui
import webbrowser
import time
from pandas.io.clipboard import clipboard_get

def meet_link_gen():
    google_meet_link = "https://meet.google.com/"
    webbrowser.open(google_meet_link)

    time.sleep(4) # # Wait for page to load
    pyautogui.click(214, 734)   # # Will click on New Meeting
    time.sleep(2) # # Wait for page to load
    pyautogui.click(214, 734)  # # Will click on Create a meeting for later
    time.sleep(3)  # # Wait for page to load
    pyautogui.click(985, 675) # # Will click on copy to clipboard

    link = clipboard_get() # # Will access the link from the clipboard

    return link


# print(pyautogui.position())

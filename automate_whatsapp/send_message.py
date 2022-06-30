import pywhatkit as pwk
import time
import pyautogui
from tkinter import *
from time_test import message_time_dict
 
# using Exception Handling to avoid unexpected errors
try:
     # sending message in Whatsapp in India so using Indian dial code (+91)
     msg=message_time_dict()
     print(msg)
     win = Tk()
     screen_width = win.winfo_screenwidth()
     screen_height= win.winfo_screenheight()
     print(screen_width, screen_height)
     pwk.sendwhatmsg("+33670513920", msg["message"], 18, 44)
     # pwk.sendwhatmsg("+33670513920", msg["message"], int(msg["hh"]), int(msg["mm"]))
     pyautogui.moveTo(screen_width * 0.694, screen_height* 0.964)
     pyautogui.click()
     pyautogui.press('enter')
 
     print("Message Sent!") #Prints success message in console
 
     # error message
except: 
     print("Error in sending the message")







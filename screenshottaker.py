import pyautogui
from tkinter import *
import os
import datetime

print("Current working directory:", os.getcwd())

#this part is to create  window
win=Tk()
win.title("Screenshot taker")
win.geometry("500x500")
win.config(bg="lightblue")

entry=Entry(win,font=('Time New Roman',30))
entry.place(x=20,height=50,width=460,y=50)

folder = "SS"
os.makedirs(folder, exist_ok=True)

# Generate a unique filename using current date and time
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"screenshot_{timestamp}.png"
filepath = os.path.join(folder, filename)

# Take screenshot and save it
screenshot = pyautogui.screenshot()
screenshot.save(filepath)
print(f"Screenshot saved as {filepath}")

def take_ss():
   folder=entry.get()
   #create folder if it doesn't exist
   if not os.path.exists(folder):
      os.makedirs(folder)
   path=os.path.join(folder,"test.png")
   print(path)
   screenshot=pyautogui.screenshot()# captures the screen
   screenshot.save(path)
   #checks whether the screenshot was saved successfully
   if os.path.exists(path):
       print("Screenshot saved successfully at:", path)
   else:
       print("Failed to save screenshot.")

button= Button(win,text="Done",font=('Time New Roman',30),command=take_ss)
button.place(x=50,y=100,height=100,width=300)

win.mainloop()
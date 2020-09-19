import win32api
import win32con
import time
import ctypes

key_map = {
    "0": 49, "1": 50, "2": 51, "3": 52, "4": 53, "5": 54, "6": 55, "7": 56, "8": 57, "9": 58,
    "A": 65, "B": 66, "C": 67, "D": 68, "E": 69, "F": 70, "G": 71, "H": 72, "I": 73, "J": 74,
    "K": 75, "L": 76, "M": 77, "N": 78, "O": 79, "P": 80, "Q": 81, "R": 82, "S": 83, "T": 84,
    "U": 85, "V": 86, "W": 87, "X": 88, "Y": 89, "Z": 90
}

def key_press(num,duration=0.2):
    MapVirtualKey=ctypes.windll.user32.MapVirtualKeyA
    time.sleep(0.4)
    win32api.keybd_event(num,MapVirtualKey(num,0),0,0)
    time.sleep(duration)
    win32api.keybd_event(num,MapVirtualKey(num,0),win32con.KEYEVENTF_KEYUP,0)

wait_time=input('Please input the waiting time (seconds):')
print('This script will wait 2s for u changing the focus to the game')
time.sleep(2)
print('Pressed e')
key_press(key_map['E'])
print('Pressed enter')
key_press(13)   #press enter
time.sleep(3.7)
print('start waiting')
time.sleep(float(wait_time))
print('Pressed s')
key_press(key_map['S'])
print('Let\'s see ~')

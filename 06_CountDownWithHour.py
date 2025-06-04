import time
import winsound

hours = int(input("Enter Hours : "))
minutes = int(input("Enter Minutes : "))
seconds = int(input("Enter Seconds : "))

total_seconds = hours*3600 + minutes*60 + seconds

while total_seconds > 0:
    hrs = total_seconds//3600
    mins = (total_seconds%3600)//60
    secs = total_seconds%60   
    print(f"{hrs:02d}:{mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)
    total_seconds -= 1

print("Time's up!")
winsound.Beep(1000, 1000)  
import time
import winsound

seconds = int(input("Enter time in seconds: "))

while seconds > 0:
    mins = seconds//60
    secs = seconds%60   
    # or simply use the divmod method:- mins, secs = divmod(seconds, 60)
    print(f"{mins:02d}:{secs:02d}", end="\r")
    time.sleep(1)
    seconds -= 1

print("Time's up!")
winsound.Beep(1000, 1000) 
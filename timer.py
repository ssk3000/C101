import time

def countdown(seconds):
    while seconds>0:
        sec = int(seconds%60)
        min = int(seconds/60)
        print(f"{min}:{sec}")
        time.sleep(1)
        seconds -= 1
    if min == 0 and sec == 0:
        print("Time is up")

seconds = int(input("How many seconds? "))   
countdown(seconds)
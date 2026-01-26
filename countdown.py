#Program to make a COUNTDOWN Timer for given time.

import time

total_time = int(input("Enter the time in seconds : "))

for x in range (total_time, -1, -1):
   seconds = x%60
   minutes = int(x/60)%60
   hours = int(x/3600)
   print(f"{hours:02}:{minutes:02}:{seconds:02}")
   time.sleep(1)
print("TIME IS UP!!")
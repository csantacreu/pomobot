
from datetime import datetime
import time

def countdown(inp_mnts):
    rem_tm = (60 * inp_mnts)
    while rem_tm:
        time.sleep(1)
        rem_tm -= 1
        print(rem_tm)

# Input work time, rest time (and cycles)

# Start work countdown

countdown(0.5)

# print(datetime.now())

# Add 25 to it

# When second time, send message(print)

# When accepted, start 5 mnts

# When 5 mnts pass, send message

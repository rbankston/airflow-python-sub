import time
import sys

maybe_fail = round(time.time() * 1000)

if maybe_fail % 5 == 0:
    for count in range(60):
        print(time.ctime())
        time.sleep(5)
else :
    for count in range(50):
        print(time.ctime())
        time.sleep(5)

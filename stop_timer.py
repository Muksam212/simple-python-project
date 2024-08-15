#simply stop timer project using the time module

import time

print("Press Enter To Start, Press Ctrl+C To Stop")

while True:
    try:
        input()
        print("Started")
        begin = time.time()
    except KeyboardInterrupt:
        print("Stopped")
        end = time.time()
        print("Total time taken: ", round(end - begin, 2),'secs')
        break
import time
print("Seconds since January 1, 1970:", f"{time.time():,}", end='')
print(" or", "{:0.2e}".format(time.time()), "in scientific notation")
print(time.strftime("%B %d %Y"))
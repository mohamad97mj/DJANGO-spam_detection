import time


def elements():
    for j in range(0, 4):
        # simulate a slow search
        time.sleep(5)
        yield (j)


print("start")
for i in elements():
    # show a "console style" progress bar  :)
    print(".", end="", flush=True)
print()
print("end")

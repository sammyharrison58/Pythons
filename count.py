import time


def count(start, end):
    for number in range(start, end + 1):
        print(number)
        time.sleep(1)


print("------Counting from 1 to 10:--------")
count(1, 10)
print("-----All done------")

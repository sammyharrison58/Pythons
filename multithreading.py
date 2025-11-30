import threading
import time


def walk_around():
    for _ in range(5):
        print("Walking around...")
        time.sleep(2)


def drink_water():
    for _ in range(5):
        print("Drinking water...")
        time.sleep(5)


def get_mail():
    for _ in range(2):
        print("Getting mail...")
        time.sleep(6)


walk_around()
drink_water()
get_mail()
cr1 = threading.Thread(target=walk_around, args="kampala")
cr2 = threading.Thread(target=drink_water)
cr3 = threading.Thread(target=get_mail)
cr1.join()
cr2.join()
cr3.join()
print("All tasks completed.")

db = {}
print("This is Database")
while True:
    print("What do you please!")
    print("Enter P to [p]ut,G to [G]et or L to [L]ist")
    print("Or  enter Q to [Q]uit")
    action = input()
    if action == "P".upper():
        k = input("enter a key:")
        d = input("enter data:")
        db[k] = d
    elif action == "G".upper():
        k = input("Enter key:")
        if not k in db:
            print("No such key:")
        else:
            print("Your data:%s" % db[k])
    elif action == "L".upper():
        print("DB contents:")
        print(db)
    elif action == "Q".upper():
        print("Bye")
        break

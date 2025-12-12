def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles!")
        return func(*args, **kwargs)

    return wrapper


def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge!")
        return func(*args, **kwargs)

    return wrapper


@add_sprinkles
@add_fudge
def make_ice_cream(flavor):
    print("Making ice cream.")


make_ice_cream("vanilla")
print("here is your{flavor} ice cream!".format(flavor=" vanilla"))

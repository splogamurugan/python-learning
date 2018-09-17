spam=100
def eggs_local():
    # global spam
    spam=200

def eggs_global():
    global spam
    spam=300

eggs_local()

print spam

eggs_global()

print spam


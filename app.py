import os

print("Path exists %s" % os.path.exists("output"))

os.system("nikola serve output")

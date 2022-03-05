import os

def set_timezone():
    os.system("tzutil /s \"Eastern Standard Time\"")

set_timezone()
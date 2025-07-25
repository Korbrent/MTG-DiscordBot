from config import VERBOSITY

NORMAL = 0
ERROR = 1
DEBUG = 2

"""
Prints the message according to a verboseness setting
Verboseness values (feel free to adjust the scale. Not set in stone yet.)
    -1  ->  None
     0  ->  Normal print-outs & Urgent 
     1  ->  Errors
     2  ->  Debugging
"""
def vprint(verbosity: int, *args, **kwargs):
    if verbosity <= VERBOSITY:
        print(*args, **kwargs)

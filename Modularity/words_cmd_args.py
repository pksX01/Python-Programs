# this file demonstrates...
# 1. command line args.
# 2. doc strings
# 3. documenting code with comments

# Command line arguments..
#  To show execution..
#  type following in REPL
#  from words_cmd_args import *
#  main("Accenture")
# module level doc string should appear as the first statement in .py file
# doc strings are enclosed within """ and """
# show the execution from REPL ...
# write:
#  import words_cmd_args
#  help(words_cmd_args)

"""
This module takes argument from REPL or commnand prompt and prints it on the
screen through for-loop
"""

import sys
def printwords(items):
    """ This function prints argument by iterating through for loop.

    Args:
        It takes one argument which could be a simple string.

    Returns:
         Nothing

    """
    
    for eachitem in items:
        print(eachitem)

def main(argument):
    """ This function calls printwords.
    Args:
        1 argument needed
    """
   
    printwords(argument)
    print(sys.argv[0]) # it will print module name with it entire path on your HDD.
    
if __name__ == '__main__':
    main(sys.argv[1]) #sys.argv[0] refers to module name
    


#Instructions:

# 1. Write only statements without def line and execute
# 2. Write with def and show execution
# 3. Show execution by importing module
# 4. show execution by writing __names__
#    on REPL ...write : import words and show the output
# 5. on REPL again write : import words and show that there is no output because
#    print(__name__) will not be executed since module code is executed
#    only once during the first import
# 6. Locate python.exe on your machine.
#    Show the execution thru command promt. write : python words.py
#    it will print __main__
# 7. now write down if statement for calling printwords and show the execution
#    from command prompt.

def printwords():
    words = ["C","C++","VC++","Python",".NET","JAVA"]
    for eachword in words:
        print(eachword)

def main():
    printwords()
    
if __name__ == '__main__':
    main()

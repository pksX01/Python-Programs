def printme(str):
    print(str)
    return;

def changeme(mylist):
    mylist.append([1,2,3,4])
    print ("Value inside the function:",mylist)
    return;

#parameter mylist is local to the function and changing
#mylist within the function doesn't change mylist
def changemeagain(mylist):
    mylist=[1,2,3,4]
    print("Values inside function:",mylist)
    return;

#function arguments - Required Arguments

#Required arguments are the arguments passed to a function
#in correct positional order. Here, the number of arguments
#in the function call should match exactly with the function
#definition.

#function arguments - Keyword Arguments

def printinfo(name,age):
    print ("Name: ",name)
    print ("Age: ",age)
    return;
#function can be called as printinfo(age=50,name="Vinay")
#order of arguments while calling doesn't matter

#function arguments - Default Arguments

def printinfodefault(name,age=55):
    print ("Name: ",name)
    print ("Age: ",age)
    return;

#function can be called as printinfodefault(age=50,name="Vinay")
#OR
#printinfodefault(name="Vinay")

#Variable-length arguments

#You may need to process a function for more arguments than
#you specified while defining the function. These arguments
#are called variable-length arguments and are not named in
#the function definition, unlike required and default
#arguments.


#General Syntax
#def functionname([formal_args,] *var_args_tuple ):
 #  "function_docstring"
  # function_suite
   #return [expression]

def printinfovariablearg(arg1,*vartuple):
    print("Output is : ")
    print (arg1)
    for var in vartuple:
        print (var)
    return;

#printinfovariablearg( 10 )
#printinfovariablearg( 70, 60, 50 )


#Anonymous functions

#These functions are called anonymous because they are not declared in
#a standard manner by using the def keyword.

#you can use lamda keyword  to create small anonymous functions.

#Lambda forms can take any number of arguments but return just one
#value in the form of an expression. They cannot contain commands or
#multiple expressions.

#An anonymous function cannot be a direct call to print because lambda
#requires an expression

#Although it appears that lambda's are a one-line version of a function,
#they are not equivalent to inline statements in C or C++,

#general syntax

#lambda [arg1 [,arg2,.....argn]]:expression

sum=lambda arg1,arg2:arg1+arg2

#another example of lambda
foo=[2,18,9,22,17,24,8,12,27]
list(map(lambda x:x*2,foo)) #apply lambda code on every element in foo
list(filter(lambda x:x%3==0,range(2,100)))
list(filter(lambda x:x%3==0,foo))



#returning a value from a function
#local and global scope
total=0 #global variable
def add(arg1,arg2):
    total=arg1+arg2 #total is local to function
    print("Inside function total=",total)
    return total


#named variables
def printnamedparam(**params):
    print(params)
#call will be : printnamedparam(x=1,y=2,z=3)

#mix of all types
def print_params_4(x, y, z=3, *pospar, **keypar):  
     print (x, y, z) 
     print (pospar)
     print (keypar)

#call will be : print_params_4(1,2,4,5,6,7,8,a=1,b=2)

#modify global variable
money=2000 #global variable
def addmoney():
    global money #for modifying global var this statement is necessary. Skipping this statement will give an error saying variable money referenced before assignment.
    money=money+1
    a=5
    print(locals()) # to list everything that a function can access locally.return value is dict
    print(globals())# to list everything that a function can access globally. return value is dict
    

#refer to d:\Phones for importing package or folder

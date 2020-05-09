#Data Hiding

class JustCounter:
   __secretCount = 0 #not visible outside the class. precede with __
  
   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
print (counter.__secretCount) # Disable below statement and enable this. This statement will not work because __secretCount will not work outside the class.
#print(counter._JustCounter__secretCount) #disable the above statement and enable this
        


def division(a,b):
	try:
		print ("a value is ", a, "b value is", b, " condition check b != 1" , b != 1)	
		if (b != 1):
			return a/b
		else:
			raise IOERROR
	except ZeroDivisionError:
		return '0 division is not possible'
	except Exception:
		return "Why are you wasting my time? don't you know the result"

print (division (2,4))
print (division (4,1))
print (division (2,0)) 
 

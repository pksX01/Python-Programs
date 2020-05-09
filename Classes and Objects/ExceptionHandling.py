Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    1/0
ZeroDivisionError: division by zero
>>> x={1:2,2:3}
>>> x[3]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    x[3]
KeyError: 3
>>> b
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> try :
	1/0
except:
	print('default exeception')

	
default exeception
>>> try :
	print(b)

except:
	print('default exeception')

	
default exeception
>>> try :
	1/0
except ZeroDivisionError as e :
	print(e)

	
division by zero
>>> try :
	print(b)
except NameError as e :
	print(e)

	
name 'b' is not defined
>>> try :
	print(x[3])
except KeyError as e :
	print(e)

	
3
>>> try :
	print(b)
except KeyError as e :
	print(e)
except IndexErroras err :
	
SyntaxError: invalid syntax
>>>  try :
	print(b)
except KeyError as e :
	print(e)
	
SyntaxError: unexpected indent
>>> try:
	print(b)
except KeyError as e:
	print(e)
except IndexError as err:
	print(err)
except:
	print('Unknown error')

	
Unknown error
>>> try:
	print(x[1])
except KeyError as e:
	print(e)
except IndexError as err:
	print(err)
except:
	print('Unknown error')

	
2
>>> y=[1,2,3]
>>> try:
	print(y[4])
except KeyError as e:
	print(e)
except IndexError as err:
	print(err)
except:
	print('Unknown error')

list index out of range
>>> y[4]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    y[4]
IndexError: list index out of range
>>> x[5]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    x[5]
KeyError: 5
>>> try:
	print(y[4])
except KeyError as e:
	print(e)
except IndexError as err:
	print(err)
except:
	print('Unknown error')
finally:
	print('In any case I will execute')

	
list index out of range
In any case I will execute
>>> try:
	print(y[1])
except KeyError as e:
	print(e)
except IndexError as err:
	print(err)
except:
	print('Unknown error')
finally:
	print('In any case I will execute')

	
2
In any case I will execute
>>> try:
	print(y[10])
except (KeyError,IndexError,NameError) as e:
	print(e)
except:
	print('Unknown error')
finally:
	print('In any case I will execute')

	
list index out of range
In any case I will execute
>>> 

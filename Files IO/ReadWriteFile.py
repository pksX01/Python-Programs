#Reading a text file

fileobj = open('c:\\pythoncodes\\testfile.txt')

print(fileobj)

#print(fileobj.read()) #read() will read the whole file

#print(fileobj.readlines()) #it will return a list consisiting of the contents of file.

mylist = fileobj.readlines()

for val in mylist: #iterate over the list returned by readlines()
    print(val)

fileobj.seek(0) #it will rewind the file

print(fileobj.read())

fileobj.seek(0)

print(fileobj.readlines(1)) #will return list consisting of line 1

print(fileobj.readlines(2))

fileobj.close()

fileobj1 = open('c:\\pythoncodes\\testfile1.txt','w')

str='vin'
fileobj1.write(str)

lst = ['this','is','a sample file']

fileobj1.writelines(lst)
print("Whether writable ? : ",fileobj1.writable())
print("Whether seekable ? :", fileobj1.seekable())
print("Whether readable ? :", fileobj1.readable())

print('Mode = ',fileobj1.mode)
fileobj1.close()




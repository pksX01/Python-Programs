mydict={'India':{'UP':1234678,'DELHI':100003},'Pak':{'PUNJAB':26788,'BALOOCH':23456},'USA':{'NEW YORK':223466,'CALIFORNIA':356782}}

print(mydict,'\n')

print('keys for outer dict')
for iter in mydict.keys():
    print(iter)

print('\n')

print('keys and values for outer dict')
for iter, val in mydict.items():
    print(iter,"->",val)

print('\n')

print('keys and values for inner dict')
for iter, val in mydict.items():
    for in_key, in_val in val.items():
        print(in_key,"->",in_val)
print('\n')

print('max population')
for out_key, out_val in mydict.items():
    for in_key, in_val in out_val.items():
        print(max(in_val))

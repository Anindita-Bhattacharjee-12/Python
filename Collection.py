l=['a','b',1,2]                #list
t=(2.2,4.7,'c','d')            #tuple
print(l[2],t[-3],l[-1])

for i,b in enumerate(l):
    print(f'{i}:{b}')

c=[]
c.append('a')
c.append('b')
c.append(1)
c.append(2.3)    
print(c)

c=['a','b','c','b']
c.insert(0,'a')
print(c)
c.insert(2,'b')
print(c)
c.remove('b')
print(c)
del c[0]
print(c)

depts={"EEE","MBA","CSE"}         #set
depts.add("IPE")
print(depts)
depts.remove("EEE")
print(depts)
print("CSE" in depts)
print("Archi" in depts)

std={'Person':2,'Watre':4,'Rat':7}    #Dictionary
print(std,type(std))
print(std['Person'])
print(std.get('Person','default'))
print(std.get('Person'))
print(f'Keys: {std.keys()}')
print(f'Values: {std.values()}')

for obs in std:
    print(obs)

for obs in std:
    value=std[obs]
    print('A %s has %d legs'%(obs,value))

for obs,value in std.items():
    print('A %s has %d legs'%(obs,value))

a=[1,2,3,4,5]
print(a[0:3])            #slicing operator
print(a[:2])
print(a[3:])
print(a[:-1])
print(a[2:-2])   

a=[1,2,3,4,5]
b=[5,4,3,2,1]
print(zip(a,b))
print(list(zip(a,b)))

for x,y in zip(a,b):
    print(f'{x} - {y} = {x-y}')

a=[1,2,3,4,5]
b=[5,4,3]
print(list(zip(a,b)))

arr1=[0,1,2,3,4,5,6,7,8,9]
arr2=[]
for a in arr1:
    arr2.append(a**2)
print(arr2)

#List Comprehension
arr1_copy=[i for i in arr1]
print(arr1_copy)

arr1_copy=[a**2 for a in arr1]
print(arr1_copy)

arr1_copy_even=[x**2 for x in arr1 if x%2==0]
print(arr1_copy_even)

d={(a,a):(a,a**2) for a in range(10)}
print(d)
print(d[5,5])
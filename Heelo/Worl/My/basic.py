x=3
print(type(x)) 
print(x+1)   
print(x-1)   
print(x*2)   
print(x**2)  

x+=1
print(x)  
x*=2
print(x)  
y=2.5
print(type(y)) 
print(y,y+1,y*2,y**2) 


t=True
f=False
print(type(t)) 
print(t and f) 
print(t or f)  
print(not t)   
print(t != f)  

print("Hello World")
print('Hello World')
print("""Hello
World""")

a=10
print(f'The value of a is {a} {a}')
print(f'The value of a is {a+5}')
print('a is {}'.format(a))
print('a is '+str(a))
print('a is %d %d'%(a,a))

a=5
b=6
if a==5:
    print('The variable a is 5')
elif b==6:
    print('The variable b is 6')
elif a==6:
    print('The value of a is 6')
else:
    print("nothing")
                
for x in range(1,20,2):
    print(x)

for a in range(10,1,-1):
    print(a)

acc=0
for x in range(1,10):
    print(f'{acc}+{x}= ',end='')    
    acc+=x
    print(acc)
print(f'Final sum is {acc}')    


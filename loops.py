'''LOOPS-
sometime a programmer wants to execute a group of statement a certain number of times. This can be done using loops. Based on this loops are further classified into following main types
1.for loop
2. while loop


for i in range(1,11,3):
    print(i,"hello world")


#print elements of a list using for:
list=[10,20,30,40,50,60]

for i in list:
    print(i)
    

fruits=["apple","banan","mango"]
for haha in fruits:
    print(haha)



#while loop:
i=0
while i<10:
    print(i,"hello world")
    i=i+1

    

#find the even number to 100:
i=2
while i <=100:
    print(i)
    i+=2
    
j=0
while j <=10:
    print(j)
    j=j+2

x=10
while x==10:
    x=x-1    
    print(x)

i=10
while i ==20:
    print("no output")
    # it will show no output
    


x=4
y=0

while x >=0:
    x-=1
    y+=1
    if x==y:
        continue
    else:
        print(x,y)

        

x=4
y=0
while x>=0:
   if x==y:
      break
   else:
      print(x,y)
      x-=1
      y+=1
      


#print the given pattern:
n=1
for _ in range(10):
    print("*"*5)

    or

n=int(input("enter n number:"))
for _ in range(n):
    print("*"*2)   
    

 

n=int(input("enter any number "))
for j in range(n):#loop for rows
    for i in range(1,n+1):
        print(i,end="")
    print() 

    
n=4
for row in range(n):
    for column in range(1,n+1):
        print(column,end="")
    print()    

n=4
for row in range(1,n+1):
    for column in range (1,row+1):
        print(column,end="")
    print()     


n=int(input("enter any number")) 
for row in range (1,n+1):
    print(" "*(n-row),end="")
    for column in range(1,2*row):
        print(column,end="")
    print()    
    '''

n=4
for row in range(1,n+1):
    for column in range(1,row+1):
        print(column,end="")
    print()     
 










    
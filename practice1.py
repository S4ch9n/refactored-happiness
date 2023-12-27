#
# 1) print the first 10 natural number using for loop
'''
 n=11
 for i in range(1,n):
  print(i)

# 2) all the even number withing given range
 n=int(input("enter any number"))
 if n % 2==0:
   print("number is even")
 else:
  print("odd")  


# to check a person is eligible for vote or not
num=int(input("enter age"))
print("person can","vote" if  num >=18  else "not vote")



#number is even or odd
n=int(input("enter any number"))
print("number is","even" if n %2==0 else "odd")


#write a program to display "hello " if a number entered by user is multiple of five
n=int(input("enter any number"))
print("hello"if n % 5==0 else "bye")

#calculate the electricity bill
n=int(input("enter any number"))
if n <=100:
    amt=0
if n>=100 and n<=200:
    amt=(n-100)*5
if n>200:
    amt=500+(n-200)*10
print("ammount to pay:",amt)    





#to display the last digit of a number 
n=int(input("enter any number"))
print("the last digit number ",n%10)



# to check whether last digit of a number is divisible by 3 or not
n=int(input("enter any number"))
print("number is","divisible"if n %3==0 else "not divisible") 


# program to write the percentage from the User
marks=int(input("enter any number"))
if marks > 100:
    print("invalid ")
elif marks >90:
    print("grade a")     
elif marks >80 and marks <= 90:    
    print("grade C")
elif marks >=60 and marks <=80:
    print("grade d")    
else:
    print("d")
    



#year is leap or not
n=int(input("enter any number"))
if n%100==0:
    if n % 400==0:
        print("entered year is a leap year")
else:
    if n % 4==0:
        print("entered year is leap ")        
    else:
        print("not a leap year")    

      



#write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for january and number of days 31 and so on

num=int(input("enter any number from one to three"))
if num==1:
    print("january")
elif num==2:
    print("feburary")    
elif num==3:
    print("march")
else:
    print("enter number from one to three")    
    


if True:
    print(101)
else:
    print(202)    




#write a program to check whether a number entered is three digit number or not
num=int(input("enter any three digit number"))
if num >99 and num < 1000:
    print("number is three digit")
else:
    print("number is not three digit")    
    

#write the program to find the lowwest number out of two number expected from user

num1=int(input("enter one number"))
num2=int(input("enter a second number"))
if num1>num2:
    print("smaller number is",num2)
else:
    print("smaller number is",num1)    
    


#find the greatest number between two number
num1=int(input("enter one number"))
num2=int(input("enter a second number"))
if num1>num2:
    print("greatest number is ",num1)
else:
    print("greatest number is", num2)    



#positive or negative
num1=int(input("enter one number"))
print("number is","positive" if num1>=0 else "negative ")

# write a program to check a number is divisible by 7 or not
n=int(input("enter a number"))
print("number is "" divisble "if n%7==0  else "not divisible" )





n=int(input("enter n number"))

for row in range(1,n+1):
    for column in range(1,row+1):
        print(column,end=" ")
    print()    
    


n=int(input("enter a number"))
for i in range(1,n+1): 
    for j in range(1 ,i+1):
        print(j,end=" ") 
    print()     
   '''
list=["apple","mango","banana","gava"]
for i in list:
    for j in i:
       print(j,end=" ")
    print()   
   




 








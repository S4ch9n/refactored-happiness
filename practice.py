'''#MCQ 1
x=10
y=5
print(x>y and x < 15)
 
 #MCQ 2
x=5
y="3"
print(int(y))#it will show error

#MCQ 3  
print("the value of these number is ",float(8//3+4%2))


#find any positive intiger    
number=int(input("enter a number"))
if number >=0:
   print("the number is positive")
else:
   print("the number is negative")   
'''
'''



# find even or odd number
number_1=int(input("enter a positive intiger"))
if number_1 % 2 ==0:
   print("number is even")
else:
   print("print number is odd")   


  
   
 #find, profit , loss  
cp=int(input("enter cost price"))
sp=int(input("enter selling price"))
if sp>cp:
    profit=sp-cp
    print("shopkeeper has made profit",profit)
elif sp < cp:
    loss=cp-sp
    print("shopkeeper has made loss",loss)
else:
    print("not profit not loss")    
    '

#find grades
name=int(input("enter any number"))
if name >80 :
    print("grade is very good")
elif name >60:
    print("grade is good")
elif name >40:
    print("grade average")       
else:
    print("fail")    
    


#multiple conditions using 'and' and 'or'
# find grades of two subjects 
eng_marks=int(input("enter eng marks"))
math_marks=int(input("enter math marks"))
if eng_marks > 80 and math_marks > 80 :
    print("a grade")
elif eng_marks >80 or math_marks >80:
   print("b grade")  
else:
    print("fail") 


#take positive integer input and tell if it is four digit number or not 
number=int(input("enter a number"))
if number >=1000 and number <=9999:
    print("it is a 4 digit number")
else:
    print("not a 4 digit number")   
    
 #take 3 positive intgers input and print the greatest of them
number1=int(input("enter any number1"))
number2=int(input("enter any number2")) 
number3=int(input("enter any number3"))
#if n1 is greatest
if number1 > number2 and number1 > number3:
    print("number1 is greatest")
elif number2 > number1 and number2 > number3:
    print("number2 is greater")    
else:
    print("number3 is greatest") 
 
    
#nested if_else :
n1=int(input("enter any number1"))
n2=int(input("enter any number2")) 
n3=int(input("enter any number3"))
if n1 > n2:
    #either n1 or n3 is greatest
    if n1 > n3:
        print(n1,"is the greatest")
    else:
        print(n3 , "is the greatest")    
else:
    if n2>n3:
        print(n2,"is the greatest number")  
    else:
        print(n3,"is greatest number")          


# take postive integer input and tell if it is divided by 5 or 3 but not divisible by 15.
num=int(input("enter any positive intger"))
#checking whether it is dvisible by 15
if num % 15 ==0:
    print("number is divisible by 15")
else:   
    if num %5 ==0 or num % 3==0:
        print("this is not divisible by 15 but was divisible by 5 and 3") 
    else:
        print("number is not divisible by 3 nor 5")   
  ''' 

     
 

    
         


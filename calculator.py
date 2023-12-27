# making calcultor using Match case:
'''
num1=int(input("enter number 1:"))
num2=int(input("enter number 2:"))


haha= input("enter operator:")

match haha :
    case"+":
        print("sum is", num1 + num2)
    case"-":
        print("difference is", num1 - num2)    
    case"*":
        print("multiplication is ",num1*num2)    
    case"/":
        print("division is ", num1/num2)    
    case _:
        print("enter a valid operator")
    

name=int(input("enter number"))    
if name >= 0 :
    print("number is even")
else:
    print("not a number")    
    
#write a program to find even or odd using ternary operation

num=int(input("enter any number"))
print("output is","even" if num %2==0 else "odd")
''' 

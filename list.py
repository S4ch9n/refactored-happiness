'''
fruits=["apple","mango","banana","cherry"] #create a list
print(fruits)
print(type(fruits))#check type of list
print(len(fruits))#check length of list
 

 #checking if item is present in the list

if "banana" in fruits:
    print("banana is part of list")
if "kiwi" not in fruits: 
    print("kiwi is not present is the list")    

fruits=["apple","mango","banana","cherry"] #create a list
print(fruits[1])
print(fruits[-3])
print(fruits[1:3])
'''
#adding elements to th list:


# list2=[70,80]
# # list.append(50) add items to the end of list
# # list.insert(5,60) insert the item in selected list
# # list.extend() it combine two list lists and make on list
# print(list,list2)

# list=[10,20,30,40]
# list.remove(30) it will remove selected item from list
# list.pop(2) it will also remove selected item 
# list.pop() remove last part of item
# print(list)
# list=[10,20,30,40]
# list[3]=50 it will replace 40 with 50
# list[3:4]=[50,60 ] it will replace 40 with 50 and add 60
# print(list)

# list=[30,20,10,50,40,60]
# list.sort() it will make list ascending order
# list.sort(reverse=True) it will make list in descending order  
# list.reverse()  it will make list in descending order
# print(list)
# new_list=[x for x in list if x > 25]
# print(new_list) it will make new list greater than 25 value

# fruits=["apple","mango","banana","kiwi","orange"]
# fruitss=[fruit for fruit in fruits if "a" in fruit]
# print(fruitss) it will only print fruits with alphabet a

# new_fruits=fruits.copy() it will copy 
# print(new_fruits)
# fruitss=fruits + new_fruits it will add two variables
# print(fruitss)


#Nested list
# fruits=["apple","mango","banana","kiwi","orange"]
# fruits.insert(2,["kiwi ","papaya"])
# print(fruits)
# print(fruits[2][0])
'''
#questions  swap the value of 0 and 2  
list=[10,20,30,40]
list1=list[0]
print(list)
list[0]=list[2]
list[2]=list1
print(list)
 #or can be written like this

n=int(input("select the size of list:"))
list=[]
for i in range(n):
    num=int(input())
    list.append(num)
list1=int(input("enter index 1"))    
list2=int(input("enter index 2 "))
print(list)


temp=list[list1]
list[list1]=list[list2]
list[list2]=temp
print(list)
'''
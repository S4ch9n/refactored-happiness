'''
phones= {
    "sachin": 86796 ,
    "jhon":675788,
    "joy":69769
}

#print the dicrt
print(phones)


#check type of dict
print(type (phones))

print(len(phones))# printing length of phones

# if we have to find jhon number
print(phones["jhon"])
print(phones.get("jhon"))# same 

# print all of the keys 
print(phones.keys())

#update value in dict
phones["jhon"]=986565
print(phones)

#add elements in dictionary
phones["kia"]=23566 # kia will be updated in dictinoary
print(phones)



}
#add two dic
phones= {
    "sachin": 86796 ,
    "jhon":675788,
    "joy":69769
}
more_phones={
    "sia":23554
}
phones.update(more_phones)
print(phones)

# remove elements from dict
phones.pop("jhon")
print(phones)

phones.popitem() # this will remove last added item

phones.clear() # this will clear the dict

#printing value of dict
phones= {
    "sachin": 86796 ,
    "jhon":675788,
    "joy":69769
}
for x in phones:
    print(phones[x]) # this will print the all value of x

#if we have to print both keys and values

phones= {
    "sachin": 86796 ,
    "jhon":675788,
    "joy":69769
} 
for x,y in phones.items():
    print(x,y)


#nested dict

phones={
"area1": {
    "x": 0,
    "y" : 1,
    "z" : 4
  },
"area2":{
    "a" :3,
    "b": 4,
    "c": 8
}


   
print(phones["area1"]["y"])
print(phones["area2"]["c"])


#given a dictionary in python , write a python program to find the sum off alll items in the dictionary

input={
    "a": 100,
    "b": 200,
    "c": 300,
    }
print("the sum of dic value is ",sum(input.values()))

'''



input_strings=input("enter string :")
n = int(input ("enter a number"))

# creating a dicitonary for mirror operation
alphabets="abcdefghijklmnopqrstuvwxyz"
reverse_alphabets=alphabets[::-1] # if it is -1(or negative ( and 1 indicate here by one step)) it indicates right to left and if it is +1 ( or postitive ) it indicates from left to right 
# :: , it means we dont set limits , means there is not starting point and ending point.We will traverse whole line
dict1=dict(zip(alphabets,reverse_alphabets)) # with zip function alphabets become key and reverse_alphabets become value


# findin the part of string on which we wil do mirror operation
prefix=input_strings[0:n-1]
suffix=input_strings[n-1:]

# finding the mirror string

mirror=""
for i in range(0,len(suffix)):
    mirror=mirror + dict1[suffix[i]]
#creating the final string
res=prefix + mirror
print("the result is",res) 
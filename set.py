'''
#creating a set

names={"sia","ria","priya"}

#printset
print(names) #can be printed in differnet sequence
print(len(names))
print(type(names))

#accessing items for set
for x in names:
    print(x)

#check if an team exist in set
if "sia" in names:
    print("sia is present")     

 #add elements in set:
# names.add('siya') it will not add siya because siya is already added on set , and set can't be duplicated    
names.add('rahul')
print(names)      


#add another sequence in set:
names={"sia","ria","priya"}
name_list=["raju","priyanak"]
names.update(name_list)
print(names)

#for removing
# names={"sia","ria","priya"}

# names.remove("sia")
# names.discard("sachin")#it will not show error even if item is not present
# print(names)



# union or update the value
names_set={"sia","ria","priya"}
names_tuples2={"tamana","parvinder","joginder"}
s3=names_set.union(names_tuples2)# it will combine both sets
names_set.update(names_tuples2) # it wil 
print(names_set)
print(s3)



#keep only duplicate while joining
s1={1,2,3,4,5}
s2={6,1,3,4,5}
s1.intersection_update(s2)
print(s1)



#keep all values except duplicate

s1={1,2,3,4,5}
s2={6,1,3,4,5}

s1.symmetric_difference_update(s2)

print(s1)
'''
ar1=[1,5,10,20,40,80]
ar2=[6,7,20,80,100]
ar3=[3,4,15,20,30,70,80,120]
#typeaasting into set
s1=set(ar1)
s2=set(ar2)
s3=set(ar3)
#join using intersection
s1s2=s1.intersection(s2)#it will make new set to add duplicate  values
final_set=s1s2.intersection(s3)
final_list=list(final_set)
print(final_list)





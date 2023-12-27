'''
list=("red","yellow","green")
list1=("apple","mango")


input=('a','b','c','d','e')
#create through a sequence order
for x in reversed (input):
    print(x,end="")
   ''' 
input_tuple=(1,2,3,4,5,6,)
list=[7,8,9]
for x in reversed(input_tuple):
      list.append(x)
output_tuple=tuple(list)
print(output_tuple)


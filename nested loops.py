'''
row=4
column=4
symbol="*"
for row in range(1,row):
    for column in range(1,column+1):
        print(symbol,end=" ")
    print()    

# BY  WHILE statement print 1234 4 time 
i=1
while i < 5:
    j=1
    while j < 5 :
        print(j,end="")
        j=j+1          
    print()
    i=i+1    
'''


#half triangle

i=1
while i <= 5:
    j=1
    while j==i:
        print("j",end="")
        j=j+1
    print()    
    i=+1
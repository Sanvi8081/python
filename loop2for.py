#for loop
list=[1,2,3,4,5,6]
for val in list:
    print(val)

#for loop with else
list=[1,2,3,4,5,6,78]
for val in list:
    print(val)
else:
    print("ends")


#print the elements using the loop [1,4,9,16,25,36,49,64.81.100]
list=[1,4,9,16,25,36,49,64.81,100]
for val in list:
    print(val)


#range
seq=range(5)
for i in seq:
    print(i)
#or
for i in range(10):
    print(i)

#pass stmt
for val in range(10):
    pass

# wap to find the sum of first n numbers(usign while)
num=int(input("ENTER THE NNUMBER N:"))
i=1
sum=0
while i<=num:
    sum+=i
    i+=1
print(sum)
#wap to find the factorial of first n numbers.(using for)
num=int(input("ENTER THE NUMBER:"))
fact=1
for i in range(1,num+1):
    fact*=i
print("factorial=",fact)

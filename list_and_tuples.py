#list slicing
fruits=["apple","strawberry","kiwi","orange"]
print(fruits[1:2])
print(fruits[-3:-1])

#list methods
DataAnalysis=["descriptive","diagnostic","predictive","prescriptive"]
#list.append()
DataAnalysis.append("qualitative")
print(DataAnalysis)
#list.reverse()
DataAnalysis.reverse()
print(DataAnalysis)
#list.insert()
DataAnalysis.insert(2,"quantative")
print(DataAnalysis)

list=[55,99,66]
#list.sort()
list.sort()
print(list)
#list.sort(reverse=true)
list.sort(reverse=True)
print(list)



#TUPLES
#wap to ask the user to enter the names of their 3 fav topics and store them in list
topic1=str(input("ENTER 1ST TOPIC OF INTEREST:"))
topic2=str(input("ENTER 2ND TOPIC OF INTEREST:"))
topic3=str(input("ENTER 3RD TOPIC OF INTEREST:"))
list=[topic1,topic2,topic3]
print(list)

#wap to check if a list conatins a palindrome of elements.
list1=[1,2,1]

copy_list1=list1.copy()
copy_list1.reverse()
if copy_list1==list1:
    print("PALINDROME.")
else:
    print("NOT A PALINDROME.")

#wap to count number of students with the A grade in the following tuple.
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))
print(tup.sort())

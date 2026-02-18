import os

f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()


f=open("demo.txt","r")
line1=f.readline()
print(line1)
f.close()

f=open("demo.txt","w")
f.write("this is me adding new line")

#r+ mode for overwriting content
f=open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()

#with sytnax
with open("demo.txt","r") as f:
   data= f.read()
   print(data)
with open("demo.txt","w") as f:
  f.write("LLMs and building systems")


#DELETING A FILE 
##os.remove("demo.txt")


#practice problems
#1. create a new file name practice using python add the following data in it
#hi everyone we are learning file i/o using java 
with open("practice.txt","w")as f:
   f.write("hi everyone we are learning file i/o \n")
   f.write("using java\n")
   f.write("i like programming in java.")

#2. WAF that replaces all occurences of "java" with "python" in above file
with open("practice.txt","r") as f:
   data=f.read()

new_data=data.replace("java","python")
print("new_data")

with open("practice.txt","w") as f:
   f.write(new_data)

#search whether the word searchinf exist or not in the file 
with open("practice.txt","r") as f:
  data=f.read()
  if(data.find("learning")!=-1):
     print("found")
  else:
     print("not found")


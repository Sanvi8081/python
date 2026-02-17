#recursive function
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)

#factorial
def fact(n):
   if(n==0 or n==1):
     return 1
   else:
      return n*fact(n-1)
   
      
print(fact(5))
   
# write a recursive function to calculate the sum of first n natural numbers
def sum(n):
   if (n==0):
      return 0
   return  sum(n-1)+n

calcsum=sum(3)
print(calcsum)
    
#wrtie a recursive function to print all elements in a list
def print_list(list,idx=0):
   if(idx==len(list)):
      return 
   print(list[idx])
   print_list(list,idx+1)
   
cars=["BMW","Mercedes","Audi","Defender"]
print_list(cars)
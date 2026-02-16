#functions
#function defination
def calcsum(a,b,c): #paramters
    sum=a+b+c
    print(sum)
    return sum
    
calcsum(1,2,3)#function call; arguments

#function to calculate the avg of 3 numbers
def avg(a,b,c):
    average=(a+b+c)/3
    print(average)
    return average
avg(4,5,6)

#built-in and user-defined functions(users make them)
#print(),len(),type(),range()

#default parameters
def cal_prod(a=1,b=1):
    print(a*b)
    return a*b
cal_prod()

#practice questions
#waf to print the length of a list (list is the parameter)
cities=["delhi","noida","mumbai","pune","kolkata"]
def print_len(cities):
    print(len(cities))
print_len(cities)

#waf to print the elemnents of a list ina singlee line.(list is the parameter)
subjects=["AI","DS","ML","NLP","DL(DEEP LEARNING)"]
def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(subjects) 


#waf to find the factorial of n (n is the parameter)
def cal_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)

cal_fact(8)

#waf to convert USD TO INR
def converter(usd_val):
    inr_val=usd_val*90.56
    print(usd_val,"USD=",inr_val,"INR")

converter(5)

#print odd even using function
def evaluator(n):
    if n%2==0:
        print("N IS EVEN")
    else:
        print("N IS ODD")
    
evaluator(44)
#WAP TO CHECK IF A NUMBER IS ODD OR EVEN
num=int(input("ENTER THE NUMBER:"))
if num%2==0:
    print("NUMBER IS EVEN.")
else: 
    print("NUMBER IS ODD.")


#WAP TO FIND GREATEST OF THREE NUMBERS ENTERD BY USER 
num1=int(input("ENTER THE 1ST NUMBER:"))
num2=int(input("ENTER THE 2ND NUMBER:"))
num3=int(input("ENTER THE 3RD NUMBER:"))
if num1>num2:
    print("NUM1 IS GREATER.")
    if num1>num3:
        print("NUM1 IS THE GREATEST.")
elif num2>num3:
    print("NUM2 IS GREATER.")
    if num2>num1:
        print("NUM2 IS GREATEST")
else:
    print("NUM3 IS GREATEST.")

#WAP TO CHECK IF NUMBER IS MULTIPLE OF 7 OR NOT
num=int(input("ENTER THE NUMBER:"))
if num%7==0:
    print("NUMBER IS DIVISIBLE BY 7.")
else:
    print("NUMBER IS NOT DIVISIBLE BY 7.")



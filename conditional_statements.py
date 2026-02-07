#if-elif-else statement
#grade system
st_name="Zoya"
print("Student Name:",st_name)
st_marks=89
print("Total marks in Math:",st_marks)

if st_marks>=90:
    print("Grade: O")
elif st_marks>=80:
    print("Grade:A+")
elif st_marks>=70:
    print("Grade:A")
elif st_marks>=60:
    print("Grade:B+")
elif st_marks>=50:
    print("Grade:B")
elif st_marks>=40:
    print("Grade:C")
else:
    print("Failed.")


#single line if / ternanry operator 
#1st way
subject=input("subject:")
Done='yes' if subject=="accounts" else 'no'
print(Done)
#2nd way
print("Accounts reviewed.") if subject=="accounts" else print("Accounts not reviewed.")

#Clever if/ternary operator 
sal=float(input("salary:"))
tax=sal*(0.1,0.2) [sal>50000]
print(tax)



            
      

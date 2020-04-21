m=int(input("Enter Maths Marks:"))
p=int(input("Enter Physics Marks:"))
c=int(input("Enter Chemistry Marks:"))
tot=m+p+c
avg=tot/3
print("Total",tot)
print("Average",avg)
if m>=35 and c>=35 and p>=35:
    result="Pass"
    if avg>=75:
        result+=" Distinction"
    elif avg>=60:
        result+=" First Class"
    else:
        result+=" Second Class"
else:
    result="Fail"
print("Result",result)



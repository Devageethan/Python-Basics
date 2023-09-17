sal=int (input("sal:"))
age=int (input("age:"))
if(sal>=20000 or age<=25):
    loan=int (input("loan amount:"))
    if(loan>50000):
        print("maximum limit 50000")
    else:
        print("you are eligible")
else:
    print("you are not eligible")
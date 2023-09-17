a=int(input("enter the score"))
if(a<35):
    print("poor student")
elif(a<=80 and a>=35):
    print ("average student")
elif(a>=90 and a<=100):
    print("good student")
else:
    print ("invalid input")

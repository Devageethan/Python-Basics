a=int(input("value A:"))
b=int(input("value B:"))
operation=input("add/sub/mul/div:")
if(operation=="add"):
    print(a+b)
elif(operation=="sub"):
    print(a-b)
elif(operation=="mul"):
    print(a*b)
elif(operation=="div"):
    print(a/b)
else:
    print (" invalid input")

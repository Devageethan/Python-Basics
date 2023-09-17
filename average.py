tamil=int(input("tamil:"))
english=int(input("english:"))
maths=int(input("maths:"))
science=int(input("science:"))
social=int(input("social:"))
add=(tamil+english+maths+science+social)
avg=add/5
print(avg)
if(avg<35):
    print("additional classes is reqiured")
else:
    print("you are good student go head")
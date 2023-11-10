print(True)
print(False)
a=bool(1)
b=bool(0)
print(a)
print(b)
c=bool("hi")
d=bool([12.22])
print(d)
print(c)
e=bool("")
print(e)
f=bool({})
print(f)
k=bool(None)
print(k)
if a>0:
    print(True)

#isinstance fun
def my():
    x=100
my()
print(isinstance(my(),int))
def fun():
    return True
fun()
print(fun())
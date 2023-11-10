a=11
b='hi'
c=34.4
d=True
r=1j
f=None
#convert int,float to complex
e=float(a)
g=int(c)
h=complex(a)
j=complex(c)
#l=int(r)    #error

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(r))
print(type(f))
print(e)
print(g)
print(h)
print(j)
#print(l)
li=[11,22,123,44]
print(type(li))
tu=(90,89,'rt')
print(type(tu))
s={'ee',34,56,98}
print(type(s))
di={
    1:'dd',
    2:'tt',
}
print(type(di))
print(type(range(5)))
fr=({23,87,9,44})
print(type(fr))
q= b"56"
print(type(q))
ba=bytearray(5)
print(ba)
print(type(ba))
mv=memoryview(bytes(5))
print(mv)

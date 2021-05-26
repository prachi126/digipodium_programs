l=[1,2,3,4,5,6]
print(type(l))
print(l)
t=(1,2,3,4,5)
print(type(t))
t1=1,2,3,4,5,6
print(type(t1))
s={1,2,3,4,5,6}
print(type(s))
d={1:[1,2,3,4],2:"eeer"}
print(d)
a=10
out=isinstance(a,int)
print("is an integer",out)
out=isinstance(a,float)
print("is a float",out)
a=10
if a>5:
    print("a is greater than 5")
if a >15:
    print("a ais less than 15")
if a==10:
    print("this is equals to 10")
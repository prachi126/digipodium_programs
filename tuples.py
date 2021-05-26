#indexed nd ordered
#heterogeneous ,immutable
#represented by paranthesis '()'
#has a function 'tuple()'
x=(1,2,3,4)
y=1,2,3,4
print(type(x))
print(type(y))
a=[1,2,3]
t=tuple(a)
n='hello'
tt=tuple(n)
print(t)
print(tt)

#functions
a=(1,2,3,4,5,6,6,6)
print(a.count(3))
print(a.index(6))

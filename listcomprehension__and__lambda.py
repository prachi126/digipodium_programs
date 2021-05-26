x=[1,2,3,4,5,6]
l=[i**2 for i in x]
print(l)
 

a=[1,2,3,4,5,6,7,8,9]
x1=[i**2 for i in a if i%2!=0]
print(x1)
names=['prachi','anjali','anjalis','vaishali','avinashsingh']
names_containing_e=[name for name in names if 'e' in name]
print(names_containing_e)

cir=lambda r:2*r*3.14
data=[3,3.42,45,67,898]

results=[cir(radius) for radius in data]
print(results)
result=list(map(cir,data))
print(result)


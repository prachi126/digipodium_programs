#multiples of 5 and 7
l=[]
for i in range(1500,2701):
    if i%7==0 and i%5==0:
        l.append(i)
print(l)

#find even and odd  numbers from a series of numbers
n=int(input("enter numbers to be inputted"))
even=[]
odd=[]
for i in range(n):
    a=int(input())
    if a%2==0:
        even.append(a)
    else:
        odd.append(a)
print(even)
print(odd)

#fibonacci series between 0 to 50
a,b,s=0,1,0
print(a)
print(b)
while s<=50:
    s=a+b
    if s>50:
        break
    print(s)
    a=b
    b=s

#reverse a word
a=input()
s=''
b=len(a)
for i in range(b-1,-1,-1):
    s+=a[i]
print(s)
# reverse using slicing
a=input()
s=a[::-1]
print(s)
#to print first 50 prime number

l=[]
t=0
for i in range(1,250):
    if t==50:
        break
    for j in range(2,i):
        if i%j==0:
            break
    else:
        l.append(i)
        t+=1
print(l)
print(len(l))

#to create a list of names and remove 'a' or 'o'

n=int(input("enter the number of names u wanna add in the list"))
l=[]
l1=[]
for i in range(n):
    l.append(input())
for n in l:
    if 'a' in n.lower():
        n=n.replace('a','')
    if 'o' in n.lower():
        n=n.replace('o','')
    l1.append(n)
print(l1)

#nested list
n=int(input())
l=[]
for i in range(n):
    l.append([])
    for j in range(5):
        l[i].append(j)
print(l)

#list of cricketers
l=[]
n=int(input())
for i in range(n):
    a=input()
    if a[0].isupper():
        l.append(a)
print(l)

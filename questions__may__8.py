
s=input()
a=s
c=0
v=['a','e','i','o','u']
for i in s:
    if i in v:
        a=a.replace(i,'')
        c+=1
print(a,' ',c)
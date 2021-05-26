#formatting functions
'''upper,
lower,
capitalize,
swapcase,
title,
center,
ljust,
rjust'''
#utility functions-helps in logical problem
'''find
index,
replace,join,strip,
rsplit,
count'''
#validation functions

msg="this is an example message from myself"
#upper case
print(msg.upper())#returnS a copy always
msg_upper=msg.upper()
print(msg_upper)
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(msg.swapcase())


#ljust and rjust and center
#to provide extra space on both the sides

word='mapple'
print(word.ljust(10)) #total length + extra space you want
for i in range(1,15,2):
    print(i*'0')
for i in range(1,15,2):
    print((i*'0').rjust(15))
for i in range(1,15,2):
    print((i*'0').center(14))
# find and index
msg='hello are you interested in this class,are you?'
ind=msg.find("are")
print(ind)
ind=msg.rfind("are")
print(ind)
ind=msg.find("aren't")
print(ind)
ind=msg.find("are")
print(ind)

# index
ind=msg.index("are")
print(ind)
ind=msg.index("aren't")
print(ind)


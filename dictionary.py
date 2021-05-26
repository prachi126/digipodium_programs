#ordered
#mutable(keys are immutable but values can be anything)
#has a function 'dict()'
#no slicing
'''update
pop
popitem
get
keys
values
items'''
fruits={'apple':100,'banana':40,'cherry':200,'dragonfruit':250}
print('updating values in dictionary')
new_fruits={'guava':40}
fruits.update(new_fruits)
print(fruits)

print('removing values')
fruits.pop('cherry')
if 'orange' in fruits:
    fruits.pop('orange')
else:
    print("orange not found")

last_item_removed=fruits.popitem()
print(f'{last_item_removed} has been removed')
print(fruits.get("apple",'price found'))
print(fruits.values())
print(list(fruits.keys()))
print(list(fruits.items()))
for i in fruits:
    print(i,fruits[i])
for i,j in fruits.items():
    print(i,'--->',j)
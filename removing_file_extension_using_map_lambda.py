files=['demo.png','hello.exe','sleep.png','work.doc']
remove_ext=lambda filename : filename.split(".")[0]
l=list(map(remove_ext,files))
print(l)


x=[1,3,4,6,7,8,9,30]

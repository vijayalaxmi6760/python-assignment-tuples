t=(10,20,30,10,40,10,50)
x=10
first =t.index(x)
last=len(t)-1-t[::-1].index(x)
print("first occurence:",first)
print("last occurence:",last)
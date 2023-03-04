x=str("HelloMyfriend")
c={}
for i in x:
    if i in c:
        c[i]+=1
    else:
        c[i]=1

print(c)



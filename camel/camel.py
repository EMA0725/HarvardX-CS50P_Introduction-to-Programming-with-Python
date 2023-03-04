def main():
    x=str(input("camelCase: "))
    r=camelCase(x)
    print(r.lower(),end="")


def camelCase(x):
    for c in x:
        if c.isupper():
           y=x.index(c)
           x=list(x)
           x.insert(y,'_')
           x="".join(x)
           x=x.strip()



    return x





main()
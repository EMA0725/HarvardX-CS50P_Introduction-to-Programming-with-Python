def main():
    x=input("File name: " )
    mime(x.strip())
def getVal(x):
   t= x.split(".")
   return t[len(t)-1]


def mime(x):
    x=x.casefold()

    l=(".gif",".png")
    g=(".pdf",".zip")
    b=(".jpg",".jpeg")
    if x.endswith(l):
        t=getVal(x)
        print("image/{}".format(t))
    elif x.endswith(b):
        print("image/jpeg")
    elif x.endswith(g):
        t=getVal(x)
        print("application/{}".format(t))
    elif x.endswith(".txt"):
        print("text/plain")
    else:
        print("application/octet-stream")

main()
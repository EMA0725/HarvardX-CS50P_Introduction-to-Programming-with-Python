def main():
    price=50
    q=getCoin(price)


def getCoin(price):
    w=[5,10,25]
    e=int(input("insert coin: "))
    if e in w:
        price=price-e
        bill(price)
    else:
        bill(price)

def bill(r):
    if(r>0):
        print("Amount Due:"+str(r))
        getCoin(r)

    elif (r<0 or r ==0):
        print("Change owed:"+str(r).strip("-"))


main()
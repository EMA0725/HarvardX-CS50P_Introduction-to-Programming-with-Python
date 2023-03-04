def main():
    get_input()




def get_input():
    while True:
        try:
            x=input("input: ")
            x=x.strip(" ")
            if x.__contains__(","):

                a,b,c=x.split(" ")
                #print(type(b))
                modify(a, b, c)

                #print(a,b,c)
                break

            elif x.__contains__("/"):
                a,b,c=x.split("/")
                #print(a,b,c)
               #modify(int(a),int(b),str(c))
                modify(a, b, c)
                break
            else:
                pass
        except ValueError:
            #print("hallelujiah")
            pass

def modify(a,b,c):
    mon=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    #print(isalpha(a))
    #print("hey4")
    if (a.isdigit() and b.isdigit() and c.isdigit()):
        a=int(a)
        b=int(b)
        if((a<=12 and a>=1) and (b<=31 and b>=1) and len(c)==4):
            print(c,f"{a:02}",f"{b:02}",sep="-")
            return
            #break
        else:
            pass

    elif (a.isalpha()   and c.isdigit() and b.__contains__(",") and (b.strip(",")).isalnum()):

        if(a in mon ):
            #print("hey4")
            b=int(b.strip(","))
            if(b<=31 and b>=1 and len(c)==4 ):
                x=int(mon.index(a))+1
                print(c,f"{x:02}",f"{b:02}",sep=("-"))
                return
            else:
                pass
        else:
            pass

    else:
            pass

    get_input()
            #print("bhasaddd")


main()
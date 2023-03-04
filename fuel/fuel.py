def main():
    get_int()
   # percentage(x)


def get_int():
    x = input("fraction: ")
    percentage(x)


def percentage(x):
    while True:
        try:
            a,b=x.split("/")
            w=round((int(a)/int(b))*100)
            if(w>100):
                get_int()
            elif (w<=1):
                print("E")
            elif (w>=99):
                print("F")
            else:
                print(f"{w}%")

            break
        except (ValueError,ZeroDivisionError):
            get_int()
main()

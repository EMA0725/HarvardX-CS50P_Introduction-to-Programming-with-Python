def main():
    x=input("greetings:  ")
    bank(x.strip())

def bank(x):
    x=x.casefold()
    if x.startswith("hello"):
        print("$0")
    elif x.startswith("h"):
        print("$20")
    else:
        print("$100")





main()
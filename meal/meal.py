def main():
    x= float(input("What time is it? : ").replace(":","."))
    meal(x)

def meal(x):
    if x>=7.00 and x<=8.00:
        print("breakfast time")
    elif x>=12.00 and x<=13.00:
        print("lunch time")
    elif x>d=18.00 and x<=19.00:
        print("dinner time")
    else:
        print()

main()
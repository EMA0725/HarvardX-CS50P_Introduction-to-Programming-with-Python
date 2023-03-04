def main():
    x=get_input()


def get_input():
    item={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }
    c=0
    while True:
        try:
            x=((input("Item: ")).lower()).title()
            if x in item:
                c+=item[x]
                print("Total: $%.2f" %c)

        except KeyError:
            pass
        except EOFError:
            return c
            break



main()

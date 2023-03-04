def main():
    get_input()



def get_input():
    while True:
        try:
            inp()
            pass
        except EOFError:
            out()
            break

dict={}
def inp():
    x=input()
    if x in dict:
        dict[x]=dict[x]+1
    else:
        dict[x]=1


def out():
    #c=sorted(dict.keys())
    for i in sorted(dict):
        print(dict[i],i.upper())



main()
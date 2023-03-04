def greatQuestion(x):
    x=x.lower()
    t="forty-two"
    t1="forty two"
    if (x=="42" or x==t or x== t.lower() or x==t1.upper() or x==t1):
        print("yes")
    else:
        print("no")

def main():
    x=input("What is the Answer to the Great Question of Life, the Universe, and Everything?").strip(" ")

    greatQuestion(x)



main()
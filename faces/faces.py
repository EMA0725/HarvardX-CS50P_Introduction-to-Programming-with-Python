def faces(x):
    y=x.replace(":)","🙂")
    y=y.replace(":(","🙁")

    return (y)
def main():
    x=input()
    print(faces(x))




main()
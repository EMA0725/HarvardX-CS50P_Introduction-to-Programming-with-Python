def main():
     print(noVowel())


def noVowel():
     x = getInput()
     list = ["a","A","e","E","i","I","o","O","u","U"]

     for i in x:
          if i in list:
               x = x.replace(i,"")

     return (x)


def getInput():
     return  input("Input: ")

main()
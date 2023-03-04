def main():
    x,y,z= input("Expression: ").split(" ")
    print(interpreter(int(x),y,int(z)))

def interpreter(x,y,z):
    match y:
        case "+":
            return float(x+z)
        case "-":
            return float(x-z)
        case "/":
            if(z!=0):
                return x/z
        case "*":
            return float(x*z)

main()
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s1):
    s=s1.lower()
    #if (s.isalnum() and plateSize(s) and plateSize(s) and numberCheck(s)):
    if (s.isalnum()):
        if plateSize(s):
            if plateSize(s):
                if numberCheck(s):
                     return True

    else:
        return False
'''
In def is_valid():
1. created a loop of if conditions which will check all requirements
2. for first condition we are making sure that the input does not contain anything except alphabets and numericals
3. return true if all requirements are satisfied else false
'''
def plateSize(s):
    if len(s) in range(2,7):
        return True
    else:
        return False
'''
In def plateSize():
checking if the range of input is in between 2 to 6
'''

def startLetter(s):
    a = s[0:2]
    return a.isalpha()
'''
In def startLetter():
we are making sure that the first two letters of the input is alphabets and not numbers
'''

def numberCheck(s):
    c=s # creating a temp variable and storing input in it
    #print(c)
    for i in s: # looping through every element of input string
        if i.isalpha():
            c=c.replace(i,"",1)     # if the element is alphabet then remove it
        elif i.isdigit():       # if the element is digit then we are breaking from the loop
            break       # up untill here we have removed all alphabets before the first occurrence of a digit

    if ((c[:1]!="0") and c.isdigit() or len(c)==0):     # if the first digit is 0(mandatory), and if all are digits(making sure we don't have digits in between two substrings of alphabets), or len of c is 0(to get desired result even if input is all alphabets)
        return True

    else:
        #print("here")
        return False

    '''
    In numberCheck():
    step by step explanation is provided
    '''


    '''
    #s="nrvous"
    x=""
    for i in s:
        if i.isdigit():
            x=x+i

    if (len(x)!=0):
        print(x)
        if ((x[:1]=="0")):
            return False
        elif s.endswith(x[-1])is False:
            return False
    else:
        return True
    '''
    '''
    x=""
    for i in s:
        if i.isdigit():
            x=x+i
    if ((x[:1]=="0")):
        return False
    elif s.endswith(x[-1]):
        return True
        '''

main()
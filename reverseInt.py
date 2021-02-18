
# Chris Taylor
# 01/18/21
""" Goal: The goal of this exercise was to reverse an int. I implemented the first version using
    string manipulation by first converting the int to a string and then traversing it backward.
    The second function I used the modulo % and int division // operators to reverse the string
    I then wanted to create a function to check to see if the strings were properly reversed without
    using the function I had just made."""
    
#To use: Simply run the file using python3 and the program will ask for input

def reverseInt(n):
    #make string
    #loop through reverse direction
    #append each character to new string
    inputS = str(n)
    length = len(inputS)
    outputS = ""
    for i in range(length-1, -1, -1):
        outputS += inputS[i]
    return outputS
print(reverseInt(3467))

def reverseInt2(n):
    #output string
    outputS = ""
    while (n > 0):
        outputS += str(n%10)
        n = n//10
    return int(outputS)
    
def isReversed(n1, n2):
    s1 = str(n1)
    s2 = str(n2)
    len1 = len(s1)
    len2 = len(s2)
    if (len1 != len2):
        false
    count = len2-1
    for dig in s1:
        if (dig != s2[count]):
            return False
        count -= 1
    return True
    
n = int(input('Please enter a positive integer that you would like reversed (using first function): '))
nrev = reverseInt(n)
print (f'The reversed int of {n} is {nrev}')
print (f'Checking if isReversed worked... {isReversed(n, nrev)}\n')

n = int(input('Please enter a positive integer that you would like reversed (using second function): '))
nrev = reverseInt2(n)
print (f'The reversed int of {n} is {nrev}')
print (f'Checking if isReversed worked... {isReversed(n, nrev)}')

print ('Thank you for using my reverse number functions! ^_^')


    
    
    
    
    
    
    
    
    
    
    
    

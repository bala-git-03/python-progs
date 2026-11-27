# Biggest of 4 numbers 

'''
        C1  C2  R
AND     1   1   1
        1   0   0
        0   1   0

OR      1   1   1
        1   0   1
        0   1   1
        0   0   0

NOT     1   0
        0   1

    
'''

a = int(input(" Enter first Number"))


b = int(input(" Enter second Number"))

c = int(input(" Enter third Number"))

d = int(input(" Enter FOURTH Number"))

if( a>b) and (a>c) and (a>d) :
    print(a , " is Big")
    
elif ( b>c) and (b>d):
    print(b, " is Big")

elif (c>d):
    print(c, " is Big")
else:
    print(d, " is Big")
    
print(" Thank You")

print("Welcome")
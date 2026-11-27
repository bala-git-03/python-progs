# Biggest of 3 numbers 

a = int(input(" Enter first Number"))


b = int(input(" Enter second Number"))

c = int(input(" Enter third Number"))

if( a>b):
    if(a>c):
        print(a , " is Big")
    else:
        print(c ," is Big")
elif (b>c):
        print(b, " is Big")
    else:
        print(c, " is Big")
    
    
print(" Thank You")
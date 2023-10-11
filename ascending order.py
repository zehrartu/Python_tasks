x = int(input("enter the first value :"))
y = int(input("enter the second value :"))
z = int(input("enter the third value :"))

if x>y :
    if y>z :
        print(str(z), str(y), str(x))
    elif x>z :
        print(str(y), str(z), str(x))
    else:
        print(str(y), str(x), str(z))
elif y>z :
    if z>x :
        print(str(x), str(z), str(y))
    else : 
        print(str(z), str(x), str(y))
else:
    print(str(x), str(y), str(z))

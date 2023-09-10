while True:
    a=int(input("Enter a Number a="))
    b=int(input ("Enter a Number b="))
    c=int(input ("Enter a Number c="))
    if a+b==c or a==b+c:
        print("The numbers satisfy Addition equation")
    elif a-b==c or a==b-c:
        print("The numbers satisfy Subtraction equation")
    elif a*b==c or a==b*c:
        print("The numbers satisfy Multiplication equation")
    elif b!=0 and c!=0:
        if a/b==c or a==b/c:
            print("The numbers satisfy Division equation")
        else:
            continue
    else:
        print("The numbers do not satisfy any equation")
        break

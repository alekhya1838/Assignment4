def maximum(a,b,c):
    if(a>=b)and(a>=c):
        print("maximum is",a)
    elif(b>=a) and (b>=c):
        print("maximum is",b)  
    else:
        print("maximum is",c)  
    return maximum
maximum(10,20,30)         
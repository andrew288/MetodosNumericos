x1 =9
x2 = 7
x3 = 3
y1 = 2
y2 = 8
y3 = 4
z1 = -1
z2 = 5
z3 = -10
r1 = -2
r2 = 3
r3 = 6
error =100.0
x = 0
y = 0 
z = 0
iteraciones = 0
errorX=100
errorY=100
errorZ=100
while(errorX>0.001 and errorY>0.001 and errorY>0.001) :
    iteraciones+=1
    oldx=x
    oldy=y
    oldz=z
    x=(r1-y1*y-z1*z)/x1
    y=(r2-z*z2-x*x2)/y2
    z=(r3-y3*y-x3*x)/z3
    print("Iteración numero: "+str(iteraciones))
    print("x:" + str(x))
    print("y:" + str(y))
    print("z"  + str(z))
    if iteraciones>1:
        errorX = abs((x-oldx)/x)
        errorY = abs((y-oldy)/y)
        errorZ = abs((z-oldz)/z)
        print("el error de x: "+ str(errorX))
        print("el error de y: "+ str(errorY))
        print("el error de z: "+ str(errorZ))
    print("---------------")



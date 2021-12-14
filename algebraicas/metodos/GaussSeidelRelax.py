x1 =5
x2 = 1
x3 = 2
y1 = 1
y2 = 4
y3 = 3
z1 = 2
z2 = -2
z3 = 8
r1 = 19
r2 = -2
r3 = 39
peso = 1.1
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
    x = (r1-y1*y-z1*z)/x1
    tempX =x
    x = peso*tempX+(1-peso)*oldx
    y = (r2-z*z2-x*x2)/y2
    tempY=y
    y = peso*tempY+(1-peso)*oldy
    z = (r3-y3*y-x3*x)/z3
    tempZ=z
    z = peso*tempZ+(1-peso)*oldz
    print("Iteración numero: "+str(iteraciones))
    print("x:" + str(x))
    print("y:" + str(y))
    print("z: "  + str(z))
    if iteraciones>1:
        errorX = abs((x-oldx)/x)
        errorY = abs((y-oldy)/y)
        errorZ = abs((z-oldz)/z)
        print("el error de x: "+ str(errorX))
        print("el error de y: "+ str(errorY))
        print("el error de z: "+ str(errorZ))
    print("---------------")



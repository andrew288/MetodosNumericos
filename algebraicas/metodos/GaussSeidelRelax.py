def metodo_gauss_seidelRelax(data,error,peso):
    print("GAUS SEIDEL RELAJACION")
    a = data
    error =float(error)
    peso = float(peso)
    iteraciones = 0
    errores = [100]*len(a)
    valores = [0]*len(a)
    olds = [0]*len(a)
    confirm = True
    temporales = [0]*len(a)
    #Arreglos para imprimir los valores en la interfaz
    Variables =[]
    Errores = [[100]*len(a)]
    while(confirm) :
        tempVariables =[]
        tempErrores = []
        contadorErrores=0
        #For donde confirmo que todas las variables tienen un error < 0.001
        for i in range(len(errores)):
            if errores[i]<error:
                contadorErrores+=1        
        if contadorErrores==len(a):
            break
        iteraciones+=1
        print("ITERACION "+ str(iteraciones))
        #Matriz provicional para calcular el error: (actual-antiguo)/actual
        for i in range(len(olds)):
            olds[i]=valores[i]
        #For para empezar a iterar y calcular los valores
        for i in range(len(valores)):
            """ print("Valores al empezar en la pos "+str(i)+" es = "+str(valores[i])) """
            result = a[i][len(a[0])-1]
            """ print("result = "+str(result)) """
            for j in range(0,len(a[0])-1):
                if (len(a[0])-j-2)==i:
                    continue
                else:
                    """ print("Result menos ->"+str(a[i][len(a[0])-j-2])+" por "+ str(valores[len(a)-j-1])) """
                    result -= a[i][len(a[0])-j-2]*valores[len(a)-j-1]
            result/=a[i][i]   
            valores[i] = result
            temporales[i] =valores[i]
            #peso*tempX+(1-peso)*oldx
            valores[i] =peso*temporales[i]+(1-peso)*olds[i]
            """ print("Valores en la pos "+str(i)+ " : "+ str(valores[i])) """
        #For que muestra los valores finales de todas nuestras variables
        for i in range(len(valores)):
            print("valores en " +str(i)+" : "+ str(valores[i]))
            tempVariables.append(valores[i])
        Variables.append(tempVariables)
        #Condicional para empezar a calcular el error desde la segunda iteraci??n
        if iteraciones>1:
            for i in range(len(errores)):
                errores[i]=abs((valores[i]-olds[i])/valores[i])
                print("error en "+ str(i)+" : "+str(errores[i]))
                tempErrores.append(errores[i])
            Errores.append(tempErrores)
        
        #Te odio :"v
        print("------------------------") 
    context = {
        "Errores":Errores,
        "Variables": Variables
    }
    return context
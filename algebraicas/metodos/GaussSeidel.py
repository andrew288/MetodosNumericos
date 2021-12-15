def metodo_gauss_seidel(data, Error):
    print("GAUSS SEIDEL ESTRESADO") 
    a = data
    iteraciones = 0
    errores = [100]*len(a)
    valores = [0]*len(a)
    olds = [0]*len(a)
    confirm = True
    #Arreglos para imprimir los valores en la interfaz
    Variables =[]
    Errores = [[100]*len(a)]
    
    while(confirm) :
        tempVariables =[]
        tempErrores = []
        contadorErrores=0
        #For donde confirmo que todas las variables tienen un error < 0.001
        for i in range(len(errores)):
            if errores[i]<float(Error):
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
            """ print("Valores en la pos "+str(i)+ " : "+ str(valores[i])) """

        #For que muestra los valores finales de todas nuestras variables
        for i in range(len(valores)):
            print("valores en " +str(i)+" : "+ str(valores[i]))
            tempVariables.append(valores[i])
            

        #Condicional para empezar a calcular el error desde la segunda iteración
        if iteraciones>1:
            for i in range(len(errores)):
                errores[i]=abs((valores[i]-olds[i])/valores[i])
                tempErrores.append(errores[i])
                print("error en "+ str(i)+" : "+str(errores[i]))
            Errores.append(tempErrores)
        Variables.append(tempVariables)
        print("------------------------------------------------------")
        print("Variables")
        for i in range(len(Variables)):
            for j in range(len(Variables[i])):
                print(Variables[i][j],end=" ")
            print()
        #Te odio :"v
        print("------------------------") 
    context = {
        "Errores":Errores,
        "Variables": Variables,
    }
    return context

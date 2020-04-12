def max_product(A):     
    n=len(A)
    m=0
    B=[]    # Lista de productos
    for i in range (n): # Para cada elemento en la lista
        s=len(A)
        for x in range (i,n):   # Para cada elemento desde el actual
            pr=1    # Limpieza de variable
            for j in range (i,s):   # Desde el elemento actual hasta el último elemnto
                pr*=A[j]
            B.append(pr)    
            s-=1
    #print (B)
    m=max(B)    # Máximo producto obtenido
    return m
        
print (max_product([2,3,-2,4]))

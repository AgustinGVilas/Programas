#Crear función que pida n parámetros y muestre los primeros n números de la sucesión de Fibonacci

def suc_fibo(n):
  if n > 0:  
    lista = [0,1]
    for x in range(1,n):
      lista.append(lista[x-1]+lista[x]) 
    print(lista[0:-1])
  else:
    print([0])

suc_fibo(5)
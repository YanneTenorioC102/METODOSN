#!/usr/bin/env python
# coding: utf-8

# In[1]:


##MÉTODO 1
print ("")
print ("MÉTODO 1: ")
print ("")
import math

x = float(input("Ingrese a qué potencia desea elevar euler: "))
n = int(input("Ingrese el valor de n: "))

def solucion(x, n):
    
    arregloLista = [math.pow(x, i) / math.factorial(i) for i in range(n + 1)]
    return sum(arregloLista)

print ("")
print("Resultado: ", solucion(x, n))


# In[ ]:


## MÉTODO 2
print ("")
print ("MÉTODO 2: ")
print ("")
x=int (input("Ingrese a qué potencia desea elevar euler:"))
n = int (input("Ingrese el valor de n:"))
fact=1
i=0
acumulador=0 
while(i<=n):
    fact=fact*i
    if fact == 0:
        fact =1

    elevar = pow (x,i)
    division = elevar / fact
    acumulador+=division
    i=i+1
print("")
print ("el resultado es:", acumulador)


# In[ ]:


## MÉTODO 3
print ("")
print ("MÉTODO 3: ")
print ("")
x=int (input("Ingrese a qué potencia desea elevar euler:"))
n = int (input("Ingrese el valor de n:"))
fact=1
i=2
acumulador=0
while(i<=n):
    fact=fact*i
    elevar = pow (x,i)
    division = elevar / fact
    acumulador+=division
    i=i+1
print("")
print ("el resultado es", acumulador+ (1+x))
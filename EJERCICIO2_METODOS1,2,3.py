#!/usr/bin/env python
# coding: utf-8

# In[2]:


##MÉTODO 1

import math
print ("")
print ("MÉTODO 1")
print ("")

x = float(input("Ingrese a qué potencia desea elevar euler: "))
n = int(input("Ingrese el valor de n: "))

def solucion(x, n):
    
    arregloLista = [math.pow(x, i) / math.factorial(i) for i in range(n + 1)]
    return 1/sum(arregloLista)

print ("")
print("Resultado: ", solucion(x, n))


# In[4]:


## MÉTODO 2

print ("")
print ("MÉTODO 2")
print ("")

#MÉTODO 1

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
print ("El resultado es:", 1/acumulador)


# In[5]:


## MÉTODO 3

print ("")
print ("MÉTODO 3")
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
  
resultado = 1/(acumulador+ (1+x))
print("")
print ("El resultado es", resultado)


# In[ ]:
import random
import math
from random import sample

def EXPMOD(a, x, n):
  c=a%n
  r=1
  while(x>0):
    if((x%2)!=0):
      r=(r*c)%n
    c=(c*c)%n
    x=int(x/2)
  return r

def es_compuesto(a,n,t,u):
  x=EXPMOD(a,u,n)
  
  if (x==1 or x==n-1):
    return False
  for i in range(1,t,1):
    x=EXPMOD(x,2,n)
    if (x==n-1):
      return False
  return True
  
def MILLER_RABIN(n, s):
  t=0
  u=n-1
  while(u%2==0):
    u=u/2
    t=t+1
  list_a=[]
  nj=0
  while(nj<s):
    a=random.randint(2,n-1)
    if (a not in list_a):
      list_a.append(a)
      nj=nj+1
    
  for h in range(len(list_a)):
    if(es_compuesto(list_a[h],n,t,u)):
      return False
  return True

def Random_bits(b):
  n=(pow(2,b-1)-1)
  n=random.randint(0,b)
  m=pow(2,b-1)+1
  n=n | m
  return n

def Random_primos(b):
  cantidad=[]
  for i in range(10):
    n=Random_bits(b)
    n=n+1-(n%2)
    while(True):
      if(MILLER_RABIN(n, 40)):
        if(n not in cantidad):
          cantidad.append(n)
          break
        else:
          n=n+2
      else:
        n=n+2
  return cantidad
def imprimir(a):
  for i in (a):
    print(i)

print("Primos de 16 bits: ")
print()
a=Random_primos(16)
imprimir(a)
print()
print("Primos de 32 bits: ")
b=Random_primos(32)
print()
imprimir(b)
print()
print("Primos de 64 bits: ")
c=Random_primos(64)
imprimir(c)

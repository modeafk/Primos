import random
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
  a=sample(range(2,n),s)
  for j in range(s):
    if(es_compuesto(a[j],n,t,u)):
      return False
  return True
ini=100 #menor deigito de 3 cifras
fin=99999 #mayor digito de 5 cifras
ini=ini+1-(ini%2)
while(ini<=fin):
  if(MILLER_RABIN(ini,50)):
    print(ini,end=";")
  ini=ini+2

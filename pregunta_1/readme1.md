#GENERANDO NUMEROS PRIMOS

#INTEGRANTES:

-Marcelo Torres Acuña

-Jhon Berly Taype Alccaccahua

-Brian Bermudez Navarro

GENERADOR DE PRIMOS:

Este algoritmo genera numeros primos que estan entre 3 a 5 cifras, el valor que le damos a s en este caso es de 50, esto para que a la hora de que genere los primos tenga una base de que los numeros hallados sean aceptables y tenga una seguridad de que los numeros candidatos a primos en realidad lo sean.

Funciones utilizadas:

- Funcion EXPMOD

![image](https://user-images.githubusercontent.com/90937895/171772814-ee3eb34b-74dc-4e84-8601-ee4861836e0a.png)

EXPMOD nos retorna el residuo "r" de elevar una base "a" a un exponente "x" y seguidamente aplicarle modulo "n"

- Funcion es_compuesto

![image](https://user-images.githubusercontent.com/90937895/171772852-2e1a27a5-75bb-48a3-93e9-876cc01fc9b9.png)

es_compuesto retorna si un numero es compuesto (True) o no (False), haciendo uso tambien de la funcion EXPMOD. Pues si EXPMOD retorna 1 o el numero-1, dicho numero no sera compuesto.

- Funcion MILLER_RABIN

![image](https://user-images.githubusercontent.com/90937895/171772896-e7c47f6d-f146-4da4-b927-5456c4e3390d.png)

MILLER_RABIN, es el test de primalidad para determinar si un número dado es primo, retornando True o False. Teniendo el parametro "s" el cual indica la precision de la prueba.

- MAIN

![image](https://user-images.githubusercontent.com/90937895/171783371-f83a1f2b-2ea8-4c76-8425-0e4cc59af6a6.png)

- Output

![image](https://user-images.githubusercontent.com/101947482/171771179-5641c5da-4af9-4a1b-98ce-4a820ae7d66a.png)

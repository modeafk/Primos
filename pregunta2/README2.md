#INTEGRANTES:

-Marcelo Torres Acuña

-Jhon Berly Taype Alccaccahua

-Brian Bermudez Navarro

Funciones Usadas:

- Funcion EXPMOD

![image](https://user-images.githubusercontent.com/90937895/171772814-ee3eb34b-74dc-4e84-8601-ee4861836e0a.png)

EXPMOD nos retorna el residuo "r" de elevar una base "a" a un exponente "x" y seguidamente aplicarle modulo "n"

- Funcion es_compuesto

![image](https://user-images.githubusercontent.com/90937895/171772852-2e1a27a5-75bb-48a3-93e9-876cc01fc9b9.png)

es_compuesto retorna si un numero es compuesto (True) o no (False), haciendo uso tambien de la funcion EXPMOD. Pues si EXPMOD retorna 1 o el numero-1, dicho numero no sera compuesto.

- Funcion MILLER_RABIN

![image](https://user-images.githubusercontent.com/90937895/171772896-e7c47f6d-f146-4da4-b927-5456c4e3390d.png)

MILLER_RABIN, es el test de primalidad para determinar si un número dado es primo, retornando True o False. Teniendo el parametro "s" el cual indica la precision de la prueba.

- Funcion Random_bits

![image](https://user-images.githubusercontent.com/90937895/171772941-771e5945-6c8f-43f3-b468-33fd3abdfa63.png)

Random_bits, genera los bits (16,32,64) de forma aleatoria retornando "n" el cual seria el menor o mayor valor que podria tomar 

- Funcion Random_primos

![image](https://user-images.githubusercontent.com/90937895/171772991-df748d9f-b432-4f5e-8c3f-dcb2ddb8d253.png)

Random_primos, retorna la lista de los primos de (16,32,64) bits. En nuestro caso hicimos uso de un S de 40, pues es el tiempo mas optimo que vimos por conveniente.

- Funcion imprimir

![image](https://user-images.githubusercontent.com/90937895/171773009-5e852b47-7c24-4895-9219-8619a9c8b265.png)

imprimir, imprime los numeros primos encontrados.

- MAIN

![image](https://user-images.githubusercontent.com/90937895/171773126-9df90034-ebeb-4903-8ed2-fcb112a7496c.png)

- OUTPUT

![image](https://user-images.githubusercontent.com/90937895/171773227-279f7c65-2752-4551-a96a-86980e7a3387.png)

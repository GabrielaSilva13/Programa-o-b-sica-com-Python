## Escreva e execute seu código aqui
n1 = float (input())
operador = input()
n2 = float(input())

if operador =="+":
    resultado = n1+n2
elif operador == "-":
    resultado  = n1-n2  
elif operador == "/":
    resultado  = n1/ n2   
elif operador == "*":
    resultado  = n1*n2    
print (f"{n1}{operador}{n2}={resultado}")  
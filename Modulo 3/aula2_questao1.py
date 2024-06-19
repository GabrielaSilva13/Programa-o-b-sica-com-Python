idade_Gabriela = int (input())
idade_Laura = int (input())

#prosessamento 
#true se ambos forem maior de idade
#<exp1> Juliana é maior de idade
#<exp2> Laura é maior de idade
#<exp1> and <exp2>
#false sem qualquer outro caso

pode_entrar = idade_Gabriela>= 18 and idade_Laura>= 18
print (pode_entrar)
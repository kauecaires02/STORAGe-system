system

#ENTRADA DE DADOS

cpf = input("Digite o cpf: ") 
nome = input ("Digite o nome: ") 
c1= input ("Digite o código: ") 
q1= input ("Digite a qntde: ") 
v1= input ("Digite o valor: ") 
c2= input ("Digite o cód: ") 
q2= input ("Digite a qntde: ") 
v2= input ("Digite o valor: ") 
c3= input ("Digite o cód: ") 
q3= input ("Digite a qntde: ") 
v3= input ("Digite o valor: ")

print ("--------------------------------")

print (" >>>Dados do pedido")

print ("--------------------------------")

#SAÍDA DE DADOS print (": cpf") - cpf print ("nome: ") - nome

print ("ITEM 1") print ("CÓDIGO informado: ") - c1 
print ("QUANTIDADE informado: ") - q1 
print ("VALOR informado: ") - v1

print ("ITEM 2") print ("CÓDIGO informado: ") - c2 
print ("QUANTIDADE informado: ") - q2 
print ("VALOR informado: ") - v2

print ("ITEM 3") print ("CÓDIGO informado: ") - c3 
print ("QUANTIDADE informado: ") - q3 
print ("VALOR informado: ") - v3

total = (int(q1)*float(v1)) + (int(q2)*float(v2)) + (int(q3)*float(v3))

print ("total") str(total)

print ("--------------------------------")


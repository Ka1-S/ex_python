import os

anos = int (input ('Digite sua idade: '))
meses = int (input ('Digite os meses:'))
dias = int (input ('Digite os dias:'))
total_de_dias= anos*365+meses*30+dias
print ('O valor do total de dias: ' + repr (total_de_dias))
print ()
os.system('pause')
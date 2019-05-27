#break = encerra o loop (while ou for) em execução e retoma a próxima instrução. 

#!/usr/bin/python3

contador = 0 
while True:
    print('Execução {}'.format(contador))
    if contador == 100:
        print('Interrompendo o loop com break')
        break
    contador += 1 
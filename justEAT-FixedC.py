import random

alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['1','2','3','4','5','6','7','8','9','0']

qty = int(input("Inserire quanti codici vuoi: "))
posizioni_numeri = [1, 4, 11, 13] 
with open("justeat.txt", "w") as f:
    for i in range(qty):
        codice_lista = []
        for indice in range(16):
            if indice in posizioni_numeri:
                codice_lista.append(random.choice(num))
            else:
                codice_lista.append(random.choice(alp))
        f.write(''.join(codice_lista) + '\n')

print("Fatto! I codici sono pronti.")
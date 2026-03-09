import random
alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['1','2','3','4','5','6','7','8','9','0']
t = alp + num
qty = int(input("Inserire quanti codici vuoi: "))
with open("justeat.txt","w") as f:
    for i in range(0,qty):
        code = ''.join(random.choices(t,k=16))
        f.write(code+'\n')
# koodi parandamine + lisaülesandega koos.

import math #lisasin import, siis programm saab teha matemaatikat.

print("Vali programm")
print("1. Ruutvõrrandid")
print("2. Palga arvutamine")
print("3. Parkimise hind")
num=float(input("Sisesta valik 1-3 => "))
if num==1:
    a=float(input("Sisesta a => "))
    b=float(input("Sisesta b => ")) # Polnud ) lõpus 
    c=float(input("Sisesta c => ")) # polnud float 
    D=b*b-4*a*c
    if D>0: # polnud : lõpus
        x1=(-b+D**0.5)/(2*a) # 2*a polnud sulgudes
        x2=(-b-D**0.5)/(2*a)
        print("Kaks lahendit:", x1, x2)
    elif D==0: # 2 '=' näitab, et see võrdub millegiga ja on elif mitte else if
        x=-b/(2*a)
        print("Üks lahend:", x)
    elif a==0: #lisaülesanne 
        print("Tegemist ei ole ruutvõrrandiga")
    else: 
        print("Reaalarvulised lahendid puuduvad") # polnud else-i all
elif num==2:
    print()
    print("Palga arvutamine")
    tunnid=float(input("Sisesta töötunnid nädalas => "))
    tunnitasu=float(input("Sisesta tunnitasu (€) => "))
    if tunnid<0 and tunnid>168:
        print("Vigane tundide arv")
    elif tunnid<=40:
        palk=tunnid*tunnitasu
        print("Nädalapalk:", palk, "€")
    else:
        palk=40*tunnitasu+(tunnid-40)*tunnitasu*1,5
        print("Nädalapalk koos ületundidega:", palk, "€")
    print()
elif num==3: 
    print("Parkimise hind")
    tunnid=int(input("Sisesta parkimise aeg tundides => "))
    if tunnid<=0: # < peab enne = olema
        print("Vigane aeg")
    elif tunnid>=3:
        print("Hind: 5 €")
    elif tunnid>=8:
        print("Hind: 10 € (päevapilet)")
    else: # polnud : lõpus
        print("Hind: 2 €") # polnud sulgudes
else:
    print("Vigane valik")
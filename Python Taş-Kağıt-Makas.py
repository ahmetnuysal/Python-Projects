#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
seçenekler=["taş","Taş","kağıt","Kağıt","makas","Makas"]

while True:
    try:
        tur=int(input("3 olan mı kazansın? 5 olan mı ?"))
        if tur==3  or tur==5:
            break
        continue
    except error:
        print("Lütfen Geçerli Bir Değer Giriniz!")

kazanan=int(tur/2)+1
OyuncuKazandı=0
BilgisayarKazandı=0

while True:
    while True:
        oyuncu=input("Taş mı?\nKağıt mı?\nMakas mı?\n")
        if oyuncu in seçenekler:
            break
    bilgisayar=random.choice(seçenekler)
    
    if oyuncu==bilgisayar:
        print("Berabere")
    elif oyuncu=="taş" or "Taş" and bilgisayar=="kağıt" or "Kağıt":
        BilgisayarKazandı+=1
        print(f"Bilgisayar Kağıt yaptı,Bilgisayar Kazandı! \n {OyuncuKazandı}-{BilgisayarKazandı}")
    elif oyuncu=="taş" or "Taş" and bilgisayar=="makas" or "Makas":
        OyuncuKazandı+=1
        print(f"Bilgisayar Kağıt yaptı,Siz Kazandınız! \n {OyuncuKazandı}-{BilgisayarKazandı} ")
    elif oyuncu=="kağıt" or "Kağıt" and bilgisayar=="makas" or "Makas":
        BilgisayarKazandı+=1
        print(f"Bilgisayar Makas yaptı,Bilgisayar Kazandı! \n {OyuncuKazandı}-{BilgisayarKazandı} ")
    elif oyuncu=="kağıt" or "Kağıt" and bilgisayar=="taş" or "Taş":
        OyuncuKazandı+=1
        print(f"Bilgisayar Kağıt yaptı, Siz Kazandınız! \n {OyuncuKazandı}-{BilgisayarKazandı} ")
    elif oyuncu=="makas" or "Makas" and bilgisayar=="taş" or "Taş":
        BilgisayarKazandı+=1
        print(f"Bilgisayar Taş yaptı,Bilgisayar Kazandı\n {OyuncuKazandı}-{BilgisayarKazandı} ")
    elif oyuncu=="makas" or "Makas" and bilgisayar=="kağıt" or "Kağıt":
        OyuncuKazandı+=1
        print(f"Bilgisayar Kağıt yaptı, Siz Kazandınız! \n {OyuncuKazandı}-{BilgisayarKazandı} ")
    if OyuncuKazandı==kazanan or BilgisayarKazandı==kazanan:
        break

if  OyuncuKazandı>BilgisayarKazandı:
    print(f"Tebrikler! {OyuncuKazandı}-{BilgisayarKazandı} Kazandınız")
else:
    print(f"Kaybettiniz {OyuncuKazandı}-{BilgisayarKazandı}")


# In[ ]:





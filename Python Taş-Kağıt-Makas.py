import random
seçenekler=["Taş","Kağıt","Makas"]

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
    elif oyuncu=="Taş" and bilgisayar=="Kağıt":
        BilgisayarKazandı+=1
        print(f"Bilgisayar Kağıt yaptı,Bilgisayar Kazandı! \n {OyuncuKazandı}-{BilgisayarKazandı}")
    elif oyuncu=="Taş" and bilgisayar=="Makas":
        OyuncuKazandı+=1
        print(f"Bilgisayar Makas yaptı,Siz Kazandınız! \n {OyuncuKazandı}-{BilgisayarKazandı} ")
    elif oyuncu=="Kağıt" and bilgisayar=="Makas":
        BilgisayarKazandı+=1
        print(f"Bilgisayar Makas yaptı,Bilgisayar Kazandı! \n {OyuncuKazandı}-{BilgisayarKazandı} ")
    elif oyuncu=="Kağıt" and bilgisayar=="Taş":
        OyuncuKazandı+=1
        print(f"Bilgisayar Taş yaptı, Siz Kazandınız! \n {OyuncuKazandı}-{BilgisayarKazandı} ")
    elif oyuncu=="Makas" and bilgisayar=="Taş":
        BilgisayarKazandı+=1
        print(f"Bilgisayar Taş yaptı,Bilgisayar Kazandı\n {OyuncuKazandı}-{BilgisayarKazandı} ")
    elif oyuncu=="Makas" and bilgisayar=="Kağıt":
        OyuncuKazandı+=1
        print(f"Bilgisayar Kağıt yaptı, Siz Kazandınız! \n {OyuncuKazandı}-{BilgisayarKazandı} ")
    if OyuncuKazandı==kazanan or BilgisayarKazandı==kazanan:
        break

if  OyuncuKazandı>BilgisayarKazandı:
    print(f"Tebrikler! {OyuncuKazandı}-{BilgisayarKazandı} Kazandınız")
else:
    print(f"Kaybettiniz {OyuncuKazandı}-{BilgisayarKazandı}")

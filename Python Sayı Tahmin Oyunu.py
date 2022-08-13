#!/usr/bin/env python
# coding: utf-8

# In[ ]:


TahminSayisi= 0
from random import randint
HedefSayi = randint(1, 100)

while True:
    TahminSayisi += 1
    sayi = int(input("1 ile 100 arasında değer girin (0 çıkış): "))
    if(sayi == 0):
        print("Oyunu İptal Ettiniz")
        break
    elif sayi < HedefSayi:
        print("Daha Yüksek Bir Sayı Girin.")
        continue
    elif sayi > HedefSayi:
        print("Daha Düşük Bir Sayı Girin.")
        continue
    else:
        print(f" Tebrikler! Doğru Bildiniz, Rastele seçilen sayı {rand}")
        print(f"Tahmin sayınız {sayac}")


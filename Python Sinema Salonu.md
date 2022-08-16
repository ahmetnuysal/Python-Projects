```python
secim = input("Filmi Seçiniz: ")
ogrenci = input("Öğrenci misiniz(E/H): ")
koltuk = input("Koltuk Numaranızı Giriniz: ")
ucret = 0
 

if secim == 'Thor: Love and Thunder':
  ucret = 30 
elif secim == 'Spider-Man: No Way Home':
  ucret = 35
elif secim == 'Black Panther: Wakanda Forever':
  ucret = 42
elif secim == 'Doctor Strange in the Multiverse of Madnesse':
  ucret = 28
else:
  print("Lütfen Vizyonda Olan Bir Film Seçiniz")
 
if ogrenci =='E' or ogrenci =='e':
  ucret=ucret - ucret *35 / 100 
 
print("Ödemeniz gereken ücret :{ucret}")
```

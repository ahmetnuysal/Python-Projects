```python
def hesaplama(a,b,islem):
    if islem not in "+-*/ sqr sqrroot":
        return "Lütfen geçerli bir işlem seçiniz"
    if islem in "+":
        return a+b
    elif islem in "-":
        return a-b
    elif islem in "*":
        return a*b
    elif islem in "/":
        return a/b
    elif islem in "sqr":
        return a**b
    elif islem in "sqrroot":
        return a**0.5
while True:
    try:
        islem=(input("İşleminizi giriniz:"))
        ilk_numara=int(input("ilk sayıyı giriniz: "))
        ikinci_numara=int(input("ikinci sayıyı giriniz"))
        print(hesaplama(ilk_numara,ikinci_numara,islem))
    except:
        print("Lütfen doğru sayı giriniz")
        break
```

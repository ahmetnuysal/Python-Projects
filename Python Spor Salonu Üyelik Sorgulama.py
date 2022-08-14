üyesayisi=int(input("Yeni Üye Sayısını Giriniz: "))
isim=[]
tarih=[]
sayi=0
while True:

    if üyesayisi==sayi:
        break
    else:
        isim.append(input(str(sayi+1)+"." +"üye ismini giriniz: "))
        tarih.append(input(str(sayi+1)+"."+ " " +"üyenin son üyelik tarihini giriniz: "))
    sayi=1+sayi

istenilen=(input("üye isimini giriniz: "))
for i in isim:
    if istenilen==i:
        istenilenindex=isim.index(istenilen)
        print(tarih[istenilenindex])
        break
    else:
        print("Üye Bulunamadı")
 

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    username=input("Username: ") 
    password=input("Password: ")
    a=0
    def selamlama():
        print(f"Günaydın {username}")
    def hata():
        print("Hatalı Kullanıcı Adı veya Şifre")
    if username=="ahmet" and password=="123123":
        selamlama()
        break
    elif username!="ahmet" or password!="123123":
        hata()

    
    
    


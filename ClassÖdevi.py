#!/usr/bin/env python
# coding: utf-8

# 1.soru

# In[14]:


class Ogrenci:
    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinif):
        self.ogrenci_adi = ogrenci_adi
        self.ogrenci_soyadi = ogrenci_soyadi
        self.ogrenci_sinif = ogrenci_sinif


class Soru(Ogrenci):
    def net_sayisi(self, dogru_sayisi, yanlis_sayisi):
        net = dogru_sayisi - (yanlis_sayisi // 4)

        print("net sayisi :", net)

        return self.hesapla(net)

    def hesapla(self, net_sayisi):
        print("Öğrenci adı : {}\nÖğrenci soyadı : {}\nÖğrencinin sınıfı {}\nOgrenci puani : {}".format
              (self.ogrenci_adi, self.ogrenci_soyadi, self.ogrenci_sinif, net_sayisi * 2))


gs = Ogrenci("Tuğçe", "Balcan", 3)
dogru_sayisi = int(input("dogru sayisini giriniz: "))
yanlis_sayisi = int(input("yanlis sayisini giriniz :"))

if dogru_sayisi + yanlis_sayisi == 50:
    Soru(gs.ogrenci_adi, gs.ogrenci_soyadi, gs.ogrenci_sinif).net_sayisi(dogru_sayisi, yanlis_sayisi)
else:
    print("Hatalı soru adeti girdiniz programdan çıkış yapılıyor!..")


# 2.soru

# In[15]:


class Insan:
    def __init__(self, ad="Ayça", soyad="Balcan", yas=30, ulke="Turkiye", sehir="Istanbul"):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)

        return self


gs = Insan("Tuğçe", "Balcan", 23, "Türkiye", "Istanbul")
gs.yetenek_ekle("gymnastic")
gs.yetenek_ekle("Dance")
print(gs.kisi_bilgileri())


# 

# In[ ]:





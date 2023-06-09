import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

# İnsan sınıfı için 2 nesne oluşturma ve bilgileri yazdırma
insan1 = Insan("123456789", "Ali", "Yılmaz", 25, "Erkek", "Türk")
insan2 = Insan("987654321", "Ayşe", "Demir", 30, "Kadın", "Türk")
print("İnsan Nesnesi 1:")
print(insan1.__str__())
print("İnsan Nesnesi 2:")
print(insan2.__str__())
print("----------------------------------------")

# İşsiz sınıfı için 3 nesne oluşturma ve bilgileri yazdırma
issiz1 = Issiz("1111111111", "Ali", "Can", 35, "Erkek", "Türk", mavi_yaka_tecrube=3, beyaz_yaka_tecrube=1)
issiz2 = Issiz("2222222222", "Ayşe", "Kara", 28, "Kadın", "Türk", mavi_yaka_tecrube=0, beyaz_yaka_tecrube=2)
issiz3 = Issiz("3333333333", "Mehmet", "Şimşek", 40, "Erkek", "Türk", mavi_yaka_tecrube=2, beyaz_yaka_tecrube=4)
print("İşsiz Nesneleri")
print("----------------------------------------")
print(issiz1.__str__())
print("----------------------------------------")
print(issiz2.__str__())
print("----------------------------------------")
print(issiz3.__str__())
print("----------------------------------------")

# Çalışan sınıfı için 3 nesne oluşturma ve bilgileri yazdırma
calisan1 = Calisan("444444444", "Ayhan", "Aydın", 32, "Erkek", "Türk", "Bankacılık", 5, 12000)
calisan2 = Calisan("555555555", "Deniz", "Kılıç", 28, "Kadın", "Türk", "Bilişim", 2, 8000)
calisan3 = Calisan("666666666", "Kemal", "Demir", 38, "Erkek", "Türk", "Mühendislik", 10, 18000)
print("Çalışan Nesnesi 1:")
print(calisan1.__str__())
print("Çalışan Nesnesi 2:")
print(calisan2.__str__())
print("Çalışan Nesnesi 3:")
print(calisan3.__str__())
print("----------------------------------------")

# MaviYaka sınıfı için 3 nesne oluşturma ve bilgileri yazdırma
maviyaka1 = MaviYaka("777777777", "Selin", "Kaya", 29, "Kadın", "Türk", "Üretim", 4, 10000, 500)
maviyaka2 = MaviYaka("888888888", "Ahmet", "Yılmaz", 35, "Erkek", "Türk", "Lojistik", 6, 15000, 600)
maviyaka3 = MaviYaka("999999999", "Elif", "Demir", 31, "Kadın", "Türk", "Gıda", 3, 9000, 400)
print("Mavi Yaka Nesnesi 1:")
print(maviyaka1.__str__())
print("Mavi Yaka Nesnesi 2:")
print(maviyaka2.__str__())
print("Mavi Yaka Nesnesi 3:")
print(maviyaka3.__str__())
print("----------------------------------------")

    # BeyazYaka sınıfı için 3 nesne oluşturma ve bilgileri yazdırma
beyazyaka1 = BeyazYaka("101010101", "Ali", "Yılmaz", 33, "Erkek", "Türk", "Muhasebe", 4, 12000, 1000)
beyazyaka2 = BeyazYaka("202020202", "Ayşe", "Demir", 29, "Kadın", "Türk", "Pazarlama", 7, 16000, 1200)
beyazyaka3 = BeyazYaka("303030303", "Mehmet", "Kara", 36, "Erkek", "Türk", "Hukuk", 5, 14000, 800)
print("Beyaz Yaka Nesnesi 1:")
print(beyazyaka1.__str__())
print("Beyaz Yaka Nesnesi 2:")
print(beyazyaka2.__str__())
print("Beyaz Yaka Nesnesi 3:")
print(beyazyaka3.__str__())
print("----------------------------------------")

    # DataFrame oluşturma

data = {
    "Nesne Değeri": ["Çalışan", "Çalışan", "Çalışan", "Mavi Yaka", "Mavi Yaka", "Mavi Yaka"],
    "TC No": [calisan1.get_tc_no(), calisan2.get_tc_no(), calisan3.get_tc_no(), maviyaka1.get_tc_no(), maviyaka2.get_tc_no(), maviyaka3.get_tc_no()],
    "Ad": [calisan1.get_ad(), calisan2.get_ad(), calisan3.get_ad(), maviyaka1.get_ad(), maviyaka2.get_ad(), maviyaka3.get_ad()],
    "Soyad": [calisan1.get_soyad(), calisan2.get_soyad(), calisan3.get_soyad(), maviyaka1.get_soyad(), maviyaka2.get_soyad(), maviyaka3.get_soyad()],
    "Yaş": [calisan1.get_yas(), calisan2.get_yas(), calisan3.get_yas(), maviyaka1.get_yas(), maviyaka2.get_yas(), maviyaka3.get_yas()],
    "Cinsiyet": [calisan1.get_cinsiyet(), calisan2.get_cinsiyet(), calisan3.get_cinsiyet(), maviyaka1.get_cinsiyet(), maviyaka2.get_cinsiyet(), maviyaka3.get_cinsiyet()],
    "Uyruk": [calisan1.get_uyruk(), calisan2.get_uyruk(), calisan3.get_uyruk(), maviyaka1.get_uyruk(), maviyaka2.get_uyruk(), maviyaka3.get_uyruk()],
    "Sektör": [calisan1.get_sektor(), calisan2.get_sektor(), calisan3.get_sektor(), maviyaka1.get_sektor(), maviyaka2.get_sektor(), maviyaka3.get_sektor()],
    "Tecrübe (Yıl)": [calisan1.get_tecrube() // 12, calisan2.get_tecrube() // 12, calisan3.get_tecrube() // 12, maviyaka1.get_tecrube() // 12, maviyaka2.get_tecrube() // 12, maviyaka3.get_tecrube() // 12],
    "Maaş": [calisan1.get_maas(), calisan2.get_maas(), calisan3.get_maas(), maviyaka1.get_maas(), maviyaka2.get_maas(), maviyaka3.get_maas()],
    "Yıpranma Payı": [0, 0, 0, maviyaka1.get_yipranma_payi(), maviyaka2.get_yipranma_payi(), maviyaka3.get_yipranma_payi()],
    "Teşvik Prim": [0, 0, 0, 0, 0, 0],
    "Yeni Maaş": [calisan1.zam_hakki(), calisan2.zam_hakki(), calisan3.zam_hakki(), maviyaka1.zam_hakki(), maviyaka2.zam_hakki(), maviyaka3.zam_hakki()]
}

# DataFrame oluşturun
df = pd.DataFrame(data)


    # b) Çalışan, mavi yaka ve beyaz yaka için gruplandırarak tecrübe ve yeni maaş ortalamalarını her grup için hesaplayınız ve yazdırınız.

# Grupları oluştur
gruplar = df.groupby("Nesne Değeri")

# Grupların tecrübe ve yeni maaş ortalamalarını hesapla
ortalamalar = gruplar["Tecrübe (Yıl)", "Yeni Maaş"].mean()

# Ortalamaları yazdır
print(ortalamalar)

    # c) Maaşı 15000TL üzerinde olanların toplam sayısını bulunuz.

# Maaşı 15000TL üzerinde olanları seç
ust_limit_sayisi = df[df["Maaş"] > 15000].shape[0]

# Sonucu yazdır
print(f"Maaşı {15000} TL üzerinde olanların sayısı: {ust_limit_sayisi}")

    # d) Yeni maaşa göre DataFrame’i küçükten büyüğe sıralayınız ve yazdırınız.

# Yeni maaşa göre DataFrame'i sırala
df_sirali = df.sort_values("Yeni Maaş")

# Sıralanmış DataFrame'i yazdır
print(df_sirali)

    # e) Tecrübesi 3 seneden fazla olan Beyaz yakalıları bulunuz ve yazdırınız.

# Tecrübesi 3 seneden fazla olan Beyaz yakalıları seç

tecrube_filtre = (df["Nesne Değeri"] == "Beyaz Yaka") & (df["Tecrübe (Yıl)"] > 3)
beyaz_yakalar = df[tecrube_filtre]

# Beyaz yakaları yazdır
print(beyaz_yakalar)

    # f) Yeni maaşı 10000 TL üzerinde olanlar için; 2-5 satır arası olanları, tc_no ve yeni_maaş sütunlarını seçerek gösteriniz ve yazdırınız.

# Yeni maaşı 10000 TL üzerinde olanları seç
maas_filtre = df["Yeni Maaş"] > 10000
ust_limitli_nesneler = df[maas_filtre]

# 2-5 satırları seçerek tc_no ve yeni_maaş sütunlarını göster
secilen_satirlar = ust_limitli_nesneler.iloc[2:5, [1, -1]]

# Sonucu yazdır
print(secilen_satirlar)

    # g) Var olan DataFrame’den ad, soyad, sektör ve yeni maaşı içeren yeni bir DataFrame elde ediniz ve yazdırınız
# Yeni DataFrame'i oluştur
yeni_df = df[["Ad", "Soyad", "Sektör", "Yeni Maaş"]]

# Yeni DataFrame'i yazdır
print(yeni_df)


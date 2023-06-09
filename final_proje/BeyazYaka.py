from Calisan import Calisan
class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = tesvik_primi

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = tesvik_primi

    def zam_hakki(self):
        if self.get_tecrube() < 2:
            return self.__tesvik_primi
        elif self.get_tecrube() >= 2 and self.get_tecrube() <= 4 and self.get_maas() < 15000:
            return (self.get_maas() * self.get_tecrube() / 100) * 5 + self.__tesvik_primi
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            return (self.get_maas() * self.get_tecrube() / 100) * 4 + self.__tesvik_primi
        else:
            return self.get_maas()

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nYaş: {self.get_yas()}\nCinsiyet: {self.get_cinsiyet()}\nUyruk: {self.get_uyruk()}\nSektör: {self.get_sektor()}\nTecrübe: {self.get_tecrube()} ay\nYeni Maaş: {self.zam_hakki()} TL"


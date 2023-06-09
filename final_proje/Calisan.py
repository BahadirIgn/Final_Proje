from Insan import Insan
class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk)
        self.__sektor = sektor
        self.__tecrube = tecrube
        self.__maas = maas

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = sektor

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas

    def zam_hakki(self):
        if self.__tecrube < 2:
            return self.__maas
        elif self.__tecrube >= 2 and self.__tecrube <= 4 and self.__maas < 15000:
            return self.__maas + (self.__maas * self.__tecrube / 100)
        elif self.__tecrube > 4 and self.__maas < 25000:
            return self.__maas + (self.__maas * self.__tecrube / 200)
        else:
            return self.__maas

    def __str__(self):
        return f" Ad: {self.get_ad()}\n Soyad: {self.get_soyad()}\n Yaş: {self.get_yas()}\n Cinsiyet: {self.get_cinsiyet()}\n Uyruk: {self.get_uyruk()}\n Sektör: {self.__sektor}\n Tecrübe: {self.__tecrube} ay\n Yeni Maaş: {self.zam_hakki()} TL"


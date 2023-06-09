from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yaş, cinsiyet, uyruk, mavi_yaka_tecrube=0, beyaz_yaka_tecrube=0):
        super().__init__(tc_no, ad, soyad, yaş, cinsiyet, uyruk)
        self.__mavi_yaka_tecrube = mavi_yaka_tecrube
        self.__beyaz_yaka_tecrube = beyaz_yaka_tecrube

    def get_mavi_yaka_tecrube(self):
        return self.__mavi_yaka_tecrube

    def set_mavi_yaka_tecrube(self, mavi_yaka_tecrube):
        self.__mavi_yaka_tecrube = mavi_yaka_tecrube

    def get_beyaz_yaka_tecrube(self):
        return self.__beyaz_yaka_tecrube

    def set_beyaz_yaka_tecrube(self, beyaz_yaka_tecrube):
        self.__beyaz_yaka_tecrube = beyaz_yaka_tecrube

    def statu_bul(self):
        mavi_yaka_etkisi = 0.2
        beyaz_yaka_etkisi = 0.35

        mavi_yaka_puan = self.__mavi_yaka_tecrube * mavi_yaka_etkisi
        beyaz_yaka_puan = self.__beyaz_yaka_tecrube * beyaz_yaka_etkisi

        if mavi_yaka_puan > beyaz_yaka_puan:
            return "Mavi Yaka"
        elif beyaz_yaka_puan > mavi_yaka_puan:
            return "Beyaz Yaka"
        else:
            return "Eşit puan, statü belirlenemiyor"

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nYaş: {self.get_yas()}\nCinsiyet: {self.get_cinsiyet()}\nUyruk: {self.get_uyruk()}\nEn Uygun Statü: {self.statu_bul()}"

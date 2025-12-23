# Isparta 18 Noktalı Veri Seti
TOPLANMA_ALANLARI = {
    "Isparta Ulu Camii (MERKEZ)": (37.7635, 30.5568),
    "Şehit Ferhat Çiftçi Okulu": (37.7883, 30.5492),
    "Isparta Anadolu Lisesi": (37.7859, 30.5543),
    "Kutlubey Emniyet Önü": (37.7676, 30.5533),
    "Ahmet Hilmi Yiğit Lisesi": (37.7684, 30.5547),
    "Akkent Parkı": (37.8178, 30.5781),
    "Şehit Sezgin Uludağ Okulu": (37.7679, 30.5447),
    "Bağlar Mahallesi": (37.7688, 30.5470),
    "AFAD İl Müdürlüğü": (37.7648, 30.5566),
    "Atatürk Stadyumu": (37.7595, 30.5537),
    "Kaymakkapı Meydanı": (37.7676, 30.5519),
    "15 Temmuz Demokrasi M.": (37.7632, 30.5522),
    "Gülcü Parkı": (37.7588, 30.5478),
    "SDÜ Doğu Kampüsü": (37.8456, 30.5312),
    "1500 Evler Parkı": (37.7512, 30.5598),
    "Şehir Hastanesi": (37.7892, 30.5234),
    "Davraz Yolu": (37.7734, 30.5123),
    "Ayazmana Mesire": (37.7498, 30.5712)
}

def get_coordinates():
    return list(TOPLANMA_ALANLARI.values())

def get_names():
    return list(TOPLANMA_ALANLARI.keys())

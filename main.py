import streamlit as st
from data.coordinates import get_coordinates, get_names
from core.matrix_utils import mesafe_matrisi_olustur
from core.ant_algorithm import KarincaKolonisiOptimizasyonu
from visual.plotting import harita_ciz
import config

# Verileri Yükle
koordinatlar = get_coordinates()
isimler = get_names()

# Matrisi Oluştur
matris = mesafe_matrisi_olustur(koordinatlar)

# Algoritmayı Çalıştır
aco = KarincaKolonisiOptimizasyonu(
    matris, 
    config.KARINCA_SAYISI, 
    config.ITERASYON, 
    config.ALPHA, 
    config.BETA, 
    config.RHO, 
    config.Q, 
    config.BASLANGIC_FEROMON
)

rota, mesafe, gecmis = aco.optimize()

# Sonuçları Göster
print(f"En Kısa Mesafe: {mesafe} km")
harita_ciz(rota, koordinatlar, isimler)

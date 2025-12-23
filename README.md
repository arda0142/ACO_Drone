
```markdown
# 🚁 ACO Tabanlı Drone Rota Optimizasyonu (Senaryo 8)

> **Isparta İli Afet ve Acil Durum Toplanma Alanları için Otonom Nakliye Rotası**

Bu proje, **BLG-307 Yapay Zeka Sistemleri** dersi kapsamında, Isparta merkezindeki kritik noktalara acil durum malzemesi taşıyacak bir drone için en kısa ve verimli rotayı **Karınca Kolonisi Optimizasyonu (Ant Colony Optimization - ACO)** algoritması kullanarak hesaplar.

---

## 👤 Künye
| **Öğrenci** | Arda Özkaya |
| **Numara** | 2312721008 |
| **Ders** | Yapay Zeka Sistemleri (Doç.Dr.Sinan Uğuz) |
| **Senaryo** | No: 8 (Isparta Afet Lojistiği) |
| **Dönem** | 2024-2025 Güz |

---

## 🎯 Projenin Amacı ve Kapsamı
Bir afet durumunda yolların kapanma ihtimaline karşı **havadan (kuş uçuşu)** nakliye hayati önem taşır. Bu proje şunları hedefler:
1.  **Gerçek Veri:** Isparta'daki Ulu Camii, Okullar, Hastaneler ve Parklar dahil **18 farklı lokasyonu** kapsar.
2.  **Optimizasyon:** Gezgin Satıcı Problemini (TSP) doğadan esinlenen ACO algoritması ile çözer.
3.  **Görselleştirme:** Rotayı ve algoritmanın öğrenme sürecini interaktif grafiklerle sunar.

---

## 🛠️ Teknik Mimari ve Klasör Yapısı
Proje, hocanın belirlediği modüler dosya yapısına uygun olarak geliştirilmiştir. GitHub deposunda aşağıdaki yapı bulunmaktadır:

```text
aco_drone_rotasi/
├── 📄 AntColony.ipynb       # ANA DOSYA (Tüm kod, analiz ve haritalar burada)
├── 📄 requirements.txt      # Gerekli kütüphane listesi
├── 📄 README.md             # Proje dokümantasyonu
└── (Sanal Ortam Klasörleri - Colab içinde oluşturulur)
    ├── core/                # Algoritma mantığı (ACO Class)
    ├── data/                # Koordinat verileri (18 Nokta)
    └── visual/              # Harita ve grafik çizim araçları

```

---

## 🧠 Algoritma Detayları (ACO)

Karıncaların feromon bırakarak en kısa yolu bulma davranışını simüle eden bu sistemde kullanılan parametreler:

| Parametre | Değer | Açıklama |
| --- | --- | --- |
| **Karınca Sayısı** | `20` | Her turda rota arayan ajan sayısı. |
| **İterasyon** | `100` | Algoritmanın kendini geliştirme döngüsü. |
| **Alpha (α)** | `1.0` | Feromon izinin (tecrübenin) karara etkisi. |
| **Beta (β)** | `3.0` | Mesafenin (yerel sezginin) karara etkisi. |
| **Buharlaşma (ρ)** | `0.5` | Eski izlerin silinme hızı (Tuzağa düşmeyi engeller). |

---

## 📍 Rota ve Lokasyonlar

Proje, Isparta merkezli **18 kritik noktayı** birbirine bağlar. Başlangıç noktası **Isparta Ulu Camii** olarak belirlenmiştir.

* **Eğitim Kurumları:** Şehit Ferhat Çiftçi Okulu, Anadolu Lisesi vb.
* **Kamusal Alanlar:** Valilik, Emniyet, Kaymakkapı Meydanı.
* **Sağlık ve Afet:** Şehir Hastanesi, AFAD İl Müdürlüğü.
* **Yeşil Alanlar:** Akkent Parkı, Ayazmana Mesire Alanı.

---

## 📊 Sonuçlar

### 1. Rota Başarısı

Algoritma başlangıçta rastgele rotalarla **34.8 km** civarında gezinirken, 100 iterasyon sonunda optimum rotayı bularak mesafeyi **33.456 km** seviyesine indirmiştir.

### 2. Görsel Çıktılar

*(Not: Bu görseller `AntColony.ipynb` dosyası çalıştırıldığında dinamik olarak üretilir.)*

* **Yakınsama Grafiği:** Algoritmanın her adımda nasıl daha iyi bir yol bulduğunu gösteren basamaklı iniş grafiği.
* **Dinamik Harita:** Başlangıç noktasının (Yeşil) ve diğer durakların (Mavi) işaretlendiği, rotanın (Kırmızı) çizildiği HTML haritası.

---

## 🚀 Nasıl Çalıştırılır?

Bu projeyi kendi bilgisayarınızda veya tarayıcıda çalıştırmak için:

1. **Google Colab'i Açın:** [Google Colab](https://colab.research.google.com/) adresine gidin.
2. **Dosyayı Yükleyin:** Bu depodaki `AntColony.ipynb` dosyasını Colab'e yükleyin (Upload).
3. **Çalıştırın:** Menüden **"Çalışma Zamanı > Tümünü Çalıştır"** (Runtime > Run All) seçeneğine tıklayın.
4. **Sonuç:** Kod otomatik olarak gerekli kütüphaneleri (`pydeck` vb.) yükleyecek ve haritayı ekrana çizecektir.

---

## 📚 Kaynakça

1. *Dorigo, M. (1992). Optimization, Learning and Natural Algorithms.*
2. *Google Maps API & Haversine Formula Documentation.*
3. *Isparta Belediyesi ve AFAD Resmi Web Siteleri (Koordinat Doğrulaması).*

---

**Lisans:** Bu proje eğitim amaçlıdır ve açık kaynak olarak sunulmuştur.

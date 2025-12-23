import numpy as np
import random

class KarincaKolonisiOptimizasyonu:
    def __init__(self, mesafe_matrisi, n_karinca, n_iterasyon, alpha, beta, rho, q, baslangic_feromon):
        self.mesafe = mesafe_matrisi
        self.n_sehir = len(mesafe_matrisi)
        self.n_karinca = n_karinca
        self.n_iterasyon = n_iterasyon
        self.alpha = alpha
        self.beta = beta
        self.rho = rho
        self.q = q
        
        self.feromon = np.full((self.n_sehir, self.n_sehir), baslangic_feromon)
        self.gorunurluk = np.zeros((self.n_sehir, self.n_sehir))
        
        for i in range(self.n_sehir):
            for j in range(self.n_sehir):
                if i != j and self.mesafe[i][j] > 0:
                    self.gorunurluk[i][j] = 1.0 / self.mesafe[i][j]
        
        self.en_iyi_rota = None
        self.en_iyi_mesafe = float('inf')
        self.mesafe_gecmisi = []
    
    def _sonraki_sehir_sec(self, mevcut, ziyaret_edilenler):
        ziyaret_edilmemisler = [s for s in range(self.n_sehir) if s not in ziyaret_edilenler]
        if not ziyaret_edilmemisler: return None
        
        olasiliklar = []
        for sehir in ziyaret_edilmemisler:
            tau = self.feromon[mevcut][sehir]
            eta = self.gorunurluk[mevcut][sehir]
            olasiliklar.append((tau ** self.alpha) * (eta ** self.beta))
        
        toplam = sum(olasiliklar)
        if toplam == 0:
            olasiliklar = [1.0 / len(ziyaret_edilmemisler)] * len(ziyaret_edilmemisler)
        else:
            olasiliklar = [p / toplam for p in olasiliklar]
        
        return random.choices(ziyaret_edilmemisler, weights=olasiliklar, k=1)[0]
    
    def optimize(self):
        for _ in range(self.n_iterasyon):
            tum_rotalar = []
            tum_mesafeler = []
            
            for _ in range(self.n_karinca):
                rota = [0] # Başlangıç: Ulu Cami (0)
                ziyaret_edilenler = {0}
                mevcut = 0
                while len(ziyaret_edilenler) < self.n_sehir:
                    sonraki = self._sonraki_sehir_sec(mevcut, ziyaret_edilenler)
                    rota.append(sonraki)
                    ziyaret_edilenler.add(sonraki)
                    mevcut = sonraki
                
                # Mesafe hesapla
                mesafe = 0
                for i in range(len(rota)-1):
                    mesafe += self.mesafe[rota[i]][rota[i+1]]
                mesafe += self.mesafe[rota[-1]][rota[0]]
                
                tum_rotalar.append(rota)
                tum_mesafeler.append(mesafe)
                
                if mesafe < self.en_iyi_mesafe:
                    self.en_iyi_mesafe = mesafe
                    self.en_iyi_rota = rota.copy()
            
            # Feromon güncelle
            self.feromon *= (1 - self.rho)
            for rota, dist in zip(tum_rotalar, tum_mesafeler):
                delta = self.q / dist
                for i in range(len(rota)-1):
                    self.feromon[rota[i]][rota[i+1]] += delta
                    self.feromon[rota[i+1]][rota[i]] += delta
                self.feromon[rota[-1]][rota[0]] += delta
                self.feromon[rota[0]][rota[-1]] += delta
            
            self.mesafe_gecmisi.append(self.en_iyi_mesafe)
            
        return self.en_iyi_rota, self.en_iyi_mesafe, self.mesafe_gecmisi

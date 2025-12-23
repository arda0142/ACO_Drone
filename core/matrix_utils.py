import numpy as np
from core.haversine import haversine

def mesafe_matrisi_olustur(koordinatlar):
    n = len(koordinatlar)
    matris = np.zeros((n, n))
    
    for i in range(n):
        for j in range(n):
            if i != j:
                matris[i][j] = haversine(koordinatlar[i], koordinatlar[j])
    
    return matris

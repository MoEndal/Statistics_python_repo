import math
from statistics import mean, median, mode


lista_str = input("Syötä luvut ja erota ne pilkulla: ")
lista_pilk_ero = (lista_str.split(","))
print(lista_pilk_ero)

# Muutetaan luvut numeroiksi
lista = []
for luku in lista_pilk_ero:
    lista.append(float(luku))

# Tulostetaan min ja max
maksimi = max(lista)
minimi = min(lista)
keskiarvo = mean(lista)
mediaani = median(lista)
moodi = mode(lista)

print(f'Maximi {maksimi}\nMinimi {minimi}\nKeskiarvo {keskiarvo}\nMediaani {mediaani}\nMoodi {moodi}')
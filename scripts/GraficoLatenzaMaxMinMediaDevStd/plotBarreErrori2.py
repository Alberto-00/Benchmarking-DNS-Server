from audioop import maxpp
from re import M
import matplotlib.pyplot as plt
import numpy as np
import sys
plt.rcParams["figure.figsize"] = [10, 22]
plt.rcParams["figure.autolayout"] = True
#mediaBIND minBind maxBind mediaPDNS minPdns maxpdns mediaTech minTech maxTech devBIND devPDNS devTech 
mediaBind = float(sys.argv[1])
minBind = float(sys.argv[2])
maxBind = float(sys.argv[3])

mediaPdns = float(sys.argv[4])
minPdns = float(sys.argv[5])
maxPdns = float(sys.argv[6])

mediaTech = float(sys.argv[7])
minTech = float(sys.argv[8])
maxTech = float(sys.argv[9])

bindStddev = float(sys.argv[10])
pdnsStddev = float(sys.argv[11])
techStddev = float(sys.argv[12])

print(mediaBind,minBind,maxBind)
print(mediaPdns,minPdns,maxPdns)
print(mediaTech,minTech,maxTech)
print(bindStddev,pdnsStddev,techStddev)


# Dati di esempio
categorie = ['BIND', 'PowerDNS', 'Technitium']
media = [mediaBind, mediaPdns, mediaTech]
deviazione_standard = [bindStddev, pdnsStddev, techStddev]
valore_massimo = [maxBind, maxPdns, maxTech]
valore_minimo = [minBind, minPdns, minTech]

# Converti categorie in numeri interi per evitare errori di tipo
categories = np.arange(len(categorie))

# Creazione del grafico a barre con errori
fig, ax = plt.subplots()

# Barre principali per la media
ax.bar(categories, media, yerr=deviazione_standard, capsize=4, label='Media')

# Linee orizzontali per il valore massimo e minimo
#ax.hlines(valore_massimo, categories - 0.2, categories + 0.2, colors='r', linestyles='dashed', label='Valore Massimo')
ax.hlines(valore_minimo, categories - 0.2, categories + 0.2, colors='y', linestyles='dashed', label='Valore Minimo')

# Impostazioni grafiche
ax.set_xticks(categories)
ax.set_xticklabels(categorie)
ax.set_ylabel('Latenza')
ax.set_title(sys.argv[13])
ax.legend(loc='upper left')
#plt.yticks(np.arange(0,0.70,0.005))

#ax.text(0.5, -0.15, "paragrafo", ha='center', va='center', transform=ax.transAxes, fontsize=8)
ax.text(1.05, 0.5, "BIND max: "+str(maxBind)+"\nPowerDNS max: "+str(maxPdns)+"\nTechnitium max: "+str(maxTech), transform=ax.transAxes, ha='left', va='center', fontsize=12)

#ax.text(categories[0], maxBind, "BIND valore massimo: "+str(maxBind), ha='center', va='bottom', rotation=0, fontsize=8)

# Mostra il grafico
plt.savefig(sys.argv[14])


import numpy as np
import sys
from audioop import maxpp
from re import M
import matplotlib.pyplot as plt
import numpy as np


#fileBind filePdns fileTech titolo nomeimg
# Leggi i numeri dal file txt
with open(sys.argv[1], 'r') as fileBind:
    numbersBind = [float(num) for num in fileBind.readline().split(',')]

# Calcola e stampa il valore minimo, massimo, media e deviazione standard
min_value_bind = np.min(numbersBind)
max_value_bind = np.max(numbersBind)
mean_value_bind = np.mean(numbersBind)
std_dev_bind = np.std(numbersBind)


with open(sys.argv[2], 'r') as filePDNS:
    numbersPDNS = [float(num) for num in filePDNS.readline().split(',')]

# Calcola e stampa il valore minimo, massimo, media e deviazione standard
min_value_pdns = np.min(numbersPDNS)
max_value_pdns = np.max(numbersPDNS)
mean_value_pdns = np.mean(numbersPDNS)
std_dev_pdns = np.std(numbersPDNS)

with open(sys.argv[3], 'r') as fileTech:
    numbersTech = [float(num) for num in fileTech.readline().split(',')]

# Calcola e stampa il valore minimo, massimo, media e deviazione standard
min_value_tech = np.min(numbersTech)
max_value_tech = np.max(numbersTech)
mean_value_tech = np.mean(numbersTech)
std_dev_tech = np.std(numbersTech)




plt.rcParams["figure.figsize"] = [10, 22]
plt.rcParams["figure.autolayout"] = True
#mediaBIND minBind maxBind mediaPDNS minPdns maxpdns mediaTech minTech maxTech devBIND devPDNS devTech 


# Dati di esempio
categorie = ['BIND', 'PowerDNS', 'Technitium']
media = [mean_value_bind, mean_value_pdns, mean_value_tech]
deviazione_standard = [std_dev_bind, std_dev_pdns, std_dev_tech]
valore_massimo = [max_value_bind, max_value_pdns, max_value_tech]
valore_minimo = [min_value_bind, min_value_pdns, min_value_tech]

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
ax.set_title(sys.argv[4])
ax.legend(loc='upper left')
#plt.yticks(np.arange(0,0.70,0.005))

#ax.text(0.5, -0.15, "paragrafo", ha='center', va='center', transform=ax.transAxes, fontsize=8)
ax.text(1.05, 0.5, "BIND max: "+str(max_value_bind)+"\nPowerDNS max: "+str(max_value_pdns)+"\nTechnitium max: "+str(max_value_tech), transform=ax.transAxes, ha='left', va='center', fontsize=12)

#ax.text(categories[0], maxBind, "BIND valore massimo: "+str(maxBind), ha='center', va='bottom', rotation=0, fontsize=8)

# Mostra il grafico
plt.savefig(sys.argv[5])


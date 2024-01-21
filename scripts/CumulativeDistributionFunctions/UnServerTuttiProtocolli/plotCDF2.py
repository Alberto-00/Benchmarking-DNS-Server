# titoloGrafico NomeImg udp tcp tls https dnssec 
from cProfile import label
from operator import le
import numpy as np 
import sys
import matplotlib.pyplot as plt 
#import pandas as pd 
#%matplotlib inline 
plt.rcParams["figure.figsize"] = [55.00, 10]
plt.rcParams["figure.autolayout"] = True

# No of Data points 
#N = 250
# Apri il file in modalità lettura
with open(sys.argv[3], 'r') as fileUDP:
    # Leggi il contenuto del file
    contentUDP = fileUDP.read().rstrip(',')

# Suddividi i numeri in una lista
numbersUDP = [float(num) for num in contentUDP.split(',')]

with open(sys.argv[4], 'r') as fileTCP:
    # Leggi il contenuto del file
    contentTCP = fileTCP.read().rstrip(',')

# Suddividi i numeri in una lista
numbersTCP = [float(num) for num in contentTCP.split(',')]

with open(sys.argv[5], 'r') as fileTLS:
    # Leggi il contenuto del file
    contentTLS = fileTLS.read().rstrip(',')

# Suddividi i numeri in una lista
numbersTLS = [float(num) for num in contentTLS.split(',')]

with open(sys.argv[6], 'r') as fileHTTPS:
    # Leggi il contenuto del file
    contentHTTPS = fileHTTPS.read().rstrip(',')

# Suddividi i numeri in una lista
numbersHTTPS = [float(num) for num in contentHTTPS.split(',')]

with open(sys.argv[7], 'r') as fileDNSSEC:
    # Leggi il contenuto del file
    contentDNSSEC = fileDNSSEC.read().rstrip(',')

# Suddividi i numeri in una lista
numbersDNSSEC = [float(num) for num in contentDNSSEC.split(',')]


Nudp = len(numbersUDP)
Ntcp = len(numbersTCP)
Ntls = len(numbersTLS)
Nhttps = len(numbersHTTPS)
Ndnssec = len(numbersDNSSEC)

print(numbersUDP[:10])
print(numbersTCP[:10])
print(numbersTLS[:10])
print(numbersHTTPS[:10])
print(numbersDNSSEC[:10])


countUDP, bins_count_UDP = np.histogram(numbersUDP, bins=len(numbersUDP))
countTCP, bins_count_TCP = np.histogram(numbersTCP, bins=len(numbersTCP))
countTLS, bins_count_TLS = np.histogram(numbersTLS, bins=len(numbersTLS))
countHTTPS, bins_count_HTTPS = np.histogram(numbersHTTPS, bins=len(numbersHTTPS))
countDNSSEC, bins_count_DNSSEC = np.histogram(numbersDNSSEC, bins=len(numbersDNSSEC))

pdfUDP = countUDP / sum(countUDP)
pdfTCP = countTCP / sum(countTCP)
pdfTLS = countTLS / sum(countTLS)
pdfHTTPS = countHTTPS / sum(countHTTPS)
pdfDNSSEC = countDNSSEC / sum(countDNSSEC)


cdfUDP = np.cumsum(pdfUDP)
cdfTCP = np.cumsum(pdfTCP)
cdfTLS = np.cumsum(pdfTLS)
cdfHTTPS = np.cumsum(pdfHTTPS)
cdfDNSSEC = np.cumsum(pdfDNSSEC)

plt.plot(bins_count_UDP[1:], cdfUDP, label="CDF_DNS-over-UDP")
plt.plot(bins_count_TCP[1:], cdfTCP, label="CDF_DNS-over-TCP")
plt.plot(bins_count_TLS[1:], cdfTLS, label="CDF_DNS-over-TLS")
plt.plot(bins_count_HTTPS[1:], cdfHTTPS, label="CDF_DNS-over-HTTPS")
plt.plot(bins_count_DNSSEC[1:], cdfDNSSEC, label="CDF_DNSSEC")

#plt.xlim(1, 1)
#plt.yticks(np.arange(0,1,0.05))
#plt.xticks(np.arange(0,3.6,0.05))
plt.title(sys.argv[1], loc='left')
plt.xlabel("Latenza")
plt.ylabel("Cumulative Distribution Function")
plt.xticks(np.arange(0,0.4,0.005))
plt.legend(loc='upper left')
plt.savefig(sys.argv[2]+".png")


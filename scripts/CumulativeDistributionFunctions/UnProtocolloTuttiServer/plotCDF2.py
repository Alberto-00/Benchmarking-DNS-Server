# argv titoloGrafico NomeImg fileBind FilePower FileTECH 
from cProfile import label
from operator import le
import numpy as np 
import sys
import matplotlib.pyplot as plt 
#import pandas as pd 
#%matplotlib inline 
plt.rcParams["figure.figsize"] = [25.00, 10]
plt.rcParams["figure.autolayout"] = True

# No of Data points 
#N = 250
# Apri il file in modalità lettura
with open(sys.argv[3], 'r') as fileBind:
    # Leggi il contenuto del file
    contentBind = fileBind.read().rstrip(',')

# Suddividi i numeri in una lista
numbersBind = [float(num) for num in contentBind.split(',')]

with open(sys.argv[4], 'r') as filePower:
    # Leggi il contenuto del file
    contentPower = filePower.read().rstrip(',')

# Suddividi i numeri in una lista
numbersPower = [float(num) for num in contentPower.split(',')]

with open(sys.argv[5], 'r') as fileTech:
    # Leggi il contenuto del file
    contentTech = fileTech.read().rstrip(',')

# Suddividi i numeri in una lista
numbersTech = [float(num) for num in contentTech.split(',')]

NBind = len(numbersBind)
NPower = len(numbersPower)
NTech = len(numbersTech)

countBind, bins_count_bind = np.histogram(numbersBind, bins=len(numbersBind))
countPower, bins_count_power = np.histogram(numbersPower, bins=len(numbersPower))
countTech, bins_count_tech = np.histogram(numbersTech, bins=len(numbersTech))

pdfBind = countBind / sum(countBind)
pdfPower = countPower / sum(countPower)
pdfTech = countTech / sum(countTech)

cdfBind = np.cumsum(pdfBind)
cdfPower = np.cumsum(pdfPower)
cdfTech = np.cumsum(pdfTech)
# initializing random values 
#data=[]
# getting data of the histogram 
#N = len(data)
#count, bins_count = np.histogram(data, bins=len(data)) 

# finding the PDF of the histogram using count values 
#pdf = count / sum(count) 

# using numpy np.cumsum to calculate the CDF 
# We can also find using the PDF values by looping and adding 
#cdf = np.cumsum(pdf) 

# plotting PDF and CDF 
#plt.plot(bins_count[1:], pdf, color="red", label="PDF") 

plt.plot(bins_count_bind[1:], cdfBind, label="CDF_BIND")
plt.plot(bins_count_power[1:], cdfPower, label="CDF_PowerDNS")
plt.plot(bins_count_tech[1:], cdfTech, label="CDF_Technitium")
#plt.xlim(1, 1)
#plt.yticks(np.arange(0,1,0.05))
plt.xticks(np.arange(0,3.6,0.05))
plt.title(sys.argv[1])
plt.xlabel("Latenza")
plt.ylabel("Cumulative Distribution Function")
plt.legend() 
plt.savefig(sys.argv[2]+".png")


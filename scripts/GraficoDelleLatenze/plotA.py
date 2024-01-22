import numpy as np
import matplotlib.pyplot as plt
import os
import sys
plt.rcParams["figure.figsize"]=(50,23)
plt.rcParams.update({'font.size':15})
#arg: nomeFileLatenzeBIND nomeFileLatenzePDNS nomeFileLatenzeTech titoloGrafico nomeImg max

def aggiungi_zeri(numero):
	numero_str = str(numero)
	if len(numero_str) > 2 and numero_str[2] != '0':
		numero_str = numero_str[:2] + '00' + numero_str[2:]
		print(numero_str)
	return float(numero_str)

with open(sys.argv[1],'r') as fileBIND:
	contentBIND = fileBIND.read()
	contentBIND = contentBIND.rstrip(',')
	numbersBIND = [float(num) for num in contentBIND.split(',')]
#	numbersBINDagg = [aggiungi_zeri(numero) for numero in numbersBIND]
	#numbersPer100 = [num*100 for num in numbers]
	#print(numbersBIND)
	#print(numbersPer100)

with open(sys.argv[2],'r') as filePDNS:
	contentPDNS = filePDNS.read()
	contentPDNS = contentPDNS.rstrip(',')
	numbersPDNS = [float(num) for num in contentPDNS.split(',')]
	#numbersPer100 = [num*100 for num in numbers]
#	numbersPDNSagg = [aggiungi_zeri(numero) for numero in numbersPDNS]
#	print(numbersPDNSagg)
	#print(numbersPer100)

with open(sys.argv[3],'r') as fileTECH:
	contentTECH = fileTECH.read()
	contentTECH = contentTECH.rstrip(',')
	numbersTECH = [float(num) for num in contentTECH.split(',')]
#	numbersTECHagg = [aggiungi_zeri(numero) for numero in numbersTECH]
	#numbersPer100 = [num*100 for num in numbers]
	#print(numbersTECH)
	#print(numbersPer100)



# Visualizza il grafico delle prime 1000 ricompense per entrambi i modelli
plt.title("Richieste DNS"+sys.argv[4]+" sui server BIND9, PowerDNS e Technitium", loc="left")

#plt.rcParams["figure.autolayout"]=True

lineBIND = plt.plot(numbersBIND, zorder=10)
linePDNS = plt.plot(numbersPDNS, zorder=0)
lineTECH = plt.plot(numbersTECH, zorder=5)
#plt.plot([0.0056, 0.045, 6.7])
plt.xlabel("Numero di richieste")
plt.ylabel("Latenza")
plt.yticks(np.arange(0,float(sys.argv[6]), 0.005))
plt.xticks(np.arange(0,1000000,100000))
plt.legend(['BIND9','PowerDNS','Technitium'])
plt.savefig(sys.argv[5])

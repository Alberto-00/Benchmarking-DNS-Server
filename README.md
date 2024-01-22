# Tabella dei contenuti
- [Introduzione](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main#Introduzione)
- [Requisiti](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main#Requisiti)
  - [Installazione e configurazione dei server](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main#Installazione-e-configurazione-dei-server)
  - [Esecuzione del benchmarking](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main#Esecuzione-del-benchmarking)
- [Benchmarking eseguiti](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main#Benchmarking-eseguiti)  
- [Analisi dei risultati](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main#Analisi-dei-risultati)
- [Autori](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main#Autori)
# Introduzione
DNS è il protocollo che permette la risoluzione di domini in indirizzi IP, di conseguenza risulta fondamentale nella navigazione web. Inoltre permette la risoluzione di indirizzi mail, liste anti-spam fino a tecniche di bilanciamento del carico. Purtoppo però la sua versione originale basata su UDP o TCP non offre nessuna garanzia di sicurezza, quindi sono nate alternative che garantiscono la confidenzialità come DNS-over-TLS e DNS-over-HTTPS e poi DNSSEC che garantisce autenticità e integrità. Tali protocolli siccome si basano su tecniche crittografiche e protocolli più ad alto livello implicano inevitabilmente un maggiore overhead protocollare, che incide sulla latenza di risoluzione e sulle capacità dei server.
In questo progetto si è cercato di analizzare tale overhead effettuando il benchmarking dei protocolli: DNS-over-UDP, DNS-over-TCP, DNS-over-TLS, DNS-over-HTTPS e DNSSEC, ognuno dei quali è stato poi testato sui tre server: [BIND9](https://www.isc.org/bind/), [PowerDNS](https://www.powerdns.com/) e [Technitium](https://technitium.com/dns/). Le metriche prese in considerazione sono: distribuzione dei tempi di risposte delle query effettuare, latenza media, latenza massima e minima, deviazione standard, andamento delle Cumulative Distribution Functions, differenze di latenze tra i vari protocolli e i vari server e numero di query al secondo risolte dal server.

# Requisiti 
### Installazione e configurazione dei server
Al fine di garantire la replicabilità degli esperimenti sono presenti le macchine virtuali da installare in [VirtualBox](https://www.virtualbox.org/) al seguente link: [Google Drive con le Virtual Machine](https://drive.google.com/drive/folders/1RAqFOcWnDRnGb0TJHqvzB3Bh9TGvJJyF?usp=sharing). In ogni VM è presente il server DNS con la configurazione di un protocollo, il file di zona, i cinque dataset utilizzati per il benchmarking e i tool per eseguire il benchmarking.

In alternativa è possibile seguire i seguenti step:
- Utilizzare [VirtualBox](https://www.virtualbox.org/) versione 7.0.4 per installare [Debian](https://www.debian.org/distrib/) versione 12 64-bit
- Installare il server DNS che si vuole utilizzare
  - per BIND9 è possibile seguire la seguente guida: [https://bind9.readthedocs.io/en/v9.18.21/](https://bind9.readthedocs.io/en/v9.18.21/)
  - per Technitium è possibile seguire la seguente guida: [https://technitium.com/dns/help.html](https://technitium.com/dns/help.html)
  - per PowerDNS è possibile seguire la seguente guida: [https://doc.powerdns.com/](https://doc.powerdns.com/)
- Per la configurazione di ogni server si rimanda al paper di questo progetto: []()
- Il file di zona da utilizzare è presente a questo link: [Datasets/db.zip](https://github.com/mtolkien/Benchmarking-DNS-Server/blob/main/Datasets/db.zip)
- I cinque dataset utilizzati durante il benchmarkind sono presenti a questo link: [Datasets/Test files](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Datasets/Test%20files)
### Esecuzione del benchmarking  
- Per i protocolli DNS-over-UDP, DNS-over-TCP e DNS-over-TLS bisogna installare [dnsperf](https://github.com/DNS-OARC/dnsperf) ed eseguire il comando `dnsperf -O verbose-interval-stats -O latency-histogram -m <protocollo> -s <ipServer> -d <datasetBenchmark> -v`. Al posto di `<protocollo>` è possibile specificare `udp`, `tcp`, `dot` (per DNS-over-TLS), al posto di `<ipServer>` bisogna indicare l'IP del server, al posto di `<datasetBenchmark>` bisogna specificare il dataset di benchmarking.
- Per i protocolli DNS-over-HTTPS e DNSSEC bisogna usare `scriptKdig.sh`, quindi si rimanda a [/scripts/BenchmarkingDNSSEC_HTTPS](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/scripts/BenchmarkingDNSSEC_HTTPS)

# Benchmarking eseguiti
In questo lavoro è stato utilizzato `dnsperf` per il benchmarking di:
- DNS-over-UDP su BIND: i file ottenuti si trovano in [/Results/One protocol on all servers/UDP/BIND/dnsperf files/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/UDP/BIND/dnsperf%20files)
- DNS-over-UDP su PowerDNS: i file ottenuti si trovano in [/Results/One protocol on all servers/UDP/PowerDNS
/dnsperf files/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/UDP/PowerDNS/dnsperf%20files)
- DNS-over-UDP su Technitium: i file ottenuti si trovano in [/Results/One protocol on all servers/UDP/Technitium
/dnsperf files/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/UDP/Technitium/dnsperf%20files)
- DNS-over-TCP su BIND: i file ottenuti si trovano in [/Results/One protocol on all servers/TCP
/BIND/dnsperf files](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/TCP/BIND/dnsperf%20files)
- DNS-over-TCP su PowerDNS: i file ottenuti si trovano in [/Results/One protocol on all servers/TCP/PowerDNS
/dnsperf files/
](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/TCP/PowerDNS/dnsperf%20files)
- DNS-over-TCP su Technitium: i file ottenuti si trovano in [/Results/One protocol on all servers/TCP/Technitium
/dnsperf files/
](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/TCP/Technitium/dnsperf%20files)
- DNS-over-TLS su BIND: i file ottenuti si trovano in [/Results/One protocol on all servers/TLS/BIND
/dnsperf files/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/TLS/BIND/dnsperf%20files)
- DNS-over-TLS su PowerDNS: i file ottenuti si trovano in [/Results/One protocol on all servers/TLS/PowerDNS
/dnsperf files/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/TLS/PowerDNS/dnsperf%20files)
- DNS-over-TLS su Technitium: i file ottenuti si trovano in [/Results/One protocol on all servers/TLS/Technitium
/dnsperf files/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/TLS/Technitium/dnsperf%20files)

`scriptKdig.sh` è stato usato per:
- DNSSEC su BIND: i file ottenuti si trovano in [/Results/One protocol on all servers/DNSSEC/BIND
/files/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/DNSSEC/BIND/files)
- DNSSEC su PowerDNS: i file ottenuti si trovano in [/Results/One protocol on all servers/DNSSEC/PowerDNS
/files/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/DNSSEC/PowerDNS/files)
- DNSSEC su Technitium: i file ottenuti si trovano in [/Results/One protocol on all servers/DNSSEC/Technitium
/files/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/DNSSEC/Technitium/files)
- DNS-over-HTTPS su BIND: i file ottenuti si trovano in []()
- DNS-over-HTTPS su PowerDNS: i file ottenuti si trovano in []()
- DNS-over-HTTPS su Technitium: i file ottenuti si trovano in []()
  
# Analisi dei risultati
Per effettuare il pre-processing, analizzare e visualizzare i dati ottenuti da `dnsperf` e `scriptKdig.sh` è possibile utilizzare

# Autori

## Per DNS-over-UDP, DNS-over-TCP e DNS-over-TLS
Lo script `plotBarreErrori.sh` permette di generare il grafico in cui per un dato protocollo testato su ogni server viene mostrata la latenza minima, la latenza massima, la media e la deviazione standard. 

Prende in input i seguenti campi: 

- File output di dnsperf per il benchmarking del protocollo sul server BIND;
- File output di dnsperf per il benchmarking del protocollo sul server PowerDNS;
- File output di dnsperf per il benchmarking del protocollo sul server Technitium;
- Il titolo che verrà mostrato sopra il grafico;
- Nome dell'immagine che verrà prodotta;
  
#### Esempio di utilizzo 
Prendiamo in considerazione i tre file dati in output da dnsperf: `tls_fileBind_dnsperf.txt`, `tls_filePower_dnsperf.txt`, `tls_fileTECH_dnsperf.txt`.

L'esecuzione del comando `./plotBarreErrori.sh tls_fileBind_dnsperf.txt tls_filePower_dnsperf.txt tls_fileTECH_dnsperf.txt TLS_Benchmarking TLS_Benchmarking.png` produrrà grafici come quelli presenti in [Benchmarking-DNS-Server/Results/One protocol on all servers/TLS/Comparisons
/MinMaxDevMean/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/TLS/Comparisons/MinMaxDevMean)

**NOTA:** lo script `plotBarreErrori2.py` verrà eseguito automaticamente dallo script `plotBarreErrori.sh`

## Per DNSSEC e DNS-over-HTTPS

Siccome per questi due protocolli si è dovuto utilizzare lo script `scriptKdig.sh` non sono presenti i file di output di dnsperf ma direttamente i file con le latenze separate da virgola. Quindi in questo bisogna eseguire il file `plotBarreErroriDNSSEC_HTTPS.py` con i parametri: `fileLatenzeBind.txt fileLatenzePdns.txt fileLatenzeTech.txt TitoloGrafico NomeImg.png`

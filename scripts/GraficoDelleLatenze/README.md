Lo script `plotA.sh` permette di generare il grafico in cui vengono mostrare le latenze delle richieste effettuate durante il benchmarking di un protocollo su tutti i server. 
Prende in input i seguenti campi:
- file output di dnssperf del benchmarkind di BIND;
- file output di dnssperf del benchmarkind di PowerDNS;
- file output di dnssperf del benchmarkind di Technitium;
- titolo del grafico che verrà mostrato nel grafico;
- nome dell'immagine che verrà generata;
- valore massimo raggiungibile dall'asse delle ordinate (questione puramente estetica).

##### Esempio di utilizzo
Prendiamo in considerazione i file ottenuti da dnsperf: `tls_bench_dnsperf_BIND.txt`, `tls_bench_dnsperf_PowerDNS.txt`, `tls_bench_dnsperf_Tech.txt`.
L'esecuzione del comando `./plotA.sh tls_bench_dnsperf_BIND.txt tls_bench_dnsperf_PowerDNS.txt tls_bench_dnsperf_Tech.txt TLS_Benchmarking TLS_Benchmarking.png 1` produrrà grafici come quelli presenti in [Benchmarking-DNS-Server/Results/One protocol on all servers/TLS/Comparisons
/Latency graph/](https://github.com/mtolkien/Benchmarking-DNS-Server/tree/main/Results/One%20protocol%20on%20all%20servers/TLS/Comparisons/Latency%20graph)

**NOTA:** il file `plotA.py` verrà eseguito automaticamente da `plotA.sh`

